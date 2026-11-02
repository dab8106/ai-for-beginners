# Capstone project brief

**Responsible AI, careers and your capstone** · Goes with [Lecture 38: AI Careers: Build a Portfolio That Gets Noticed](https://www.youtube.com/watch?v=mPjLlKMAITw) · About 4 to 8 hours, spread over a week or two · No-code or Python, your choice

## What you'll do

You'll build a small AI assistant for a real problem: one that you, or someone you know, actually has. Then you'll test it, write it up honestly, and add it to your portfolio. This is the strongest piece of work you'll show anyone, because it's yours from start to finish.

Good capstone problems are small, repeated and annoying. For example:

- A clinic in Pune answers the same patient questions all day: timings, fees, which documents to bring, how to book.
- A shop owner tracks UPI payments in a spreadsheet and wants a weekly summary of who has paid and who hasn't.
- A tuition centre gets the same admission questions by email every June.
- A small team spends an hour every Monday turning meeting notes into a task list.

If you can't think of a problem yet, use one of the two made-up problems in [`sample-problems/`](sample-problems/). Both count just as much.

## Pick a track

There are two tracks. Both count. Pick the one that fits your problem and your comfort level, not the one that sounds more impressive.

### Track A: No-code

Build **a custom assistant and an automation** that work together.

1. **A custom assistant** (a Claude Project, a ChatGPT Project or custom GPT, or similar) with your own files and written instructions. Use what you did in the lab [Build a company FAQ assistant](../../04-no-code-assistants-and-automation/labs/faq-assistant.md).
2. **An automation with an AI step** (for example in n8n) that takes something in, uses AI to summarise, label or extract it, and puts the result somewhere useful, such as a sheet. Use what you did in the lab [Email to AI summary to Google Sheet](../../04-no-code-assistants-and-automation/labs/email-to-sheet.md).

For the clinic example: an assistant that answers patient questions only from the clinic's FAQ, plus an automation that labels incoming enquiry emails (booking, report, billing, other) and logs them in a sheet.

### Track B: Python

Build an app in Google Colab that uses **at least one** of these:

- **RAG**: answers questions from your own documents and shows its sources. Start from the [Chat with your PDF](../../06-rag/labs/chat-with-your-pdf.md) notebook.
- **Tools**: the model calls one or more functions you wrote. Start from the [chatbot with two tools](../../07-agents-and-mcp/labs/chatbot-with-two-tools.md) notebook.
- **An agent**: the model works in a loop with tools, with a step limit and checks on every input. Start from the same tools notebook, or build an [MCP server](../../07-agents-and-mcp/labs/mcp-connect-and-build.md).

For the UPI example: a notebook that reads the payments sheet, uses a tool to total payments per customer, and answers questions like "who hasn't paid this month?", with the numbers checked by code, not by the model.

You don't have to write code from scratch. Starting from a lab notebook and changing it for your problem is exactly the skill this course teaches.

## Requirements (both tracks)

Your project must:

1. **Solve one clear problem** for one clear user. Write it in one sentence before you build anything.
2. **Use only made-up or permitted data.** No real customer names, phone numbers, health details, bank details or company documents unless you have permission and your tool is approved for them. When in doubt, make up realistic sample data, as the labs do.
3. **Keep keys safe.** API keys live only in Colab Secrets or your tool's credential store. Never in a notebook cell, a screenshot, a file you share or your write-up. Keep a spending limit on every paid key.
4. **Say "I don't know".** The assistant answers from its sources and says when the answer isn't there, instead of guessing.
5. **Be tested.** Write at least 10 test questions or inputs before you build, with the answer you expect. Include at least two that it should refuse or say it doesn't know, and at least two prompt-injection attempts like the ones from [Red-team your own chatbot](../labs/red-team-your-chatbot.md). Record what happened, fix what fails, and test again.
6. **Have a human check.** Decide which outputs a person must check before they're used (for example, anything about money, health or a customer), and say so in your write-up.

## Steps

### Step 1: Write the plan (30 minutes)

Copy [`project-plan-template.md`](project-plan-template.md) and fill in the problem, the user, the track, the data and your test questions. Keep it to one page.

**Check:** a friend can read your plan and tell you, in one sentence, what your assistant does and for whom.

### Step 2: Build the smallest version (1 to 3 hours)

Build the simplest thing that answers your first three test questions. Don't add features yet.

**Check:** it gives a correct answer to at least one real test question, end to end.

### Step 3: Test it like a strict examiner (1 hour)

Run all your test questions in fresh chats (or fresh runs). Fill in the results table in your plan: expected answer, actual answer, pass or fail.

**Check:** every test has a result, including the ones that failed.

### Step 4: Fix, then test again (1 to 2 hours)

Fix the failures one at a time: better instructions, better files, smaller chunks, clearer tool descriptions, stricter checks in code. Run the full test list again after each change, so a fix in one place doesn't break another.

**Check:** you can name at least one thing you changed and the test it fixed.

### Step 5: Write it up (1 hour)

Copy [`portfolio-page-template.md`](portfolio-page-template.md) and write one page: the problem, how you built it, what went wrong, what you'd improve. Add two or three screenshots, with no personal details, API keys or account names visible.

**Check:** someone who has never seen your project understands what it does from the page alone.

## Submit

There's nothing to hand in to us. Your capstone is for your portfolio:

- Put the write-up somewhere people can see it: a GitHub repository, a blog post, a LinkedIn post or a shared document.
- If you built in Python, share the notebook too, with outputs cleared and no keys in it.
- Share what you built in the comments under the lecture. We'd love to see it.

## Checklist before you share

- [ ] The problem fits in one sentence.
- [ ] Only made-up or permitted data is used, and none is visible in screenshots.
- [ ] No API keys, passwords or personal account details anywhere.
- [ ] At least 10 tests, with results, including refusals and injection attempts.
- [ ] The write-up says honestly what is a demo and what is in real use.
- [ ] The write-up says what you'd improve next.

## What you'll have at the end

- A working assistant for a real problem, built on one of the two tracks.
- A tested, honest one-page write-up you can link from your CV and LinkedIn.
- A line for your CV that describes an outcome, not a tool. Not "used AI tools", but for example: "Built an assistant that answers patient questions from the clinic FAQ, tested on 20 questions, with a human check on anything about fees."
