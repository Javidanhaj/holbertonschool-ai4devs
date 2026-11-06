# Prompt Use Cases

This document identifies recurring software-development tasks where reusable AI prompt patterns can improve consistency, speed, and quality. Each use case describes the goal, expected input, and desired output.

## Code Quality

- **Refactoring Existing Code**
  - **Goal**: Improve readability and maintainability without changing observable behavior.
  - **Input**: A function or module in `[LANGUAGE]`, its purpose, and any compatibility constraints.
  - **Output**: Refactored code, a summary of changes, and possible behavior risks.

- **Performance Optimization**
  - **Goal**: Identify unnecessary work and improve time or memory efficiency.
  - **Input**: Code in `[LANGUAGE]`, typical input sizes, and observed performance bottlenecks.
  - **Output**: Suggested optimizations, revised code, and an explanation of trade-offs and complexity.

- **Code Review**
  - **Goal**: Detect maintainability, correctness, and security concerns before merging changes.
  - **Input**: A code snippet or pull-request diff, relevant requirements, and project conventions.
  - **Output**: Prioritized review findings with code locations, reasons, and suggested fixes.

## Debugging

- **Error Message Investigation**
  - **Goal**: Understand an error and identify the most likely cause.
  - **Input**: The exact error message, relevant code, runtime environment, and reproduction steps.
  - **Output**: Possible causes ranked by likelihood, checks to perform, and safe next steps.

- **Root Cause Analysis**
  - **Goal**: Find why a recurring defect happens instead of applying a temporary workaround.
  - **Input**: Expected versus actual behavior, logs, recent changes, and affected components.
  - **Output**: Root-cause hypotheses, evidence needed to verify each, and a proposed correction.

- **Minimal Reproduction**
  - **Goal**: Isolate a bug into the smallest example that still demonstrates the failure.
  - **Input**: A failing application scenario, code fragments, and setup details.
  - **Output**: A minimal reproducible example, execution steps, and the expected failure.

## Documentation

- **README Creation**
  - **Goal**: Help developers understand, install, and run a project.
  - **Input**: Project purpose, technology stack, configuration, and run commands.
  - **Output**: A structured README with prerequisites, setup, usage, and troubleshooting sections.

- **API Documentation**
  - **Goal**: Make an endpoint understandable and usable by other developers.
  - **Input**: Endpoint definitions, request/response schemas, authentication details, and examples.
  - **Output**: Endpoint documentation with parameters, examples, status codes, and error cases.

- **Architecture Explanation**
  - **Goal**: Explain how components interact and why a design was chosen.
  - **Input**: System components, data flow, dependencies, and known design decisions.
  - **Output**: A concise architecture overview describing responsibilities, interactions, and trade-offs.

## Testing

- **Unit Test Generation**
  - **Goal**: Verify that a function behaves correctly for defined inputs.
  - **Input**: Source code in `[LANGUAGE]`, expected behavior, and the testing framework.
  - **Output**: Unit tests with clear names, assertions, and brief coverage notes.

- **Edge Case Identification**
  - **Goal**: Find boundary conditions and unusual inputs that normal tests may miss.
  - **Input**: Function or feature requirements, input constraints, and current test cases.
  - **Output**: A prioritized list of edge cases with expected results and suggested test inputs.

- **Regression Test Design**
  - **Goal**: Prevent a previously fixed bug from reappearing.
  - **Input**: Bug description, reproduction steps, the fix, and affected modules.
  - **Output**: Regression test scenarios, test code or pseudocode, and pass/fail expectations.
