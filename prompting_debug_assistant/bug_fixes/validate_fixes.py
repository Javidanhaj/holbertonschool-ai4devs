"""Reproducible validation for all six Holberton AI-debugging fixes.
Run: python3 prompting_debug_assistant/bug_fixes/validate_fixes.py
Needs Python 3, Node.js, and GCC; creates C binaries only in a temporary directory.
"""
import contextlib
import io
import json
import runpy
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
results = []


def check(bug, case, input_value, expected, actual):
    passed = expected == actual
    results.append({"bug": bug, "case": case, "input": input_value,
                    "expected": str(expected), "actual": str(actual), "pass": passed})
    print(f"{bug} | {case} | expected={expected!s} | actual={actual!s} | {'PASS' if passed else 'FAIL'}")


def run(command):
    p = subprocess.run(command, capture_output=True, text=True, check=False)
    if p.returncode:
        raise RuntimeError(f"Command failed {command}:\n{p.stderr}")
    return p.stdout.strip()


def load_py(filename):
    with contextlib.redirect_stdout(io.StringIO()):
        return runpy.run_path(str(ROOT / filename))


# Python: five slicing cases, four order-total cases.
last_n = load_py('bug1_fixed.py')['last_n']
for case, items, n, expected in [
    ('normal', [10,20,30,40,50], 2, [40,50]),
    ('zero', [10,20,30,40,50], 0, []),
    ('full length', [10,20,30,40,50], 5, [10,20,30,40,50]),
    ('too large', [10,20,30,40,50], 8, [10,20,30,40,50]),
]:
    check('bug1', case, f'last_n({items}, {n})', expected, last_n(items, n))
try:
    last_n([1,2], -1)
    observed = 'no exception'
except Exception as exc:
    observed = type(exc).__name__
check('bug1', 'negative n', 'last_n([1,2], -1)', 'ValueError', observed)

total = load_py('bug2_fixed.py')['calculate_total']
for case, items, expected in [
    ('mixed', [{'price':12},{'price':3},{'item':'sample'},{'price':5}], 20),
    ('missing price', [{'item':'sample'}], 0),
    ('empty', [], 0),
    ('zero price', [{'price':0},{'price':7}], 7),
]:
    check('bug2', case, f'calculate_total({items})', expected, total(items))

# JavaScript: run the original corrected file inside a Node vm to call its functions.
js3 = r'''const fs=require('fs'),vm=require('vm');const ctx={console:{log(){}}};
vm.runInNewContext(fs.readFileSync(process.argv[1],'utf8'),ctx);
console.log(JSON.stringify([[70,80,90],[],[10,20]].map(x=>ctx.calculateAverage(x))));'''
res3 = json.loads(run(['node','-e',js3,str(ROOT/'bug3_fixed.js')]))
for (case, inp, expected), actual in zip([
    ('sample', '[70,80,90]', 80),('empty', '[]', 0),('two values', '[10,20]', 15)
], res3):
    check('bug3', case, f'calculateAverage({inp})', expected, actual)
check('bug3', 'main output', 'node bug3_fixed.js',
      'Average: 80\nExpected average: 80', run(['node',str(ROOT/'bug3_fixed.js')]))

js4 = r'''const fs=require('fs'),vm=require('vm');const ctx={console:{log(){}}};
vm.runInNewContext(fs.readFileSync(process.argv[1],'utf8'),ctx);
const pairs=[[100,.1],[40,.25],[100,0],[100,1],[100,-.1],[100,1.1]];
console.log(JSON.stringify(pairs.map(([p,r])=>{try{return ctx.applyDiscount(p,r)}catch(e){return 'Error'}})));'''
res4 = json.loads(run(['node','-e',js4,str(ROOT/'bug4_fixed.js')]))
for (case, inp, expected), actual in zip([
    ('10% discount','(100, 0.1)',90),('25% discount','(40, 0.25)',30),
    ('0% discount','(100, 0)',100),('100% discount','(100, 1)',0),
    ('negative rate','(100, -0.1)','Error'),('too large rate','(100, 1.1)','Error')
],res4):
    check('bug4', case, f'applyDiscount{inp}', expected, actual)
check('bug4', 'main output', 'node bug4_fixed.js',
      'Keyboard: $90.00\nMouse: $30.00\nExpected final prices: $90.00 and $30.00',
      run(['node',str(ROOT/'bug4_fixed.js')]))

# C: strict compilation and separate harness that calls the production functions.
with tempfile.TemporaryDirectory() as td:
    td = Path(td)
    for bug, sample, expected in [
        ('bug5', 'bug5_fixed.c', 'Sum: 15\nExpected sum: 15'),
        ('bug6', 'bug6_fixed.c', 'Administrator recognized\nExpected: Administrator recognized'),
    ]:
        exe = td/bug
        run(['gcc','-std=c11','-Wall','-Wextra','-Werror','-pedantic',
             str(ROOT/sample),'-o',str(exe)])
        check(bug, 'main output (strict build)', 'gcc -Werror && execute', expected, run([str(exe)]))

    harnesses = {
        'bug5': '''#define main original_main\n#include "bug5_fixed.c"\n#undef main\nint main(void) { int a[]={2,4,6};
    printf("%d\\n%d\\n%d\\n",sum_array(a,3),sum_array(a,0),sum_array(a,1)); return 0; }''',
        'bug6': '''#define main original_main\n#include "bug6_fixed.c"\n#undef main\nint main(void) { printf("%d\\n%d\\n%d\\n",is_admin("admin"),is_admin("guest"),is_admin("ADMIN")); return 0; }''',
    }
    for bug, source in harnesses.items():
        harness=td/f'{bug}_harness.c'
        harness.write_text(source)
        exe=td/f'{bug}_harness'
        run(['gcc','-std=c11','-Wall','-Wextra','-Werror','-pedantic',
             '-I',str(ROOT),str(harness),'-o',str(exe)])
        answers=run([str(exe)]).splitlines()
        cases = (
            [('three values','{2,4,6}, count=3','12'),
             ('zero count','{2,4,6}, count=0','0'),
             ('one value','{2,4,6}, count=1','2')]
            if bug=='bug5' else
            [('correct username','"admin"','1'),
             ('other username','"guest"','0'),
             ('case-sensitive','"ADMIN"','0')]
        )
        for (case, inp, expected), actual in zip(cases, answers):
            check(bug,case,inp,expected,actual)

passed = sum(x['pass'] for x in results)
print(f'\nFINAL: {passed}/{len(results)} checks passed')
if '--json' in sys.argv:
    (ROOT/'test_results.json').write_text(json.dumps(results,indent=2))
sys.exit(0 if passed==len(results) else 1)
