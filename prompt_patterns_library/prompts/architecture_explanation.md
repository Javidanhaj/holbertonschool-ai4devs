# Architecture Explanation Prompt Template

**Category:** Documentation  
**Use Case:** Architecture Explanation  
**Role:** Software architect explaining an existing design  
**Task:** Describe component responsibilities, dependencies, data flow, and trade-offs.  
**Input Placeholders:** `[SYSTEM_GOAL]`, `[COMPONENTS]`, `[DATA_FLOW]`, `[DEPENDENCIES]`, `[DESIGN_DECISIONS]`  
**Expected Output Format:** Markdown sections: Overview, Components, Request/Data Flow, Design Rationale, and Risks.

## Reusable Prompt

Act as a software architect. Explain the system described below to a developer joining the project.

**System goal:** [SYSTEM_GOAL]  
**Main components:** [COMPONENTS]  
**Known data flow:** [DATA_FLOW]  
**Dependencies and integrations:** [DEPENDENCIES]  
**Known design decisions:** [DESIGN_DECISIONS]

Explain how the components interact and why the design may have been chosen. Distinguish documented decisions from your own interpretation. Do not invent architecture details.

Return:
1. **Overview:** One paragraph.
2. **Components:** Table of component and responsibility.
3. **Request/Data Flow:** Numbered sequence from input to output.
4. **Design Rationale:** Known benefits and trade-offs.
5. **Risks and Unknowns:** Dependencies, scaling concerns, and open questions.
