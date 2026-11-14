# Team Ideation — AI-Enhanced Hackathon

## Brainstormed Ideas

| Idea | Problem addressed | Proposed MVP | Decision |
|---|---|---|---|
| **StudyFlow AI** — AI Study Planner | Students struggle to balance assignments, deadlines, and available study time. | Courses, deadlines, availability, suggested study sessions, progress tracking. | **Chosen** |
| **SmartNotes** — Lecture Notes Summarizer | Students spend too much time reviewing long lecture notes. | Paste notes, generate summaries, create revision questions. | Not selected: evaluating summary accuracy would require more content review. |
| **TeamTask AI** — Group Project Organizer | Student teams lose track of tasks and responsibilities. | Task board, owners, deadlines, AI-generated task breakdowns. | Not selected: collaboration and permissions add complexity to the MVP. |

## Chosen Product

**StudyFlow AI** is a lightweight web app that helps university students plan study time around real academic deadlines. AI-assisted suggestions help students turn a list of assignments and free hours into an actionable weekly schedule.

## Problem Statement

University students often track assignments across several courses using disconnected notes and calendars. They may know *what* to finish but struggle to decide *when* to study, especially when deadlines overlap. Our MVP will give them one place to enter coursework and availability, then suggest a realistic study plan they can adjust themselves.

## Target Users

- **Primary:** University students managing multiple courses and deadlines.
- **Secondary:** Students working part-time or balancing other commitments who need flexible scheduling.

## MVP Features (5)

1. **Course and assignment management:** Create, edit, and complete coursework with titles, estimated effort, and due dates.
2. **Weekly availability input:** Record free study slots and preferred session duration.
3. **AI-assisted study schedule:** Generate suggested sessions based on deadlines, effort, and availability; offer a rules-based fallback if AI is unavailable.
4. **Manual schedule editing:** Move or remove suggested sessions without losing the original assignment information.
5. **Progress dashboard:** Mark sessions complete and view outstanding assignments and upcoming deadlines.

## MVP Constraints and Non-Goals

- Build a responsive web prototype suitable for desktop and mobile.
- Prioritize clear behavior and basic validation over advanced personalization.
- Do not include university system integrations, payment processing, social features, or push notifications in the first release.
- Suggestions must not invent assignments or override student edits; students retain final control.
- Treat student workload data as private and avoid including personal information in external AI prompts where possible.

## Proposed Team Roles

*Names are left as role placeholders until actual team members are confirmed; this table does not claim these are assigned people.*

| Member | Proposed Role | Main Responsibilities |
|---|---|---|
| Team Member 1 | Product Lead / Documentation | Define scope, prioritize stories, track demo readiness, write project documentation. |
| Team Member 2 | Frontend / UI-UX Developer | Build responsive screens, forms, schedule view, and usability checks. |
| Team Member 3 | Backend / Database Developer | Design data models, CRUD endpoints, validation, and persistence. |
| Team Member 4 | AI Integration / Testing Lead | Develop scheduling prompts or rules, test edge cases, and verify generated plans. |

*For a smaller team, roles can be combined and reassigned based on actual membership.*

## Success Criteria

- A student can create a course and at least one assignment.
- A student can specify available study hours and obtain a suggested schedule.
- A student can edit a suggested session and mark a session completed.
- The demo works on a desktop and phone-width browser without horizontal overflow.
- A sample end-to-end workflow can be demonstrated without real university integrations.

## Initial Implementation Plan

1. Agree on the data entities and user stories.
2. Implement course, assignment, and availability forms.
3. Build a basic scheduling algorithm; add optional AI refinement.
4. Add schedule editing and completion tracking.
5. Test typical, empty-input, and conflicting-deadline cases; prepare the demo.
