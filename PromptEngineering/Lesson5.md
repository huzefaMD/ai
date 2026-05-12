# Lesson 5

## Basic XML Tag Structure

```
<context>
Who you are and background information
</context>

<task>
Exactly what you want Claude to do
</task>

<format>
How you want the output structured
</format>

<tone>
The style and voice to use
</tone>

<example>
A sample of what good output looks like
</example>
```
###  Without Tags vs With Tags

**Without XML Tags:**

```
I run HuzefAI an online training company in Chennai
teaching Cloud DevOps and AI. Write me a landing page
headline. Make it punchy and exciting. Something like
"Launch your cloud career in 6 weeks." For IT
professionals and freshers. Keep it under 10 words.
```

Claude has to figure out what's context,what's the task,
what's the example, and what's the constraint. It might mix them up. 

## With XML Tags:

```
<context>
I run HuzefAI, an online training company in Chennai
teaching Cloud, DevOps, and AI courses to IT
professionals and freshers.
</context>

<task>
Write 5 landing page headlines for HuzefAI's
AWS course.
</task>

<format>
- Each headline under 10 words
- Numbered list
- No punctuation at the end
</format>

<tone>
Punchy, exciting, aspirational - speaks to
career growth
</tone>

<example>
Good headline style: "Launch Your Cloud Career in 6 Weeks"
</example>
```
Claude now knows exactly what each part me---
Output will be precise every time.
