# Build your personal prompt library

**Prompting that works** · Goes with [Lecture 11: Get Tables and JSON From ChatGPT Every Time](https://www.youtube.com/watch?v=CauvI8IM91o) and [Lecture 12: Stop Saying "Make It Better": How Pros Iterate With AI](https://www.youtube.com/watch?v=d2Ioa-Hk72E) · About 40 minutes · No coding

## What you'll do

You'll turn the best prompts from this section into reusable templates, with placeholders you fill in each time. You'll test every template on safe, made-up inputs, improve it with specific feedback, and then fold that feedback back into the template, so next time it works in one go. You'll finish with a small library of at least five templates you'll actually use at work.

## What you need

- An AI assistant: Claude or ChatGPT (the free tier is fine).
- The starter file `starter/prompt-library-template.md`. It has the layout for each entry, one worked example, and fictional test inputs.
- Your five fixed prompts from the lab where you fixed five bad prompts, if you've done it. If not, you can still do this lab from the starter file.
- A place to keep your library that you open every day: Google Docs, Notion, OneNote or a notes app. Some assistants also let you save instructions or projects, but a plain document works with every tool, and moves with you when tools change.

> Your library will hold templates, not data. Use placeholders such as `[CLIENT A]` in the template, and fill in real details only when you use it, in a tool your company has approved.

## Steps

### Step 1: Set up your library (3 minutes)

1. Create a new document called **My prompt library**.
2. Copy the template layout and the worked example from the starter file into it.

**Check:** your document has the headings Name, Use it when, Technique, Tested in, Prompt and Notes.

### Step 2: Choose your five templates (5 minutes)

Pick five tasks you do, or expect to do, every week. Cover at least four different techniques from this section. If you're not sure, start with these:

| Template | Technique |
|---|---|
| Reply to a customer or colleague | Four parts: role, context, task, format |
| Meeting notes to action items | Table with named columns |
| Write in my style (posts, product text, replies) | Examples |
| Compare options and recommend one | Step by step |
| Start any big task | Ask me questions first |

Write the five names into your library.

### Step 3: Turn a prompt into a template (7 minutes)

Take your first prompt and replace every detail that changes from one use to the next with a placeholder in square brackets. For example, the meeting-notes prompt becomes:

```
Below are raw notes from a [TYPE OF MEETING].

1. Give a two-line summary of what was decided.
2. List every action item as a table with the columns:
   Task | Owner | Deadline | Notes.
   If no deadline was given, write "not set". If no owner was given, write
   "not decided". Don't invent dates or names.
3. List open questions that nobody owns yet.

Notes:
[NOTES]
```

Do the same for the other four. For the "ask me questions first" template, you can use this:

```
I need help with [TASK]. It's for [AUDIENCE], and the goal is [GOAL].

Before you write anything, ask me up to five questions about anything you
need to know to do this well. Ask them all at once, as a numbered list.
Then wait for my answers.
```

**Check:** read each template. Is every name, number, date and company name now a placeholder? Is every instruction that stays the same still written out in full?

### Step 4: Test each template (12 minutes)

For each template, start a **new chat**, fill in the placeholders with a test input from the starter file, and send it.

1. Read the answer. What would you change?
2. Give **one** round of specific feedback. Not "make it better", but what to change, for example `Keep it under five lines and drop the closing paragraph.`
3. If the feedback fixed it, that instruction belongs in the template.

**Check:** for the step-by-step template, the laptop test input should give a visible calculation and a one-line recommendation. For the table template, the three reviews should come back as three rows. If the answer doesn't have the shape you need, the template is missing a format instruction.

### Step 5: Fold your feedback back in (5 minutes)

This is the step most people skip, and it's what makes a library useful.

1. For each template, add the instruction from your feedback into the prompt itself.
2. Start a new chat and run the updated template once more, with the same test input.
3. Fill in **Notes** (what to watch for in the answer) and **Last tested**.

**Check:** does the updated template now give a usable answer in **one** go, with no follow-up?

### Step 6: Test in the other assistant (5 minutes)

Run two of your templates in the **other** assistant (if you used Claude, try ChatGPT, or the other way round), with the same test inputs.

**Check:** do they work in both? If one needs an extra instruction to work in the other tool, add it to the template, since it probably makes the prompt clearer for both. Update **Tested in**.

### Step 7: Make it easy to find (3 minutes)

1. Give each template a name you would search for, for example "Payment reminder", not "Email prompt 3".
2. Put the template you'll use most often at the top.
3. Bookmark the document, or pin it, where you'll see it at work.

## Results table

| Template name | Technique | Score of first test (1–5) | Feedback you gave | Score after folding it back in (1–5) | Works in both assistants? |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

## Stretch challenge

Ask the assistant to review your library. Start a new chat and send:

```
Below are five prompt templates I use at work. For each one, point out:
anything vague that could get a generic answer, a missing instruction for
what to do when information is missing, and one improvement. Don't rewrite
them, just give me a short list for each.

[YOUR FIVE TEMPLATES]
```

Apply the suggestions you agree with, and test again. Then add a sixth template for a task from your own job.

## Submit

Your prompt library document (with at least five tested templates, each with Notes and Last tested filled in), and your filled-in results table.

## What you learned

- A good prompt is worth saving. Placeholders turn a one-off prompt into a template you can reuse every week.
- Specific feedback fixes an answer once. Folding it back into the template fixes it for every future use.
- Test templates on made-up inputs, so you never need real data to build your library.
- A library in a plain document works with any assistant, and moves with you when tools change.
