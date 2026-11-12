# StudyFlow AI — User Stories

These user stories define the initial requirements for StudyFlow AI, an academic planning web application. Each story follows the role–goal–benefit format and includes testable acceptance criteria. **MVP** stories form the initial release; other priorities indicate subsequent enhancements.

### User Story 1 — Create an Account
As a university student, I want to register and sign in to a personal account so that my courses, tasks, and study plans are available in my own workspace.

**Acceptance Criteria**:
- A student can register with a valid email address and password and then sign in using those credentials.
- Invalid credentials produce an error without granting access.
- After signing in, the student can access only their own private workspace by default.

**Priority**: MVP

### User Story 2 — Manage Courses
As a university student, I want to add and edit my courses so that I can organize academic work by subject.

**Acceptance Criteria**:
- A student can create a course with a required name and can later edit its name.
- The dashboard lists all courses belonging to the signed-in student.
- Course names cannot be submitted as empty values.

**Priority**: MVP

### User Story 3 — Record Assignments and Exams
As a university student, I want to add assignments and exams to a course so that I can keep track of what I need to complete.

**Acceptance Criteria**:
- A student can add a task with a title, course, type (assignment or exam), due date, and estimated effort.
- The student can edit task details and mark a task as complete.
- A task remains associated with its selected course after saving.

**Priority**: MVP

### User Story 4 — View Upcoming Deadlines
As a university student, I want to see my upcoming deadlines in one dashboard so that I can prioritize urgent coursework.

**Acceptance Criteria**:
- The dashboard shows incomplete tasks ordered by due date, with the earliest deadline first.
- Each listed task displays its course, title, and due date.
- Completed tasks do not appear in the default upcoming-deadlines list.

**Priority**: MVP

### User Story 5 — Set Study Availability
As a working student, I want to define the hours when I am available to study so that my plan fits around work and classes.

**Acceptance Criteria**:
- The student can add and edit available time windows for each day of the week.
- A time window cannot be saved if its end time is not later than its start time.
- Saved availability is used when generating a weekly study plan.

**Priority**: MVP

### User Story 6 — Generate a Weekly Study Plan
As a university student, I want an AI-assisted weekly study plan based on my deadlines, estimated effort, and available hours so that I can distribute my workload realistically.

**Acceptance Criteria**:
- The student can request a plan for a selected week using their saved tasks and availability.
- Every proposed study session is associated with a task or course and falls within an available time window.
- The proposed plan contains no overlapping sessions and is shown for review before it is saved.

**Priority**: MVP

### User Story 7 — Review and Edit a Proposed Plan
As a university student, I want to adjust an AI-generated plan before confirming it so that I remain in control of my schedule.

**Acceptance Criteria**:
- The student can change the start time or duration of a proposed session before saving the plan.
- The application warns when an edited session conflicts with another session or falls outside saved availability.
- The student can confirm the edited plan or discard the proposal without changing the previously saved plan.

**Priority**: MVP

### User Story 8 — Explain Scheduling Recommendations
As a university student, I want to see why a task was scheduled or prioritized so that I can understand and trust the suggested plan.

**Acceptance Criteria**:
- Each proposed study session displays a brief explanation referencing relevant factors, such as deadline proximity, priority, or estimated effort.
- Explanations correspond to the task data used for the current plan.
- The student can still edit or reject a suggested session after viewing its explanation.

**Priority**: High

### User Story 9 — Reschedule Delayed Work
As a university student, I want to request an updated plan when I fall behind so that remaining tasks can be reorganized without losing my progress.

**Acceptance Criteria**:
- After a student marks a scheduled session as skipped or a task as delayed, they can request a revised plan.
- The revision proposes new session times using current tasks and availability without changing task due dates.
- Existing saved plans remain unchanged until the student approves the revision.

**Priority**: High

### User Story 10 — Track Study Sessions
As a university student, I want to record completed study sessions and actual time spent so that I can understand my study habits.

**Acceptance Criteria**:
- A student can mark a planned session complete and enter the actual number of minutes studied.
- The application displays planned versus actual study minutes for the selected week.
- Recorded time remains linked to the correct course or task.

**Priority**: Medium

### User Story 11 — Organize Study Materials
As a university student, I want to save resource links and notes under courses or tasks so that I can find relevant study materials quickly.

**Acceptance Criteria**:
- A student can attach a text note or a valid web link to a course or task.
- Saved materials appear when the student opens the related course or task.
- Notes and links are accessible only to their owner unless the owner explicitly shares them.

**Priority**: Medium

### User Story 12 — Share Selected Group Milestones
As a study-group member, I want to share specific project milestones with invited classmates so that we can coordinate group work without exposing our private schedules.

**Acceptance Criteria**:
- A student can invite another registered user to view a specifically selected group-project milestone.
- An invited collaborator can see only the milestones shared with them, not the owner's private tasks, notes, or complete calendar.
- The owner can revoke access, after which the collaborator can no longer view the shared milestone.

**Priority**: Low
