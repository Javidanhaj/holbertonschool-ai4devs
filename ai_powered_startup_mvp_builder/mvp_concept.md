# MVP Concept — StudyFlow AI

## Problem Statement
University students often manage assignments, exams, and study sessions across scattered calendars, notes, and messaging apps. This makes it easy to miss deadlines or spend too much time deciding what to study next. StudyFlow AI is a lightweight web application that brings academic tasks into one place and proposes a realistic weekly study plan based on deadlines and the time a student has available.

## Target Users
- **University students:** Need a simple way to organize courses, prioritize assignments, and plan study time.
- **Students balancing work and study:** Need schedules that fit limited availability and can be adjusted quickly.
- **First-year students:** Need clear reminders and an overview of upcoming academic commitments.

## Core Features
1. **Course and task management:** Create, edit, complete, and delete courses and assignments; record due dates and estimated study time.
2. **Weekly study planner:** Enter available study hours and generate a suggested study schedule based on upcoming deadlines and task estimates.
3. **Editable schedule:** Move or reschedule suggested sessions manually without losing the underlying tasks.
4. **Deadline dashboard:** View upcoming assignments, due dates, and overdue items in one place.
5. **Progress tracking:** Mark study sessions and assignments as complete and view a simple weekly completion summary.

## Constraints
- **MVP scope:** A responsive web app for individual students; no native mobile apps or collaboration features in the initial release.
- **Authentication:** Basic email-and-password login; each student can access only their own courses, assignments, and schedule.
- **AI reliability:** AI-generated schedules are suggestions, not guarantees; students can review and edit them. A rules-based schedule is an acceptable fallback if the AI service is unavailable.
- **Budget:** Use free-tier or low-cost hosting and database services for an initial pilot. Any AI API usage must remain within configured spending limits.
- **Data collection:** Store only account information and study-planning data needed for the MVP; never request passwords or private university credentials.
- **Integrations:** No university learning-management-system sync, calendar sync, push notifications, or payment system in version 1.
- **Validation:** Require valid task titles and deadlines; provide clear error messages and prevent users from accessing other users' records.

## MVP Success Criteria
- A student can add a course and assignment, generate a weekly plan, edit a session, and mark work complete.
- The same account can return later and see previously saved tasks and schedule.
- The interface remains usable on common desktop and mobile screen sizes.
