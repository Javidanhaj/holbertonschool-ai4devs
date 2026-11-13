#!/usr/bin/env python3
"""Reproducible 30-check validation for Smart Bug Bounty fixes."""
from pathlib import Path
import importlib.util
import json
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
passed = 0

def check(name, condition):
    global passed
    if not condition:
        raise AssertionError(name)
    passed += 1
    print(f"PASS {passed:02d}: {name}")

def load(filename):
    spec = importlib.util.spec_from_file_location(filename.replace('.', '_'), HERE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

b1 = load('bug1_fixed.py')
a=[1,2,3,4]
check('bug1 last 2', b1.last_items(a,2)==[3,4])
check('bug1 last 1', b1.last_items(a,1)==[4])
check('bug1 zero', b1.last_items(a,0)==[])
check('bug1 oversized', b1.last_items(a,20)==a)
check('bug1 no mutation', a==[1,2,3,4])

b2 = load('bug2_fixed.py')
check('bug2 ignores invalid', b2.average_score([80,90,None])==85)
check('bug2 basic average', b2.average_score([70,80,90])==80)
check('bug2 empty', b2.average_score([])==0)
check('bug2 all invalid', b2.average_score(['absent',None])==0)
check('bug2 boundary scores', b2.average_score([0,100,101])==50)

js=r"""
const assert = require('node:assert/strict');
const {filterByPrice} = require('./bug3_fixed.js');
const {uniqueUsernames} = require('./bug4_fixed.js');
const checks = [
 ['bug3 boundary price', () => assert.deepEqual(filterByPrice([{price:5}],5),[{price:5}])],
 ['bug3 mixed prices', () => assert.deepEqual(filterByPrice([{price:2},{price:7}],5),[{price:2}])],
 ['bug3 empty list', () => assert.deepEqual(filterByPrice([],5),[])],
 ['bug3 zero price', () => assert.deepEqual(filterByPrice([{price:0},{price:1}],0),[{price:0}])],
 ['bug3 negative limit rejects', () => assert.throws(()=>filterByPrice([], -1))],
 ['bug4 duplicates case-insensitive', () => assert.deepEqual(uniqueUsernames(['Zara','ZARA']),['zara'])],
 ['bug4 empty list', () => assert.deepEqual(uniqueUsernames([]),[])],
 ['bug4 repeats', () => assert.deepEqual(uniqueUsernames(['ali','ali','ali']),['ali'])],
 ['bug4 insertion order', () => assert.deepEqual(uniqueUsernames(['zara','ali','mina']),['zara','ali','mina'])],
 ['bug4 whitespace', () => assert.deepEqual(uniqueUsernames([' ali ','ALI']),['ali'])],
];
for (const [label, run] of checks) {run(); console.log('PASS: '+label)}
"""
# Use js code via node -e and require absolute paths by executing with cwd
node=subprocess.run(['node','-e',js],cwd=HERE,capture_output=True,text=True,check=True)
for row in node.stdout.splitlines():
    if row.startswith('PASS: '):
        check(row[6:],True)

java=r"""
public class FixTests {
  static int checks = 0;
  static void ok(String name, boolean v) {
    if (!v) throw new AssertionError(name);
    checks++;
    System.out.println("PASS: " + name);
  }
  static void rejects(String name, Runnable test) {
    boolean failed = false;
    try { test.run(); } catch (IllegalArgumentException ex) { failed=true; }
    ok(name, failed);
  }
  public static void main(String[] args) {
    ok("bug5 positive",Bug5.maxValue(new int[]{4,2,9})==9);
    ok("bug5 negatives",Bug5.maxValue(new int[]{-9,-3,-7})==-3);
    ok("bug5 singleton",Bug5.maxValue(new int[]{8})==8);
    ok("bug5 zeros",Bug5.maxValue(new int[]{0,-2})==0);
    rejects("bug5 empty rejected",()->Bug5.maxValue(new int[]{}));
    ok("bug6 middle range",Bug6.rangeSum(new int[]{2,4,6,8},1,3)==18);
    ok("bug6 singleton",Bug6.rangeSum(new int[]{2,4},0,0)==2);
    ok("bug6 full range",Bug6.rangeSum(new int[]{2,4,6},0,2)==12);
    ok("bug6 negatives",Bug6.rangeSum(new int[]{-3,2,-1},0,2)==-2);
    rejects("bug6 invalid rejected",()->Bug6.rangeSum(new int[]{1},0,1));
  }
}
"""
with tempfile.TemporaryDirectory() as tmp:
    out=Path(tmp)
    (out/'FixTests.java').write_text(java)
    subprocess.run(['javac','-d',str(out),str(HERE/'bug5_fixed.java'),str(HERE/'bug6_fixed.java'),str(out/'FixTests.java')],check=True,capture_output=True,text=True)
    result=subprocess.run(['java','-cp',str(out),'FixTests'],check=True,capture_output=True,text=True)
    for row in result.stdout.splitlines():
        if row.startswith('PASS: '):
            check(row[6:],True)
print(f'\nTOTAL: {passed}/30 PASS')
assert passed==30
