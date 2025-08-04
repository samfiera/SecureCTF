# SecureCTF - Created by: Sam Fiera
*Development Period: March - September 2025

A three-level Capture The Flag (CTF) web application designed to teach fundamental web security concepts through hands-on challenges. This project was developed over several months to create an engaging, educational platform for learning about web security vulnerabilities.

## Features

- **Three Progressive Difficulty Levels:**
  1. Cookie Monster (Basic Cookie Manipulation)
  2. Cryptography Challenge (Base64 + ROT Cipher)
  3. SQL Injection Challenge (Advanced Database Attacks)

- **User Management:**
  - Personal username tracking
  - Session management
  - Progress tracking

- **Leaderboard System:**
  - Real-time completion tracking
  - Time-based scoring
  - Medal system (🥇, 🥈, 🥉)
 
## Installation

1. Open terminal and clone the repository:
   ```bash
   git clone https://github.com/samfiera/ctf-project.git
   cd ctf-project
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install flask flask_sqlalchemy cryptography
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Access the application at `http://localhost:(whatever port it says)`

## Technical Stack

- **Backend**: Flask 3.0.2
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3
- **Security Features**: Session Management, Cookie Handling, Custom Encryption

## Challenge Details

### Level 1: Cookie Monster
- **Difficulty**: Easy
- **Topic**: Cookie Manipulation
- **Skills Learned**: Browser DevTools, Cookie Inspection


### Level 2: Cryptography
- **Difficulty**: Medium
- **Topic**: Basic Cryptography
- **Skills Learned**: Base64 Encoding, Character Shifting


### Level 3: SQL Injection
- **Difficulty**: Hard
- **Topic**: Database Security
- **Skills Learned**: SQL Injection, UNION Attacks


## Project Structure
```
ctf-project/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── ctf.db             # SQLite database
└── templates/         # HTML templates
    ├── index.html     # Main page
    ├── login.html     # User login
    ├── level1.html    # Cookie challenge
    ├── level2.html    # Cryptography challenge
    ├── level3.html    # SQL injection challenge
    └── leaderboard.html
```

## App Structure
- Framework: Flask (Python web framework)
- Database: SQLite (a file-based database, ctf.db)
- Main File: app.py (contains all the logic and routes)
- Templates: HTML files rendered for each page (login, challenges, leaderboard, etc.)
## User Flow
- Login:
  - User visits the site.
  - If not logged in, they are redirected to the login page.
  - User enters a username (no password required for the app).
- Challenge Selection:
  - After login, user sees the main page with links to Level 1, Level 2, and Level 3.
Solving a Challenge:
  - User clicks a level (e.g., Level 1).
  - The app starts a timer for that level (records the start time in the session).
  - User solves the challenge and submits the flag via a form.
- If the flag is correct:
  - The app calculates how long it took (end time - start time).
  - The app records the attempt in the database (who, which level, how fast).
  - User sees a success message and their completion time.
- If the flag is wrong:
  - User sees an error message and can try again.
- Leaderboard:
  - User can view the leaderboard for each level.
  - The leaderboard shows the fastest users for each challenge.
- Logout:
  - User can log out, which clears their session.
    
## Development Timeline

### 🧠 Sprint Management Overview

This appendix provides selected extracts from the SecureCTF project log, tracking sprint-based development, testing, and reflective learning over time. Each sprint is approximately two weeks and structured around ScrumBan milestones described in Section 3.4. The full log is maintained in parallel with GitHub issue tracking and includes blockers, features implemented, and key insights. Peer testing and feature-based decision-making were key components of iteration.

---

### ✅ Sprint 1: March 20 – April 3

**Tasks Completed:**
- Reconfirmed project scope and MoSCoW priorities.
- Set up GitHub Projects board using ScrumBan with labeled issues.
- Started conducting a literature search.

**Challenges:**
- Originally planned React + FastAPI architecture felt too heavy for a solo, short-term project.
- Started to question value of a complex decoupled frontend.

**Reflection:**
- Tutor feedback and further research led to the decision to re-evaluate technology stack post-TMA01 and TMA02.
- Focused on foundational planning deliverables for a strong start.

---

### ✅ Sprint 2: April 4 – April 17

**Tasks Completed:**
- Finalized prioritization and drafted plan.
- Began prototyping backend using FastAPI.
- Translated MVP ideas into actual tangible tasks.

**Challenges:**
- Encountered frustrating async and CORS errors in FastAPI.
- Early peer testers found React UI too clunky to install/setup for a small CTF game.

**Reflection:**
- MVP features implemented but integration felt fragile.

---

### ✅ Sprint 3: April 18 – May 1

**Tasks Completed:**
- Implemented all endpoints in FastAPI.
- Created JSON-based storage for leaderboard and user data.

**Challenges:**
- Struggled with Pydantic validation errors in FastAPI.
- JSON storage lacked flexibility or memory for future features.

**Reflection:**
- FastAPI was fast to start but then started getting more complicated as I added more needs.

---

### ✅ Sprint 4: May 1 – May 15

**Tasks Completed:**
- Created frontend prototype with Vite.
- Integrated challenge flow with API.

**Challenges:**
- React/Vite setup slowed progress significantly; overengineered for a static app.
- Peer feedback suggested UI was usable but inconsistent.

**Reflection:**
- Framework struggles identified early; React probably not ideal for my application.

---

### ✅ Sprint 5: May 16 – May 31

**Tasks Completed:**
- Removed React; tested static HTML + Flask as a prototype.
- Built challenge 1 logic into Flask using templates and form validation.

**Challenges:**
- Flask routing simpler but required full app refactors.
- No more need for Swagger and Docker.

**Reflection:**
- Flask provided more control with less friction, promising direction for the project.

---

### ✅ Sprint 6: June 1 – June 7

**Tasks Completed:**
- Flask easing into full adoption.
- Rewrote all templates using Jinja2 (`base.html`, `level1.html`, `level2.html`).
- Set up flash messages and route-based flow.

**Challenges:**
- Manual rebuild was super time consuming.
- Needed to rethink state management and navigation.

**Reflection:**
- Dropping JSON and React removed major headaches.
- Flask+Jinja made form handling super fluid.

---

### ✅ Sprint 7: June 8 – June 14

**Tasks Completed:**
- Prepared screenshots, documentation, and evidence for TMA03.
- Wrote reflection, updated resource tables, removed obsolete tools (FastAPI, React, Docker).
- Reviewed project log entries for completeness.

**Challenges:**
- Revisiting older entries revealed gaps in detail. Some had to be rewritten from memory.

**Reflection:**
- Moving forward, commit to live weekly logs, not retroactive patches.
- Tutor feedback has reinforced the importance of structured communication and regular updates.

---

### ✅ Sprint 8: June 15 – June 29

**Tasks Completed:**
- Integrated SQLite for score tracking.
- Peer testing sent out via Google Forms.

**Challenges:**
- Feedback revealed some level 2 logic errors that needed to be fixed.

**Reflection:**
- Major milestones hit: backend, templates, and scoring now fully integrated.

---

### ✅ Sprint 9: June 30 – July 15

**Tasks Completed:**
- Final peer testing and evidence collection.
- Updated screenshots, project logs, and risk tables.
- Revised TM470 report to reflect Flask implementation.

**Challenges:**
- Tight turnaround for documentation.
- Small window to learn new frameworks.

**Reflection:**
- Major turning points this month due to framework switch.
- The app is now complete and matches scoped deliverables, waiting on more feedback to add extra features.

**Next Focus:**
- Clean up the app after TMA03 feedback for a perfect EMA!


### Sprint 10: July 16 – August 1

**Tasks Completed:**
- Conducted user interface tweaks based on preliminary tutor feedback
- Enhanced form styling and leaderboard readability for accessibility compliance
- Removed deprecated comments and unused code from Flask templates and routes
- Verified that all final EMA features were in scope per MoSCoW

**Challenges:**
- Had limited feedback from peers over the summer period

**Reflection:**
- Improvements made based on TMA03 strengthened final app quality
- Final app performance was reliable and clean, requiring no major overhauls

---

### Sprint 11: August 2 – August 30

**Tasks Completed:**
- Conducted final round of peer testing with fully functional Flask application
- Reviewed and updated all accessibility elements (color contrast, text size, button labels)
- Collected and logged final Google Forms feedback (see Appendix X)
- Archived app version and captured screenshots for additional documentation

**Challenges:**
- Final testing had to be managed alongside new SOC internship and other commitments
- Accessibility testing with real users was still limited more than I hoped for

**Reflection:**
- Peer feedback loop was a highlight: several tweaks (error messaging) directly informed by real users
- Project now considered complete from a functionality and compliance standpoint

---

### Sprint 12: September 1 – September 15

**Tasks Completed:**
- Polished EMA document: expanded Section 4.3.4 (Testing), cleaned references, scored risks, updated appendices
- Final integration of risk register, updated MoSCoW table, and project logs
- Snipped and formatted all final screenshots, diagrams, and flowcharts
- Uploaded all required evidence and zipped the final Flask app version

**Challenges:**
- Tight deadline to submit before travelling on September 16
- EMA word count and formatting constraints required focused editing and prioritization

**Reflection:**
- The final sprint felt like a full circle tying together: months of experimentation, pivoting, and iteration finally comes to an end
- Project confidence at an all-time high due to strong feedback in TMA03, working prototype, and documentation alignment




## Security Notice

This application intentionally contains vulnerabilities for educational purposes. Do not deploy it in a production environment or expose it to the public internet.

## Development Journey

This project evolved significantly over its development period:

1. **Initial Phase (April 2023)**
   - Basic application setup
   - Core routing structure

2. **User Experience (May 2023)**
   - Added user authentication
   - Switched to flask
   - Implemented session management
   - Created basic UI templates

3. **Challenge Development (June 2023)**
   - Implemented Cookie Monster challenge
   - Added cryptography challenge
   - Created leaderboard system
   - Enhanced UI/UX

4. **Final Phase (July 2023)**
   - Added SQL injection challenge
   - Improved error handling
   - Enhanced security for non-challenge components
   - Final testing and documentation

## Contributing

This project was developed as an educational tool, and while it's not actively maintained, suggestions and improvements are welcome through issues and pull requests.


## Acknowledgments

- Flask documentation and community
- Web security resources and CTF platforms that inspired this project
- Beta testers who provided valuable feedback during development

--- 
