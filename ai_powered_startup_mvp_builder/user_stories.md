# StudyFlow AI — MVP User Stories

These stories implement the scope defined in `mvp_concept.md`: a responsive, single-student study planner with account security, course and assignment management, editable weekly scheduling, deadline visibility, and progress tracking. Each story has testable acceptance criteria.

## Story 1 — Create an account
**Role / goal / benefit:** As a university student, I want to sign up with an email and password so that I can save my planning data securely.

**Acceptance criteria:**
- A valid email and a password meeting the stated minimum length create an account; the email must be unique.
- Invalid or duplicate email submissions display a useful error and do not create an account.
- Passwords are stored as secure password hashes rather than plaintext.

**Priority:** MVP

## Story 2 — Log in and protect private data
**Role / goal / benefit:** As a registered student, I want to log in and see only my own information so that my coursework stays private.

**Acceptance criteria:**
- Valid credentials establish a session; invalid credentials are rejected without disclosing whether the email exists.
- Unauthenticated requests for private data are rejected.
- A user cannot read or change another user's courses, assignments, or study sessions by modifying record IDs.

**Priority:** MVP

## Story 3 — Manage courses
**Role / goal / benefit:** As a student, I want to add, rename, view, and delete courses so that I can organize my coursework by subject.

**Acceptance criteria:**
- A course with a nonempty name appears in the signed-in student's course list.
- Editing a course updates its name; submitting a blank name shows a validation error.
- Deleting a course requires confirmation and explains what will happen to its assignments before deletion.

**Priority:** MVP

## Story 4 — Manage assignments and deadlines
**Role / goal / benefit:** As a student, I want to create, update, complete, and delete assignments so that I can track what needs to be done.

**Acceptance criteria:**
- A new assignment records a title, linked course, due date/time, and positive estimated study duration.
- Students can edit, complete, or delete their own assignments; the updated state persists after refresh.
- Blank titles, invalid dates, and nonpositive durations show clear errors without saving.

**Priority:** MVP

## Story 5 — Enter weekly availability
**Role / goal / benefit:** As a student balancing classes and work, I want to specify my available study periods so that the suggested schedule fits my week.

**Acceptance criteria:**
- The student can create, edit, and remove time windows for specific days of the week.
- A time window must have an end time after its start time and cannot overlap another availability window for the same student and day.
- Saved availability is used when generating a new plan.

**Priority:** MVP

## Story 6 — Generate a weekly study plan
**Role / goal / benefit:** As a student, I want suggested study sessions based on deadlines, workload, and availability so that I know what to work on next.

**Acceptance criteria:**
- Plan generation considers incomplete assignments, their deadlines and estimated time, plus the student's saved availability.
- Suggested sessions fall inside availability windows and do not overlap each other; tasks due soon are prioritized.
- If AI generation is unavailable, a rules-based fallback returns a usable plan or explains when available time is insufficient.

**Priority:** MVP

## Story 7 — Edit the generated schedule
**Role / goal / benefit:** As a student, I want to reschedule study sessions manually so that I can adapt the plan when my circumstances change.

**Acceptance criteria:**
- A student can change the date/time of an uncompleted session and see the updated schedule immediately.
- The system rejects invalid times and overlapping sessions with a clear message.
- Manual changes persist after page refresh and are not silently overwritten by later plan generation.

**Priority:** MVP

## Story 8 — See a deadline dashboard
**Role / goal / benefit:** As a student, I want one dashboard showing upcoming and overdue assignments so that I can prioritize urgent work.

**Acceptance criteria:**
- Open assignments display their course, title, deadline, and status, sorted by due date.
- Overdue, upcoming, and completed assignments can be visually distinguished.
- The dashboard shows only the signed-in student's assignments and updates after changes.

**Priority:** MVP

## Story 9 — Track completed work
**Role / goal / benefit:** As a student, I want to mark study sessions and assignments complete so that I can see what I have accomplished.

**Acceptance criteria:**
- A student can mark their own study session completed and reverse the action if needed.
- A student can mark an assignment completed; completed assignments no longer receive new suggested sessions.
- Completion status is stored and remains accurate after refresh.

**Priority:** MVP

## Story 10 — View weekly progress
**Role / goal / benefit:** As a student, I want a weekly completion summary so that I can judge whether I am following my plan.

**Acceptance criteria:**
- The weekly summary shows completed versus scheduled study sessions for the selected week.
- It calculates a completion percentage with a documented zero-session case (display 0% and a "No sessions planned" message).
- Updating session completion changes the summary without counting the same session twice.

**Priority:** High

## Prioritization and boundaries
- **MVP:** Stories 1–9 are needed for a complete first-use journey: sign in → add courses/tasks → set availability → generate and edit a plan → track deadlines and completion.
- **High:** Story 10 provides additional value after the end-to-end planner works.
- **Out of scope:** Collaborative calendars, university LMS integration, payments, native apps, and push notifications.
