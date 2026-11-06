# Regression Test Design Prompt Template

**Category:** Testing  
**Use Case:** Regression Test Design  
**Role:** Software quality engineer preventing repeated defects  
**Task:** Design a test that fails before a bug fix and passes after it, without assuming execution occurred.  
**Input Placeholders:** `[BUG_DESCRIPTION]`, `[REPRODUCTION_STEPS]`, `[FIX_DETAILS]`, `[AFFECTED_CODE]`, `[TEST_FRAMEWORK]`  
**Expected Output Format:** Markdown sections: Regression Scenario, Test Code/Pseudocode, Pass/Fail Criteria, and Related Risks.

## Reusable Prompt

Act as a software quality engineer designing a regression test for a recently fixed defect.

**Bug:** [BUG_DESCRIPTION]  
**Steps that previously reproduced it:** [REPRODUCTION_STEPS]  
**Changes made in the fix:** [FIX_DETAILS]  
**Affected code or modules:** [AFFECTED_CODE]  
**Test framework (if known):** [TEST_FRAMEWORK]

Design a test that specifically detects the old failure. If code details are insufficient, provide clear pseudocode instead of inventing APIs. Do not claim to have run any test.

Return:
1. **Regression Scenario:** Given/When/Then description.
2. **Test Code or Pseudocode:** Implementation based on supplied details.
3. **Pass/Fail Criteria:** How to distinguish the old bug from the corrected behavior.
4. **Related Risks:** Adjacent cases worth testing.
