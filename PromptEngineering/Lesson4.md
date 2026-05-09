# Lesson 4

## Without CoT vs With CoT
### Without Chain of Thought:
`Should I price my AWS course at ₹4,999 or ₹9,999?`

**Claude's response:**
```
I'd recommend ₹4,999 as it's more accessible for students
```
Shallow. No reasoning. Could be wrong.

## With Chain of Thought:

Should I price my AWS course at ₹4,999 or ₹9,999?

Think through this step by step:
1. `First analyze the target audience`
2. `Then consider competitor pricing in India`
3. `Then evaluate perceived value vs price`
4. `Then consider HuzefAI's current brand stage`
5. `Finally give your recommendation with easoning`

## The Magic Phrases That Trigger CoT

These phrases instantly activate step-by-step thinking in Claude:

|Phrase|Use When|
|------|--------|
|```"Think step by step"```|`Any complex problem`|
|```"Walk me through your reasoning"```|`When you want to see the logic`|
|```"Break this down"```|`Complex topics or decisions`|
|```"First analyze X, then Y, then Z"```|`When you control the thinking order`|
|```"Think out loud"```|`When you want full transparency`|
|```"Before answering, consider ... "```|`When you want Claude to weigh factors`|
|```"What are the pros and cons first?"```|`Before a recommendation`|

## 3 Levels of Chain of Thought
###  Level1- Simple CoT
Just add 
```
think step by step
```
 to any prompt:
