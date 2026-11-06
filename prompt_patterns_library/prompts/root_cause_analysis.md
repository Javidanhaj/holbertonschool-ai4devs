# Root Cause Analysis Prompt Template

**Category:** Debugging  
**Use Case:** Root Cause Analysis  
**Role:** Incident investigator and backend engineer  
**Task:** Identify testable hypotheses for a recurring defect and determine how to confirm the root cause.  
**Input Placeholders:** `[EXPECTED_BEHAVIOR]`, `[ACTUAL_BEHAVIOR]`, `[LOGS]`, `[RECENT_CHANGES]`, `[AFFECTED_COMPONENTS]`  
**Expected Output Format:** Markdown sections: Symptoms, Hypotheses, Evidence Plan, Root Cause Status, and Prevention.

## Reusable Prompt

Act as an incident investigator. Help find the underlying cause of a recurring software defect rather than suggesting only a workaround.

**Expected behavior:** [EXPECTED_BEHAVIOR]  
**Actual behavior:** [ACTUAL_BEHAVIOR]  
**Logs and errors:** [LOGS]  
**Recent changes:** [RECENT_CHANGES]  
**Affected components:** [AFFECTED_COMPONENTS]

Separate observations from assumptions. Never claim to have reproduced the bug unless evidence is provided. Prioritize inexpensive diagnostic checks.

Return:
1. **Symptoms:** Facts confirmed by the input.
2. **Hypotheses:** Ranked possible causes with supporting and contradicting evidence.
3. **Evidence Plan:** Tests or logs needed to confirm or reject each hypothesis.
4. **Root Cause Status:** Confirmed, likely, or unresolved, with justification.
5. **Prevention:** Fix and regression-prevention suggestions once validated.
