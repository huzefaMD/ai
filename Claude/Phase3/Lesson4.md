# Lesson 4 : `Coding help and Debugging`

## The Code Generation Template
```
<task>
Write [language] code that does [specific function].
</task>

<requirements>
- Requirement 1
- Requirement 2
- Requirement 3
</requirements>

<context>
This code will be used for [purpose].
My technical level is [beginner/intermediate/expert].
</context>

<format>
- Add comments explaining each section
- Keep it simple and readable
- Include example usage at the end
</format>

<dont>
- Don't use complex libraries unless necessary
- Don't assume I know advanced concepts
</dont>
```
## Example 1 - Student Registration Form
```
<task>
Write HTML and CSS code for a
student registration form for HuzefAI.
</task>

<requirements>
- Fields: Full name, Email, Phone number,
Current job role, Course interested in
(dropdown: AWS, DevOps, AI, Generative AI),
How did you hear about us
- Submit button in HuzefAI brand colors
- Mobile responsive design
- Simple clean professional look
</requirements>

<context>
This will be embedded in our WordPress website.
I have basic HTML knowledge.
</context>

<format>
- Complete HTML file with CSS included
- Comments explaining each section
- No external libraries - pure HTML/CSS only
</format>
```
## Exampie 2 - Student Data Tracker
```
<task>
Write a Python script that reads a CSV
file of student data and produces a
simple report.
</task>

<requirements>
- Read CSV with columns: Name, Course,
Enrollment Date, Completion Status, Rating
- Calculate: Total students per course,
Average rating per course,
Completion rate per course
- Print a clean formatted report
- Save report as a text file
</requirements>

<context>
I am not a Python expert.
I just need this to work simply.
Running on Windows laptop.
</context>

<format>
- Simple readable code
- Comments on every section
- Show me how to run it
- Include sample CSV data to test with
</format>
```
## PART 2: Code Explanation
Claude is the best code teacher in the world - it explains any code at exactly your level.

### The Explanation Template
```
<task>
Explain this code to me.
</task>

<my_level>
[Complete beginner / Know basics / Intermediate]
</my_level>

<what_i_need>
1. What does this code do overall?
2. Explain each section line by line
3. What would happen if I changed [X]?
4. Are there any problems with this code?
5. How would I modify it to also do [Y]?
</what_i_need>

<code>
[paste your code here]
</code>
```
### Levels of Explanation For Complete Beginners:
```
"Explain this code as if I'm a
10-year-old who has never seen
code before. Use simple analogies
and everyday examples."
```
### For Basic Knowledge:
```
"Explain this code clearly. I know
basic programming concepts but
I'm not familiar with this language."
```
### For Teaching Students:
```
"Explain this code in a way that
would be perfect for teaching
IT freshers in a DevOps course.
Include the WHY behind each decision."
```
## Explain Any Technology
Not just code - Claude explains ANY technical concept for your HuzefAI courses:
```
<task>
Explain [technical concept] for my
HuzefAI course students.

My students are: [describe their level]

Explain using:
1. Simple definition (1 sentence)
2. Real world analogy
3. How it works technically
4. Hands-on example they can try
5. Common mistakes beginners make
6. How this connects to what they
already know
</task>
```
### Examples:

- Explain Docker containers
- Explain Kubernetes orchestration
- Explain AWS IAM roles
- Explain CI/CD pipelines
- Explain REST APIS
- Explain Git branching
  
## PART 3: Debugging & Error Fixing
This is where Claude saves the most time. Debugging can take hours - Claude often solves
it in seconds.

### The Debug Template
```
<task>
Help me fix this error in my code.
</task>

<error_message>
[paste the exact error message]
</error_message>

<code>
[paste your complete code]
</code>

<context>
- Language: [Python/JavaScript/etc]
- What I'm trying to do: [explain]
- What I've already tried: [list attempts]
- When the error occurs: [describe]
</context>

<what_i_need>
1. What is causing this error?
2. Fix the code
3. Explain WHY it was wrong
4. How do I avoid this mistake in future?
</what_i_need>
```
## Common Error Types Claude Fixes Instantly

| Error Type | Example | Claude's Fix Rate |
|------------|---------|-------------------|
| Syntax errors | Missing bracket, wrong indentation | ⭐⭐⭐⭐⭐ Instant |
| Logic errors | Wrong output, infinite loop | ⭐⭐⭐⭐⭐ Very fast |
| Import errors | Module not found | ⭐⭐⭐⭐⭐ Instant |
| API errors | Authentication, wrong endpoint | ⭐⭐⭐⭐ Fast |
| Database errors | Wrong query, connection issues | ⭐⭐⭐⭐ Fast |
| CSS layout issues | Broken responsive design | ⭐⭐⭐⭐ Fast |

## Real Debug Example
### Student brings this error to Huzefa:

Error: ModuleNotFoundError:
No module named 'pandas'

Code:
import pandas as pd
df = pd.read_csv('students.csv')
print(df.head())

### Prompt to Claude:
```
<task>Fix this Python error</task>

<error_message>
ModuleNotFoundError: No module named 'pandas'
</error_message>

<code>
import pandas as pd
df = pd.read_csv('students.csv')
print(df.head())
</code>

<context>
Running on Windows. Using Python 3.10.
Never installed any packages before.
</context>

<what_i_need>
1. Why is this happening?
2. Exact commands to fix it
3. How to verify it's fixed
4. Explain what pandas is while you're at it
</what_i_need>
```
## PART 4: Code Review & Improvement
Claude reviews code like a senior developer - catching problems before they cause issues.

### The Code Review Template
```
<role>
You are a senior software engineer
with 10 years experience doing
thorough code reviews.
</role>

<task>
Review this code and give me:
1. Overall quality assessment (1-10)
2. Security vulnerabilities if any
3. Performance issues if any
4. Best practices being violated
5. Specific improvements with

3. Performance issues if any
4. Best practices being violated
5. Specific improvements with
corrected code
6. What's actually done well
</task>

<code>

[paste your code]
</code>

<context>
This code is for: [purpose]
Will be used by: [number] users
My experience level: [beginner/intermediate]
</context>
```
### Code Improvement Requests

### Make it faster:
```
"This code works but is slow when
processing 1000+ records.
Optimize it for performance."
```
### Make it simpler:
```
"This code works but is too complex.
Rewrite it to be simpler and more
readable for a junior developer."
```
### Make it more secure:
```
"Review this code for security
vulnerabilities. Fix any issues
you find."
```
### Add error handling:
```
"Add proper error handling to this code.
It currently crashes when something
goes wrong."
```
## PART 5: Real HuzefAI Coding Projects
Here are 5 real projects Claude can build for HuzefAI right now:

### Project 1- Student Progress Dashboard
```
<task>
Build a simple HTML dashboard that
shows HuzefAI student progress.
</task>

<requirements>
- Display: Total students, Active courses,
Completion rates, Average ratings
- Simple cards layout
- HuzefAI color scheme (blue and white)
- Data hardcoded for now (I'll connect
real data later)
- Mobile responsive
</requirements>

<format>
Single HTML file with CSS and
JavaScript included.
No external dependencies.
</format>
```
## PART 5: Real HuzefAI Coding Projects
Here are 5 real projects Claude can build for HuzefAI right now:

### Project 1 - Student Progress Dashboard
```
<task>
Build a simple HTML dashboard that
shows HuzefAI student progress.
</task>

<requirements>
- Display: Total students, Active courses,
Completion rates, Average ratings
- Simple cards layout
- HuzefAI color scheme (blue and white)
- Data hardcoded for now (I'll connect
real data later)
- Mobile responsive
</requirements>

<format>
Single HTML file with CSS and
JavaScript included.
No external dependencies.
</format>
```
### Project 2- Course Waitlist System
```
<task>
Create a simple Python script for
managing HuzefAI course waitlists.
</task>

<requirements>
- Add student to waitlist (name, email,
phone, course interested in)
- View all students on waitlist
- Remove student when they enroll
- Export waitlist to CSV
- Simple command line interface
</requirements>

<format>
Complete Python script.
Save data to a JSON file.
Comments on every function.
</format>
```
### Project 3- Automated Certificate Generator
```
<task>
Write a Python script that generates
completion certificates for HuzefAI students.
</task>

<requirements>
- Read student names from CSV file
- Generate PDF certificate for each student
- Certificate includes: Student name,
Course name, Completion date,
HuzefAI branding
- Save each certificate as
"StudentName_CourseName_Certificate.pdf"
</requirements>

<format>
Complete script with setup instructions.
Use only free Python libraries.
</format>
```
### Project 4- Email Newsletter Script
```
<task>
Write a Python script to send
weekly newsletter emails to
HuzefAI students.
</task>

<requirements>
- Read student emails from CSV
- Send HTML formatted email
- Email includes: Weekly tip,
Upcoming batch announcement,
Student success story placeholder
- Use Gmail SMTP (free)
- Log sent emails
- Handle failed sends gracefully
</requirements>

<format>
Complete script with:
- Setup instructions
- Gmail configuration guide
- HTML email template
- Main sending script
</format>
```
### Project 5-HuzefAI Chatbot
```
<task>
Build a simple FAQ chatbot for
HuzefAI's website using HTML,
CSS, and JavaScript.
</task>

<requirements>
- Chat bubble in bottom right corner
- Answers these questions:
* Course fees and details
* Batch timings
* How to enroll
* About Huzefa
* Contact information
- Friendly responses in HuzefAI voice
- If unknown question: show contact details
- Mobile responsive
</requirements>

<format>
Single HTML file - ready to embed
in any website.
No external APIs needed.
Completely free to use.
</format>
```
## 💡 Pro Tips for Coding with Claude

| Tip | Why It Matters |
|------|---------------|
| Always paste exact error messages | Claude diagnoses instantly with full error text |
| Mention your skill level | Claude adjusts explanation complexity |
| Ask for comments in code | Makes code understandable and teachable |
| Request setup instructions | Claude explains how to run the code too |
| Ask "what could go wrong?" | Claude identifies edge cases proactively |
| Iterate step by step | Build complex projects in small pieces |
| Ask for alternatives | "Show me 3 different ways to do this" |
