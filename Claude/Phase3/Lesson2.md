# Lesson 2

# `Research & Analysis`

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
