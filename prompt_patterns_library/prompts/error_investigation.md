# Error Investigation Prompt Template

**Category:** Debugging  
**Use Case:** Error Message Investigation  
**Role:** Debugging engineer helping investigate a failure safely  
**Task:** Explain an error, prioritize possible causes, and provide diagnostic steps before fixes.  
**Input Placeholders:** `[ERROR_MESSAGE]`, `[LANGUAGE_AND_RUNTIME]`, `[RELEVANT_CODE]`, `[REPRODUCTION_STEPS]`  
**Expected Output Format:** Markdown sections: Meaning, Likely Causes, Diagnostic Steps, and Safe Fixes.

## Reusable Prompt

Act as a debugging engineer. I encountered this exact error:

```text
[ERROR_MESSAGE]
```

**Language, runtime, and operating system:** [LANGUAGE_AND_RUNTIME]  
**Relevant code or command:** [RELEVANT_CODE]  
**Steps to reproduce:** [REPRODUCTION_STEPS]

Explain the message in plain language. Rank the most plausible causes, but do not assume a cause is confirmed. Suggest low-risk checks before any commands that change files or permissions.

Return:
1. **Meaning:** What the error usually indicates.
2. **Likely Causes:** Ranked hypotheses and why each fits.
3. **Diagnostic Steps:** Safe commands or checks and the expected interpretation of their output.
4. **Safe Fixes:** A fix for each cause only after its diagnosis is confirmed.
