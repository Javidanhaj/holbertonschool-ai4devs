# Unit Test Generation Prompt Template

**Category:** Testing  
**Use Case:** Unit Test Generation  
**Role:** Software test engineer  
**Task:** Write unit tests for a function's documented behavior using a specified framework.  
**Input Placeholders:** `[LANGUAGE]`, `[TEST_FRAMEWORK]`, `[SOURCE_CODE]`, `[EXPECTED_BEHAVIOR]`, `[DEPENDENCIES]`  
**Expected Output Format:** Executable test code followed by a brief test-case/coverage summary.

## Reusable Prompt

Act as a test engineer. Write unit tests for this `[LANGUAGE]` code using `[TEST_FRAMEWORK]`.

**Source code:**
```text
[SOURCE_CODE]
```

**Expected behavior and rules:** [EXPECTED_BEHAVIOR]  
**Dependencies or mocks available:** [DEPENDENCIES]

Test normal behavior, meaningful boundaries, and known failures. Mock external services rather than making destructive calls. Do not claim tests were executed or passed.

Return:
1. **Test Code:** A complete `[LANGUAGE]` test file using `[TEST_FRAMEWORK]`.
2. **Test Cases Covered:** Brief table with scenario and expected outcome.
3. **Missing Information:** Any ambiguity affecting expected assertions.
4. **How to Run:** Appropriate command, if it can be determined from the inputs.
