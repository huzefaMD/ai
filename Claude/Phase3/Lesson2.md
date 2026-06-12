# Lesson 2:`Research & Analysis`

## Why This is a Game-Changer

### Before Claude, research meant:

Google search > Read 10 articles > Take notes
> Cross-reference > Synthesize > Form opinion
> 3-4 hours minimum

### With Claude, it means:

Ask the right question > Get synthesized,
relevant, actionable insight
> 10-15 minutes

## What We'll Cover

Part 1: Research Techniques
Part 2: Competitive Analysis
Part 3: Market Research
Part 4: Data Analysis
Part 5: Learning Any Topic Fast

## PART 1: Research Techniques

### The 4 Research Modes

MODE 1: EXPLAIN IT TO ME
Understanding a new topic fast

MODE 2: COMPARE FOR ME
Evaluating options side by side

MODE 3: ANALYZE THIS FOR ME
Making sense of data or content

MODE 4: FIND GAPS FOR ME
Spotting opportunities others miss

## Mode 1 - Explain It To Me
### Best for: Learning something new quickly
```
<role>
You are an expert in [topic] who specializes
in teaching complex concepts simply.
</role>

<task>
Explain [topic] to me as if I'm a smart
professional but complete beginner
in this specific area.
</task>

<format>
1. What it is (simple definition)
2. Why it matters (real-world impact)
3. How it works (simple explanation)
4. Real example I can relate to
5. What I should know next
</format>

<dont>
- No jargon without explanation
- No academic language
- Don't overwhelm with details
</dont>
```
## Real Example for Huzefa:
```
<role>
Expert in EdTech business models who
teaches founders simply.
</role>

<task>
Explain the cohort-based course model
vs self-paced course model. I run
HuzefAI and need to decide which
works better for my Cloud/DevOps/AI courses.
</task>

<format>
1. How each model works
2. Revenue comparison
3. Student experience comparison
4. Operational complexity comparison
5. Which is better for HuzefAI right now and why
</format>
```
## Mode 2- Compare For Me
### Best for: Making decisions between options
```
<task>
Compare [Option A] vs [Option B] vs [Option C]

Evaluate each on these criteria:
1. [Criterion 1]
2. [Criterion 2]
3. [Criterion 3]
4. [Criterion 4]

Present as a comparison table.
End with a clear recommendation
for my specific situation: [context]
</task>
```
## Real Example for Huzefa:
```
<task>
Compare these 3 platforms for hosting
HuzefAI's online courses:
- Teachable
- Thinkific
- Building our own on WordPress

Evaluate on:
1. Cost for 500 students
2. Features for live + recorded content
3. Payment gateway options for India
4. Student experience quality
5. Customization flexibility

Present as a table.
Recommend the best for a Chennai-based
EdTech startup at early growth stage.
</task>
```
## Mode 3- Analyze This For Me
### Best for: Making sense of content, feedback, or data you already have
```
<task>
Analyze this [content/data/feedback] and tell me:
1. Key patterns you notice
2. What's working well
3. What's not working
4. Hidden insights I might be missing
5. Top 3 actionable recommendations
</task>

<data>
[paste your content here]
</data>
```
## Real Example for Huzefa:
```
<task>
Analyze these student reviews from
HuzefAI's last AWS batch and tell me:

1. Most common praise (top 3 themes)
2. Most common complaints (top 3 themes)
3. Sentiment score overall (1-10)
4. Any surprising or unexpected feedback
5. Top 3 changes to make for next batch
</task>

<data>
[paste 20-30 student reviews here]
</data>
```
## Mode 4- Find Gaps For Me
### Best for: Spotting opportunities competitors are missing
```
<task>
Analyze the [market/industry/niche] and:
1. Identify underserved needs
2. Spot gaps competitors aren't filling
3. Find emerging trends nobody is teaching yet
4. Suggest 3 opportunities HuzefAI could own
</task>

<context>
HuzefAI teaches Cloud, DevOps, AI in Chennai.
Target: IT professionals and freshers.
Current gap we see: [describe what you notice]
</context>
```
## PART 2: Competitive Analysis
Understanding your competition is critical for HuzefAI. Claude makes this fast and
structured.

### The HuzefAI Competitor Analysis Template
```
<role>
You are a business strategist specializing
in EdTech market analysis in India.
</role>

<task>
Analyze the competitive landscape for
online Cloud, DevOps, and AI training
in India. Focus on:

1. MAJOR PLAYERS
- Who are the top 5 competitors?
- What do they offer?
- How are they positioned?

2. PRICING LANDSCAPE
- What price ranges exist?

2. PRICING LANDSCAPE
- What price ranges exist?
- Where are the gaps?
- What does premium vs budget look like?

3. CONTENT GAPS
- What topics are overcrowded?
- What's underserved?
- What emerging topics nobody covers well?

4. AUDIENCE GAPS
- Who is everyone targeting?
- Who is being ignored?

5. HUZEFAI'S OPPORTUNITY
- Where can we win?
- What's our unfair advantage?
- What position should we own?
</task>

<context>
HuzefAI is Chennai-based, teaches Cloud/
DevOps/AI, currently 50 students,
</task>

<context>
HuzefAI is Chennai-based, teaches Cloud/
DevOps/AI, currently 50 students,
founder-led, focuses on practical
hands-on training.
</context>

<format>
Section by section with clear headers.
End with a positioning statement
HuzefAI should own in the market.
</format>
```
## PART 3: Market Research

### Research Any Market in Minutes
```
<role>
Market research analyst specializing
in Indian tech education sector.
</role>

<task>
Give me a complete market research
report on [specific topic].
</task>

<format>
1. Market size and growth rate
2. Target customer profile
3. Key buying triggers
4. Key objections to buying
5. Price sensitivity analysis
6. Best marketing channels to reach them
7. Seasonal trends if any
8. Bottom line opportunity assessment
</format>
```
## Real HuzefAI Examples:

### Research 1: Your Target Student
```
<task>
Build a detailed profile of HuzefAI's
ideal student - a Chennai IT professional
looking to upskill in Cloud and AI.

Include:
1. Demographics (age, income, education)
2. Current job situation and pain points
3. Career goals and fears
4. What they search for online
5. Where they spend time online
6. What makes them buy a course
7. What makes them hesitate
8. Their dream outcome from training
</task>
```
### Research 2: Pricing Research
```
<task>
Research and analyze course pricing
for Cloud, DevOps, and AI training in India.

Cover:
1. What platforms charge (Udemy, Coursera,
local bootcamps)
2. Price points that convert best
3. What justifies premium pricing
4. Psychological pricing strategies
that work in Indian EdTech
5. Recommended pricing ladder for HuzefAI
</task>
```
### Research 3: Trend Research
```
<task>
What are the top 5 emerging technology
trends in 2026 that Chennai IT professionals
should be learning right now?

For each trend tell me:
1. What it is
2. Why it matters for Indian IT market
3. Job market demand for this skill
4. How hard it is to learn
5. Should HuzefAI build a course on this?
</task>
```
## PART 4: Data Analysis
Claude can analyze data you paste directly - no Excel formulas needed.

### Simple Data Analysis
```
<task>
Analyze this data and give me insights:

[paste your data as text or table]

Tell me:
1. Key trends you notice
2. Best performing item and why
3. Worst performing item and why
4. Surprising patterns
5. What I should do based on this data
</task>
```
## PART 5: Learning Any Topic Fast
This is one of the most powerful uses of Claude - becoming a quick expert on any topic
you need for HuzefAI.

### The Fast Learning Framework
```
<role>
You are a world-class teacher in [topic]
who specializes in rapid skill transfer.
</role>

<task>
Teach me [topic] using the 80/20 principle.
I need to understand the 20% of knowledge
that gives me 80% of practical value.

I am: [describe your background]
My goal: [what you need this knowledge for]
Time available: [how quickly you need to learn]
</task>

<format>
1. The core concept in one paragraph
2. The 5 most important things to know
3. Common misconceptions to avoid
4. 3 practical applications immediately
5. What to learn next if I want to go deeper
</format>
```
## Rapid Learning Examples for Huzefa

### Learn: Google Cloud (to teach it)
```
<role>
Senior Google Cloud architect and educator.
</role>

<task>
I currently teach AWS at HuzefAI.
I want to add Google Cloud to my curriculum.

Teach me the key differences between
AWS and GCP so I can:
1. Explain GCP to my AWS-familiar students
2. Know which GCP services map to which AWS services
3. Understand where GCP is stronger than AWS
4. Build a 4-week GCP course outline
</task>
```
## Learn: Business Finance (to run HuzefAI better)
```
<role>
CFO mentor who helps startup founders
understand their numbers simply.
</role>

<task>
I'm a technical founder running HuzefAI.
Teach me the 5 most important financial
metrics I must track monthly to know
if my EdTech business is healthy.

Explain each metric:
- What it is (simple definition)
- How to calculate it
- What good looks like for EdTech
- What to do if mine is bad
</task>
```
## Learn: SEO (to grow HuzefAI online)
```
<role>
SEO specialist who has grown EdTech
websites in India from 0 to 100K visitors.
</role>

<task>
Teach me the minimum SEO I need to know
to rank HuzefAI's website for terms like
"cloud course Chennai" and
"DevOps training India."

Focus on:
1. What actually moves the needle in 2026
2. What I can do myself without hiring anyone
3. Quick wins in first 30 days
4. Mistakes to avoid
</task>
```
