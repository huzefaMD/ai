# Lesson 3
## Why Does This Work?
Claude learns from patterns. When you show it examples, it picks up on:
- Your writing style
- The exact format you want
- The tone and vocabulary
- The length of responses
- The structure you prefer

Think of it like training a new employee. Instead of describing what good work looks like, 
you show them 3 examples and say "do it like this." They get it immediately.

### Zero-Shot vs Few-Shot - Side by Side
Zero-Shot (No Examples):
` Write a course description for my AWS Fundamentals course. `

**Claude's response might be:**

```
This comprehensive AWS Fundamentals course covers core
cloud concepts including EC2, S3, IAM, and VPC. Students will learn to deploy scalable
applications on Amazon Web Services
```
Generic. Could be from any EdTech platform.

| Few-Shot (With Examples) 
Write course descriptions in this style:

Example 1:
Course: Python for Beginners
Description: "No coding experience? No problem. In 6 weeks
you'll go from writing your first line of Python to building
real automation scripts. Taught by practitioners, not
professors. Batch starts every Monday."
|---------|
Example 2:
Course: Docker & Containers
Description: "Still manually deploying apps? Join 2,000+
engineers who switched to containers. Hands-on labs,
real projects, lifetime access. Your next job wants
this skill - get it in 4 weeks."
|---------|
Now write one for: AWS Fundamentals |
|---------|
