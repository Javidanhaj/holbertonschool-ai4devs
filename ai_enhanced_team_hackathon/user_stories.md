# StudyFlow AI — MVP User Stories

These stories implement the scope agreed in `team_ideation.md`: course and assignment management, availability, schedule generation, manual edits, and progress. Priority **MVP** means required for the hackathon demonstration.

## US-01 — Access a personal workspace
**Story:** As a student, I want to sign in to my workspace so that my coursework and study plans remain private.

**Acceptance criteria:**
- A student can sign in using an account and access only their own courses and schedules.
- Unauthenticated requests to private data are rejected.
- Signing out ends the active session.

**Priority:** MVP

## US-02 — Manage courses
**Story:** As a student, I want to create and rename my courses so that I can organize assignments by subject.

**Acceptance criteria:**
- A nonempty course name can be saved and appears in the course list.
- A student can rename or delete their own course; deletion requires confirmation if assignments exist.
- Blank course names are rejected with an explanation.

**Priority:** MVP

## US-03 — Add assignments
**Story:** As a student, I want to record an assignment with its deadline and estimated effort so that I know what needs to be scheduled.

**Acceptance criteria:**
- Saving requires a course, title, due date, and positive estimated minutes.
- Saved assignments appear under the selected course and in the upcoming-work list.
- Invalid dates or nonpositive estimates produce an error and are not saved.

**Priority:** MVP

## US-04 — Update assignment status
**Story:** As a student, I want to edit or complete assignments so that the planner reflects my current workload.

**Acceptance criteria:**
- I can edit the title, deadline, and estimated effort of my own assignment.
- Marking an assignment completed removes its remaining work from future schedule generation.
- Updates remain available after refreshing the page.

**Priority:** MVP

## US-05 — Set weekly availability
**Story:** As a student, I want to enter the times I am free to study so that suggested sessions fit my routine.

**Acceptance criteria:**
- I can add and remove availability windows with weekday, start time, and end time.
- The end time must be after the start time; invalid windows are rejected.
- My availability is saved and can be reused when generating a new plan.

**Priority:** MVP

## US-06 — Generate a realistic study plan
**Story:** As a student, I want a suggested weekly plan based on deadlines and free time so that I know when to work on assignments.

**Acceptance criteria:**
- Generating a plan uses only my incomplete assignments and recorded availability.
- Suggested sessions do not overlap and do not extend past an assignment deadline or outside an availability window.
- If the workload cannot fit, the app shows unscheduled effort rather than silently discarding it.

**Priority:** MVP

## US-07 — Keep planning available when AI fails
**Story:** As a student, I want a usable schedule even if the AI service is unavailable so that I can still plan my week.

**Acceptance criteria:**
- If the external AI request times out or fails, a deterministic scheduling fallback runs.
- The UI labels the result as a fallback plan and does not claim it was AI-generated.
- The plan does not introduce tasks that I did not enter.

**Priority:** High

## US-08 — Edit suggested sessions
**Story:** As a student, I want to move or remove suggested sessions so that I remain in control of my timetable.

**Acceptance criteria:**
- I can move a study session to another valid time within my available hours.
- Overlapping or out-of-window changes are rejected with a clear message.
- My manual edits persist after page reload and are not silently overwritten.

**Priority:** MVP

## US-09 — Track completed study sessions
**Story:** As a student, I want to mark sessions complete so that I can measure my progress.

**Acceptance criteria:**
- Each scheduled session can be marked completed or returned to pending.
- The dashboard counts completed versus planned sessions correctly.
- Status changes persist after a refresh.

**Priority:** MVP

## US-10 — Review upcoming work
**Story:** As a student, I want a dashboard of upcoming deadlines and unfinished assignments so that I can prioritize my next actions.

**Acceptance criteria:**
- The dashboard lists incomplete assignments ordered by upcoming due date.
- It displays the next scheduled study session and a completed-session count.
- An empty state explains how to add a first course or assignment.

**Priority:** MVP

## Scope and Definition of Done
- Stories are demonstrated on desktop and phone-width screens.
- Each state-changing action validates inputs and enforces ownership of records.
- Core flows work without payment, university integrations, social features, or push notifications.
- At least one end-to-end scenario is tested: course -> assignment -> availability -> plan -> edit -> complete.
