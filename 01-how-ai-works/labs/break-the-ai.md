# Lab: Break the AI, then fix it

**How AI actually works** · Goes with [Lecture 7: Why AI Makes Things Up (Hallucinations) and How to Catch It](https://www.youtube.com/watch?v=grYRk0ZE0VU) · About 45 minutes · No coding

## What you'll do

You'll try to catch an AI assistant making things up (hallucinating), check its answers yourself, and then fix the problem by grounding it in a source document.

## What you need

- An AI assistant: Claude or ChatGPT (the free tier is fine). Many assistants now search the web on their own. Watch for a "Searched the web" line above each answer: with a search, the assistant can check itself; without one, it answers from memory, which is where made-up details come from. If your tool has a web-search switch, try each test once with it on and once with it off.
- The starter file [`starter/leave-policy.md`](../starter/leave-policy.md), a short, made-up company policy.
- A browser tab for checking answers (Google Scholar: https://scholar.google.com, or https://doi.org).

> Use only the provided files. Never paste real company or client data into a public AI tool.

## Part A: Try to catch it (20 minutes)

Start a **new chat** for each test, so earlier answers don't influence later ones.

### Test 1: Citations on a niche topic

Ask:

```
List three peer-reviewed research papers about how the monsoon season affects
productivity in Mumbai's IT offices. For each, give the authors, year, journal
and DOI.
```

Now check each paper: search the exact title in Google Scholar, and paste each DOI into https://doi.org.

### Test 2: A precise number

Ask:

```
Exactly how many public libraries were operating in Pune in 2019?
Give a single number.
```

Ask yourself: did it give a confident number? Did it say where the number came from? Could you verify it?

### Test 3: After the cutoff

Ask:

```
What were the three biggest news stories in India yesterday?
```

Did it say it doesn't know, or did it produce stories anyway?

### Record your results

| Test | What it answered (short) | Confident? (yes/no) | Verified true? (yes/no/can't tell) |
|---|---|---|---|
| 1. Paper A | | | |
| 1. Paper B | | | |
| 1. Paper C | | | |
| 2. Number | | | |
| 3. News | | | |

## Part B: Fix it with grounding (20 minutes)

Open a new chat and paste this prompt, followed by the whole text of `leave-policy.md`:

```
Answer the questions below using ONLY the policy text I paste after them.
If the answer is not in the text, say "The policy doesn't say."
Quote the sentence you used for each answer.

Questions:
1. How many days of annual leave does a full-time employee get?
2. Can unused annual leave be carried over? How much?
3. How many days of paternity leave are there?
4. Is there a leave policy for interns?

Policy text:
<paste the policy here>
```

**Check:** questions 1 to 3 should come back with a quote from the policy. Question 4 is **not** answered in the policy, so a well-grounded answer says "The policy doesn't say." If it invents an intern policy instead, tighten your instruction and try again.

### Record your results

| Question | Answer | Quote given? | Correct per the policy? |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

## Reflect (5 minutes)

Write two or three sentences on each:

1. Which test made the AI hallucinate most easily, and why do you think that was?
2. What changed in Part B that made the answers trustworthy?
3. Name one task at your own job where you'd now always ask for a source.

## Stretch challenge

Run Test 1 and Part B in a **second** assistant (if you used Claude, try ChatGPT, or the other way round). Do they fail in the same places?

## Submit

Both filled-in tables, a screenshot of your Part B chat, and your reflection.

## What you learned

- AI can produce confident, specific, and completely made-up answers, especially citations, exact numbers, and recent events.
- Always open and check a link or reference before you rely on it.
- Grounding (giving the source text and telling the AI to use only that) is the most effective everyday fix.
