# Lesson 7

## Without vs With Negative Prompting

### Without Negative Prompting:
```
Write a LinkedIn post about why IT professionals
in Chennai should learn cloud skills.
```
## With Negative Prompting:

```
Write a LinkedIn post about why IT professionals
in Chennai should learn cloud skills.

NEVER:
- Start with "Certainly", "Great", or any affirmation
- Use bullet points
- Use "In conclusion" or any summary phrase
- Use corporate language like "leverage" or "utilize"
- Add disclaimers
- Be preachy or lecture-y

ALWAYS:
- Start with a hook that stops the scroll
- Write like a real person talking to a friend
- End with a question that invites comments
```
### The Negative Prompting Framework
```
<avoid>
List everything Claude should NOT do
</avoid>

<never>
Hard rules that must never be broken
</never>

<tone_avoid>
Specific tones or styles to stay away from
</tone_avoid>
```

### Social Media Content:
```
<task>
Write LinkedIn content for HuzefAI about
our AWS certification course.
</task>

<avoid>
- Starting with "Excited to announce"
- Using hashtag spam (max 3 hashtags)
- Bullet point lists
- Corporate buzzwords: leverage, synergy,
utilize, innovative, cutting-edge
- Humble bragging
- Generic advice anyone could give
</avoid>

<never>
- Sound like an advertisement
- Use exclamation marks more than twice
- End without a call to action or question
</never>
```
### Email Writing:

```
<task>
Write a follow-up email to leads who attended
HuzefAI's free webinar.
</task>

<avoid>
- "I hope this email finds you well"
- "As per our last conversation"
- "Please do not hesitate to contact us"
- Passive voice
- More than 3 paragraphs
- Listing every course feature
</avoid>

<never>
- Sound desperate or pushy
- Use "URGENT" or "LAST CHANCE" in caps
- Add more than one call to action
- Write more than 150 words
</never>
```

### Course Content Creation:
```
<task>
Write an explanation of Kubernetes for
beginners in HuzefAI's DevOps course.
</task>

<avoid>
- Assuming prior knowledge of containers
- Using acronyms without explaining them first
- Academic or textbook language
- Overwhelming with too many concepts at once
- Passive voice explanations
</avoid>

<never>
- Use the phrase "simply put" or "basically"
- Skip the practical real-world application
- Make it sound more complex than it is
- Write more than 300 words for this intro
</never>
```

## The Most Powerful Negative Prompts

These are universal negatives that improve almost any Claude output:

### Top 10 Universal Negative Prompts
```
 1. Don't start with affirmations like
'Certainly!' or 'Great question!'
```
```
2. Never use bullet points - write in
flowing prose
```
```
3. Avoid corporate buzzwords: leverage,
utilize, synergy, innovative
```
```
4. Don't add disclaimers or caveats
unless absolutely necessary
```
```
5. Never use passive voice
```
```
6. Don't summarize at the end -
trust the reader
```
```
7. Avoid hedging language like 'might',
'could possibly', 'it may be that'
```
```
8. Never write more than [X] words
```
```
9. Don't give generic advice - be
specific to my situation
```
```
10. Avoid starting consecutive sentences
with the same word
```
### Negative + Positive = Perfect Prompt

The master technique is combining positive AND negative instructions:
```
<role>
You are HuzefAI's content writer with deep
knowledge of Cloud and DevOps.
</role>

<task>
Write a LinkedIn post announcing our new
Generative AI course launching Monday.
</task>

<do>
- Start with a scroll-stopping hook
- Tell a mini story or share a surprising fact
- Write like a real person, not a brand
- End with an engaging question
- Use 1-2 relevant emojis naturally
</do>

<dont>
- Start with "Excited to announce"
- Use bullet points

<dont>
- Start with "Excited to announce"
- Use bullet points
- Sound like an advertisement
- Use corporate buzzwords
- Add more than 2 hashtags
- Exceed 200 words
</dont>

<tone>
Authentic founder voice - passionate about
teaching, genuinely excited, not salesy
</tone>
```


### Common Negative Prompting Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| Too many restrictions | Claude has no room to be creative | Limit to 5-7 key negatives |
| Contradicting positives | "Be detailed" + "Don't be long" clash | Make sure positives and negatives align |
| Vague negatives | "Don't be bad" means nothing | Be specific — "Don't use passive voice" |
| Forgetting negatives entirely | Claude uses defaults you don't want | Always include at least 3 negatives |
