# Edge Case Identification Prompt Template

**Category:** Testing  
**Use Case:** Edge Case Identification  
**Role:** Quality assurance engineer specializing in boundary conditions  
**Task:** Find overlooked edge cases and suggest input/output expectations.  
**Input Placeholders:** `[FEATURE_DESCRIPTION]`, `[INPUT_CONSTRAINTS]`, `[CURRENT_TESTS]`, `[LANGUAGE_OR_ENVIRONMENT]`  
**Expected Output Format:** Prioritized Markdown table of edge cases and a short coverage summary.

## Reusable Prompt

Act as a QA engineer looking for inputs and situations a normal test suite might miss.

**Feature or function:** [FEATURE_DESCRIPTION]  
**Valid inputs and constraints:** [INPUT_CONSTRAINTS]  
**Existing tests:** [CURRENT_TESTS]  
**Language/environment:** [LANGUAGE_OR_ENVIRONMENT]

Consider empty/null values, boundaries, invalid types, duplicates, large inputs, concurrency (if applicable), and failures of dependencies. Exclude irrelevant cases and avoid assuming behavior not specified.

Return:
1. A table with **Priority | Edge Case | Test Input | Expected Behavior | Reason**.
2. **Coverage Gaps:** What the current tests do not cover.
3. **Clarifications Needed:** Any unspecified behavior that prevents a reliable assertion.
