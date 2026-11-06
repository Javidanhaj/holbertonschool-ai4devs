# Refactoring Prompt Template

**Category:** Code Quality  
**Use Case:** Refactoring Existing Code  
**Role:** Senior software engineer reviewing a maintainability change  
**Task:** Refactor existing code for readability and maintainability without changing its observable behavior.  
**Input Placeholders:** `[LANGUAGE]`, `[CODE_BLOCK]`, `[INTENDED_BEHAVIOR]`, `[CONSTRAINTS]`  
**Expected Output Format:** Markdown sections: Refactored Code, What Changed, Behavior Risks, and Verification Steps.

## Reusable Prompt

Act as a senior software engineer. Review this `[LANGUAGE]` code and refactor it to make it easier to read and maintain.

**Original code:**
```text
[CODE_BLOCK]
```

**What the code should do:** [INTENDED_BEHAVIOR]  
**Constraints (public APIs, dependencies, coding style, etc.):** [CONSTRAINTS]

Keep the same externally visible behavior and preserve the required interfaces. Do not add unnecessary dependencies. If the intended behavior is unclear, state your assumptions instead of silently changing functionality.

Respond with:
1. **Refactored Code:** Complete code in a `[LANGUAGE]` code block.
2. **What Changed:** Short bullets explaining the main improvements.
3. **Behavior Risks:** Anything that might behave differently or needs review.
4. **Verification Steps:** Tests or checks to confirm behavior was preserved.
