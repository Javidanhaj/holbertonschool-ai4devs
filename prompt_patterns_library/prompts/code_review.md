# Code Review Prompt Template

**Category:** Code Quality  
**Use Case:** Code Review  
**Role:** Senior peer reviewer prioritizing correctness, security, and maintainability  
**Task:** Review code or a pull-request diff and provide specific, actionable feedback.  
**Input Placeholders:** `[LANGUAGE]`, `[CODE_OR_DIFF]`, `[REQUIREMENTS]`, `[CONVENTIONS]`  
**Expected Output Format:** A prioritized Markdown review table followed by a summary and recommended tests.

## Reusable Prompt

You are a senior developer reviewing a proposed change in `[LANGUAGE]`.

**Code or diff:**
```text
[CODE_OR_DIFF]
```

**Requirements:** [REQUIREMENTS]  
**Project conventions:** [CONVENTIONS]

Look for correctness, security, edge cases, clarity, and maintainability. Do not invent file names, line numbers, or runtime results. Identify any missing context.

Return:
1. A table with **Severity (High/Medium/Low) | Location | Finding | Why it matters | Suggested fix**.
2. **Overall Assessment:** Two to four sentences describing readiness and highest risk.
3. **Recommended Tests:** Specific cases to run before merging.
