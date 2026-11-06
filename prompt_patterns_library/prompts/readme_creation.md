# README Creation Prompt Template

**Category:** Documentation  
**Use Case:** README Creation  
**Role:** Developer documentation writer  
**Task:** Draft a clear README for developers who need to set up and use a project.  
**Input Placeholders:** `[PROJECT_NAME]`, `[PROJECT_PURPOSE]`, `[TECH_STACK]`, `[SETUP_STEPS]`, `[RUN_COMMANDS]`, `[CONFIGURATION]`  
**Expected Output Format:** A complete Markdown README with Overview, Prerequisites, Installation, Configuration, Usage, and Troubleshooting sections.

## Reusable Prompt

Act as a developer documentation writer. Create a README.md for the following project:

**Name:** [PROJECT_NAME]  
**Purpose:** [PROJECT_PURPOSE]  
**Technology stack:** [TECH_STACK]  
**Installation steps and dependencies:** [SETUP_STEPS]  
**Commands to run or test it:** [RUN_COMMANDS]  
**Configuration and environment variables:** [CONFIGURATION]

Write for a developer encountering the repository for the first time. Use commands exactly as provided; do not invent installation instructions, URLs, or secrets. Mark genuinely missing details as 'Not provided.'

Return a Markdown README with these sections:
1. Overview
2. Prerequisites
3. Installation
4. Configuration
5. Usage and Tests
6. Troubleshooting
