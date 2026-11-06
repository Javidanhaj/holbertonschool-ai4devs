# Performance Optimization Prompt Template

**Category:** Code Quality  
**Use Case:** Performance Optimization  
**Role:** Performance-minded software engineer  
**Task:** Identify bottlenecks and propose safe improvements in execution time or memory use.  
**Input Placeholders:** `[LANGUAGE]`, `[CODE_BLOCK]`, `[INPUT_SIZES]`, `[BOTTLENECK]`, `[CONSTRAINTS]`  
**Expected Output Format:** Markdown sections: Bottlenecks, Optimized Code, Complexity and Trade-offs, and Measurement Plan.

## Reusable Prompt

Act as a software engineer focused on performance. Analyze the following `[LANGUAGE]` code.

```text
[CODE_BLOCK]
```

**Expected input sizes and workload:** [INPUT_SIZES]  
**Observed slowdown or bottleneck:** [BOTTLENECK]  
**Constraints:** [CONSTRAINTS]

Suggest improvements that preserve correct behavior. Distinguish measured issues from performance guesses. Avoid claiming speedups without benchmarks.

Respond with:
1. **Bottlenecks:** Where unnecessary time or memory may be spent.
2. **Optimized Code:** Revised code in a `[LANGUAGE]` code block.
3. **Complexity and Trade-offs:** Expected time/memory complexity before and after, with limitations.
4. **Measurement Plan:** How to benchmark the proposed improvement using representative inputs.
