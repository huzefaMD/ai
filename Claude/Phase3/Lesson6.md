#  Lesson 6 - `Claude Projects and Memory`

## PART 1: Understanding Claude's Memory System

### How Claude Memory Works

**LEVEL 1:** IN-CONVERSATION MEMORY

Claude remembers everything
within one conversation.
Resets when you start a new chat.
Always available - no setup needed.

**LEVEL 2:** CLAUDE PROJECTS

You create a "Project" with
permanent context and instructions.
Claude remembers your setup
across ALL conversations in that project.
Available on Claude.ai Pro.

**LEVEL 3:** CLAUDE MEMORY FEATURE

Claude automatically saves facts
about you from conversations.
Builds a personal memory over time.
Available on Claude.ai (can be enabled).

## The Memory Hierarchy
## The Memory Hierarchy

|  |  | |
|---------|-------------|-------|
| **CLAUDE PROJECTS**|  Your business context lives here across all chats | ` ← Permanent, structured context you control` |
| **CLAUDE MEMORY** | Facts Claude learns about you automatically |` ← Auto-saved facts from conversations` |
| **IN-CONVERSATION** | Everything in current chat |` ← Temporary, resets each new chat` |

## PART 2: Claude Projects - Deep Dive

### What is a Claude Project?

A Project is a dedicated workspace in Claude that contains:

**1. SYSTEM PROMPT (Instructions)**
- Permanent instructions for how
Claude should behave in this project
- Your business context
- Your preferences and style

**2. PROJECT FILES (Knowledge Base)**
- Documents you upload
- SOPs, templates, course content
- Student data, pricing, FAQs

**3. CONVERSATION HISTORY**
- All chats within the project
- Searchable and organized
- Claude learns from previous chats

## Why Projects are Powerful

| Without Projects | With Projects |
|------------------|---------------|
| Repeat context every chat | Context always loaded |
| Generic responses | Responses tailored to HuzefAI |
| Start from scratch daily | Builds on previous work |
| One context for everything | Different contexts per purpose |
| No file reference | Files always available |

## PART 3: Setting Up Your HuzefAI Project

### Step by Step Setup

STEP 1:` Go to claude.ai`

STEP 2: `Click "Projects" in left sidebar`

STEP 3: `Click "New Project"`

STEP 4:` Name it "HuzefAI - Main"`

STEP 5: `Add your System Prompt
(we'll build this below)`

STEP 6: `Upload relevant files`

STEP 7:` Start chatting - Claude now
knows your business!`

## PART 4: The Perfec
This is the most important setup step. Your system prompt tells Claude exactly who it is,
what it knows, and how to behave in every conversation.

### Building HuzefAI's Master System Prompt
Here's how to create it using Claude itself:
```
<task>
Help me create a perfect system prompt
for a Claude Project dedicated to
running HuzefAI efficiently.

This system prompt should make Claude
act as my dedicated business assistant
who knows everything about HuzefAI.
</task>

<include>
1. Who I am and what HuzefAI is
2. Our courses, pricing, and target students
3. My communication style and preferences
4. How Claude should respond to me
5. What Claude should always remember
6. What Claude should never do
7. How to handle different types of requests
</include>
```
## PART 5: Managing Multiple Projects

### The HuzefAI Project System

DAILY WORKFLOW:

Morning > Open "HuzefAI Main" project
Quick decisions, emails, planning

Content day > Open "Content Creation" project
LinkedIn posts, webinar content

Course work > Open "Course Development" project
Curriculum, labs, exercises

Student queries > Open "Student Support" project
Quick answers, troubleshooting

Personal > Open "Personal Growth" project
Strategy, learning, reflection

## PART 6: Memory Best Practices

### Building Claude's Memory Over Time
The more you use Claude Projects consistently, the more useful it becomes. Here's how to
maximize it:

### Practice 1-Weekly Context Update
Once a week, update your system prompt with new information:

"Update my system prompt to add:
- We now have [X] students (up from [Y])
- New course launched: [name] at [price]
- Key win this week: [achievement]
- Current challenge: [problem]
- Next goal: [target]"
