# SecureCTF
*Development Period: April 2023 - July 15, 2023*

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

1. Clone the repository:
   ```bash
   git clone https://github.com/1samyool/TM470SecureCTF.git
   cd TM470SecureCTF
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Access the application at `http://localhost:8080`


## Development Timeline

### Week 1 (1–7 April)
**What I did:**
- Finalized project proposal with clear scope, objectives, and MoSCoW prioritization.
- Created risk register and mitigation plans.
- Defined MVP and non-MVP features.
- Addressed initial legal/ethical concerns.

**What went well:**
- Strong start to planning phase. Tutor feedback on proposal was largely positive, indicating good alignment with module expectations.

**What didn’t go well:**
- Struggled initially to distinguish between MVP and stretch goals until after reviewing past EMA exemplars.

**What I’ll do next week:**
- Start coding backend core functionality, focusing on challenge initiation and flag submission.
---
### Week 2 (8–14 April)
**What I did:**
- Implemented `/start-challenge`, `/submit-flag`, and `/leaderboard` endpoints.
- Set up JSON-based storage and basic validation.

**What went well:**
- Backend work came together quickly, with FastAPI proving very efficient.

**What didn’t go well:**
- Faced issues with CORS until I discovered I hadn’t correctly set headers in FastAPI config.

**What I’ll do next week:**
- Begin frontend development to interact with backend APIs.
---
### Week 3 (15–21 April)
**What I did:**
- Developed core frontend with challenge list, username entry, and leaderboard view.
- Configured CORS correctly and Dockerized the first challenge.

**What went well:**
- Successful API integration and functional UI prototype.

**What didn’t go well:**
- Docker setup was new territory; required significant debugging.

**What I’ll do next week:**
- Add admin endpoint and begin backend security improvements.
---
### Week 4 (22–28 April)
**What I did:**
- Added admin reset endpoint.
- Hardened backend security and used Swagger UI for documentation.

**What went well:**
- Swagger UI provided a professional touch and made testing easier.

**What didn’t go well:**
- Discovered leaderboard was vulnerable to tampering due to missing validation step; fixed it.

**What I’ll do next week:**
- Begin refactoring and review codebase structure.
---
### Week 5 (29 April–5 May)
**What I did:**
- Modularized backend code for maintainability.
- Reorganized GitHub issues and verified all endpoint functionality.

**What went well:**
- Code quality and traceability significantly improved.

**What didn’t go well:**
- Realized some of my early Git commits lacked descriptive messages, which made tracking harder.

**What I’ll do next week:**
- Start frontend enhancements and form-based flag submission.
---
### Week 6 (6–12 May)
**What I did:**
- Refactored backend validation logic.
- Started frontend design for improved UX (e.g. navigation, inputs).

**What went well:**
- Refactored functions now easier to test and reuse.

**What didn’t go well:**
- I overcomplicated form handling before simplifying it using controlled components in React.

**What I’ll do next week:**
- Finish and test updated frontend workflows.
---
### Week 7 (13–19 May)
**What I did:**
- Implemented frontend flag submission form and improved challenge navigation.
- Developed `/challenges/{id}` endpoint for dynamic challenge details.

**What went well:**
- Seamless integration between frontend and new endpoint.

**What didn’t go well:**
- Small bug in challenge ID parsing delayed UI testing.

**What I’ll do next week:**
- Final polish of current features and prepare for documentation.
---
### Week 8 (20–27 May)
**What I did:**
- Conducted final review and updated documentation.
- Compiled logs, test evidence, and milestone status for TMA02.

**What went well:**
- Documentation is clean and traceable to GitHub history.

**What didn’t go well:**
- Slight time crunch in compiling screenshots and evidence.

**What I’ll do next:**
- Submit TMA02 and shift focus to challenge enhancements and user feedback cycle in TMA03.

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
- **Flag Format**: CTF{C00k13_M0nst3r}

### Level 2: Cryptography
- **Difficulty**: Medium
- **Topic**: Basic Cryptography
- **Skills Learned**: Base64 Encoding, Character Shifting
- **Flag Format**: CTF{R0T_M4st3r_2023}

### Level 3: SQL Injection
- **Difficulty**: Hard
- **Topic**: Database Security
- **Skills Learned**: SQL Injection, UNION Attacks
- **Flag Format**: CTF{SQL_M4st3r_2023}

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
