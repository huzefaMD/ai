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
## Without Tags vs With Tags

*X Without XML Tags:*
```
I run HuzefAI an online training company in Chennai
teaching Cloud DevOps and AI. Write me a landing page
headline. Make it punchy and exciting. Something like
"Launch your cloud career in 6 weeks." For IT
professionals and freshers. Keep it under 10 words.
```

Claude has to figure out what's context, what's the task, what's the example, and what's the
constraint. It might mix them up.

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
Claude now knows exactly what each part me*** Output will be precise every time.

## Most Useful XML Tags for You

| Tag | What It's For |
|------|--------------|
| `<context>` | Background info, who you are |
| `<task>` | What you want Claude to do |
| `<format>` | How to structure the output |
| `<tone>` | Style and voice |
| `<example>` | Sample of good output |
| `<rules>` | Constraints and limitations |
| `<data>` | Raw data for analysis |
| `<question>` | The specific question to answer |
| `<goal>` | The end objective |
| `<audience>` | Who the output is for |
| `<steps>` | Step-by-step instructions |
| `<output>` | Expected final output |
| `<constraints>` | Additional restrictions |
| `<references>` | Supporting resources or links |
| `<persona>` | Role the AI should act as |
| `<success_criteria>` | What defines a successful answer |

## Email Campaign:
```
<context>
HuzefAI is a Chennai-based online training company
teaching Cloud, DevOps, and AI. We just launched
a new Generative AI course priced at t9,999.
</context>

<audience>
IT professionals aged 25-35 who attended our
free webinar but haven't enrolled yet.
</audience>

<task>
Write a launch email for our new Generative AI course.
</task>

<format>
- Subject line
- Opening hook (2 sentences)
- Course benefits (3 bullet points)
- Social proof (1 sentence)
- Call to action
- Sign off as Huzefa, Founder HuzefAI
</format>

<tone>
Warm, personal, excited - like a founder
personally writing to a student
</tone>

<rules>
- No corporate jargon
- No more than 200 words total
- Must mention Chennai IT market opportunity
</rules>
```
## Data Analysis:
```
<context>
HuzefAI ran 3 courses last quarter.
</context>

<data>
Course 1: AWS Fundamentals - 45 students - ₹4,999 -
4.8 rating - 85% completion
Course 2: DevOps Bootcamp - 28 students - ₹7,999 -
4.6 rating - 72% completion
Course 3: Python for AI - 61 students - ₹3,999 -
4.9 rating - 91% completion
</data>

<task>
Analyze this data and give me business insights.
</task>

<format>
1. Best performing course and why
2. Biggest opportunity I'm missing
3. Pricing insights
4. Top 3 recommendations for next quarter
</format>

<tone>
Direct, data-driven, no fluff
</tone>
```
