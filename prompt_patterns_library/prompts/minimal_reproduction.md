# Minimal Reproduction Prompt Template

**Category:** Debugging  
**Use Case:** Minimal Reproduction  
**Role:** Software engineer isolating a bug for investigation  
**Task:** Reduce a failing scenario to the smallest reproducible example.  
**Input Placeholders:** `[LANGUAGE_AND_ENVIRONMENT]`, `[FAILING_SCENARIO]`, `[CODE_FRAGMENTS]`, `[SETUP_DETAILS]`  
**Expected Output Format:** Markdown sections: Minimal Example, Setup and Run, Expected vs. Actual, and Assumptions.

## Reusable Prompt

Act as a software engineer preparing a minimal reproducible example (MRE) for a bug report.

**Environment:** [LANGUAGE_AND_ENVIRONMENT]  
**Failure description:** [FAILING_SCENARIO]  
**Available code:**
```text
[CODE_FRAGMENTS]
```
**Dependencies and setup:** [SETUP_DETAILS]

Remove unrelated features while preserving the conditions that appear necessary for the failure. Do not invent observed output or claim the example was executed.

Return:
1. **Minimal Example:** The smallest self-contained code sample you can reasonably construct.
2. **Setup and Run:** Exact dependencies and commands.
3. **Expected vs. Actual:** What should happen versus the reported failure.
4. **Assumptions:** Missing details and what would need to be verified in a real run.
