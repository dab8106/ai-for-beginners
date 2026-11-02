# Fix five bad prompts

**Prompting that works** · Goes with [Lecture 8: The 4-Part Prompt Formula That Fixes Bad AI Answers](https://www.youtube.com/watch?v=ypvup6hwrPk) and [Lecture 9: Few-Shot Prompting: Show AI Examples, Get Better Results](https://www.youtube.com/watch?v=UKncKUWVZLE) and [Lecture 10: "Think Step by Step": The Prompt Trick That Boosts AI Accuracy](https://www.youtube.com/watch?v=qoEMprBgf8c) · About 45 minutes · No coding

## What you'll do

You'll run five short, vague prompts, see the generic answers they produce, and then fix each one with a technique from this section: the four parts of a good prompt, examples, step by step, structured output, and one round of specific feedback. By the end you'll have five before-and-after pairs, and a feel for which fix matters most for which kind of task.

## What you need

- An AI assistant: Claude or ChatGPT (the free tier is fine).
- The starter file `starter/five-bad-prompts.md`. It has the five bad prompts and the material each one needs: a customer message, meeting notes, two past captions, two price offers and five enquiries. All of it is made up.
- A notes file or a sheet for the results table.

> Use only the starter material. Never add real customer messages, names or phone numbers to a public AI tool.

## How to run each prompt

For each of the five prompts:

1. Start a **new chat** and send the **bad prompt** with its material, so you see what a vague prompt produces. Score the answer from 1 (useless) to 5 (ready to use).
2. Start another **new chat** and send the **fixed prompt**. Score it again.
3. Give **one round** of specific feedback in the same chat, and see what changes.

New chats matter: if you fix the prompt in the same chat, the earlier answer steers the new one, and you can't compare fairly.

## Steps

### Prompt 1: The customer reply (four parts)

The bad prompt is `Write a reply to this customer.` followed by Anjali's message. Send it, and score the reply.

Now the fix. Give it a **role**, the **context**, a clear **task** and a **format**:

```
You are the customer care team at Shree Balaji Furnishings, a family-run
furniture shop in Nagpur. You write warm, honest replies that take
responsibility without long excuses.

Context: the customer's sofa (order SB-20417) was promised by 12 October and
is 10 days late, because our fabric supplier delivered late. It is now ready.

Task: write a reply to her message below that apologises, explains the delay
in one sentence, confirms delivery on Saturday 25 October between 10 am and
1 pm, and confirms we will refund the ₹1,500 delivery charge.

Format: under 120 words, a short subject line, no jargon, signed
"Warm regards, Customer Care, Shree Balaji Furnishings".

Customer's message:
<add Anjali's message from the starter file here>
```

**Check:** does the new reply mention the order number, the exact delivery slot and the refund? Did the bad version invent anything, such as a discount, a date or a reason?

One round of feedback: `Good. She took leave twice, so acknowledge that in one short line. Keep the rest the same.`

### Prompt 2: The meeting notes (format)

The bad prompt is `Summarise these meeting notes.` followed by the notes. Send it, and score it.

Now the fix. The missing part is the **format**:

```
Below are raw notes from a school's Annual Day planning meeting.

1. Give a two-line summary of what was decided.
2. Then list every action item as a table with the columns:
   Task | Owner | Deadline | Notes.
   If no deadline was given, write "not set". If no owner was given, write
   "not decided". Don't invent dates or names.
3. Finally, list open questions that nobody owns yet.

Notes:
<add the meeting notes from the starter file here>
```

**Check:** count the action items. The notes contain at least six (songs list, sound quotes, food stall volunteers, drill practice slots, chief guest shortlist, budget check), plus an open question about who prints the invitations. Are the sound quotes marked "not set"? Did the bad version bury any of them?

One round of feedback: `Add a row for the next meeting on 14 November, and sort the table by deadline.`

### Prompt 3: The Instagram caption (examples)

The bad prompt is `Write an Instagram caption for our new filter coffee.` Send it on its own, and score it.

Now the fix. Don't describe the style. **Show** it, with the two past captions, and keep the examples clearly separate from the new task:

```
You write Instagram captions for Kaapi Corner, a small café in Coimbatore.
Here are two past captions our customers loved. Match their style: length,
humour, and how they end.

### Example 1
Monsoon outside. Ginger, cardamom and a little too much sugar inside. Just
how Amma made it. Pull up a chair, the second cup is on us till Sunday.
#KaapiCorner #Coimbatore

### Example 2
We tried to make it healthy. Then we added jaggery and walnuts, and nobody
complained. Fresh out of the oven every morning at 8.
#KaapiCorner #BakedToday

### New task
Write one caption in the same style for our new traditional filter coffee:
decoction from a local estate, served in a steel tumbler and dabarah.
Offer: free tumbler refill on weekdays before 10 am, this month only.
Give me three options.
```

**Check:** compare the length and tone with the bad version. Did the examples beat words like "catchy"? Did any option copy a phrase from the examples too closely?

One round of feedback: pick your favourite option and say exactly what to change, for example `Option 2, but make the offer clearer and drop the second hashtag.`

### Prompt 4: The cheaper plan (step by step)

The bad prompt is `Which plan is cheaper?` followed by the two offers. Send it, and score it. Did it show any working?

Now the fix. Ask it to **work through the steps** before it answers:

```
My team of 6 people needs co-working space for 12 months. Compare the two
offers below.

Work through it step by step: first the total 12-month cost of Plan A, then
of Plan B, including every fee and discount, then the difference. Show each
calculation on its own line. Then give your recommendation in one sentence.

<add the two offers from the starter file here>
```

**Check:** Plan A costs 6 × ₹7,500 × 11 months = ₹4,95,000. Plan B costs ₹38,000 × 12 + ₹25,000 = ₹4,81,000. Plan B is cheaper by **₹14,000**. Did the bad version miss the free month or the setup fee? With the steps visible, could you spot a wrong step?

One round of feedback: `Now assume the team grows to 8 people after 6 months. Recalculate, step by step.`

### Prompt 5: The enquiries table (structured output)

The bad prompt is `Put these enquiries in a table.` followed by the five enquiries. Send it, and score it.

Now the fix. Name the **columns**, and say what to write when something is **missing**:

```
Turn the WhatsApp enquiries below into a table, one row per enquiry, with
exactly these columns:
Name | Event type | City | Date | Services (photo, video, drone) | Budget (₹) | Next step

Rules:
- If something isn't in the message, write "not given". Never guess a date
  or a budget.
- Write budgets as full numbers, for example 2.5L becomes 2,50,000.
- "Next step" is one short action for our team, for example "send rates".

Enquiries:
<add the five enquiries from the starter file here>
```

**Check:** Rohit's budget and Meera's budget should both be "not given", and Meera's date should stay vague ("March, first week"), not become an exact date. Did the bad version invent anything?

One round of feedback: `Add a column "Priority" (high, medium, low) based on how soon the event is and how clear the budget is. Explain your rule in one line under the table.`

## Results table

| Prompt | What was wrong with the bad prompt | Technique you used | Score before (1–5) | Score after (1–5) | What your one round of feedback changed |
|---|---|---|---|---|---|
| 1. Customer reply | | | | | |
| 2. Meeting notes | | | | | |
| 3. Instagram caption | | | | | |
| 4. Cheaper plan | | | | | |
| 5. Enquiries table | | | | | |

## Stretch challenge

Pick the prompt where your fixed version still wasn't quite right. Start a new chat and begin with: `Before you write anything, ask me the questions you need answered to do this well.` Then answer its questions. Did it find a gap in your brief? Finally, run your best two fixed prompts in the **other** assistant (if you used Claude, try ChatGPT, or the other way round). Does the same fix work in both?

## Submit

Your filled-in results table, and a screenshot of one before-and-after pair (the bad answer and the fixed answer side by side).

## What you learned

- Vague prompts get generic answers, because the AI has to guess. Each fix removes a guess.
- Different tasks need different fixes: the four parts for a brief, examples for a style, step by step for numbers and decisions, named columns for data.
- Always say what to write when information is missing, or the AI may invent it.
- Treat the first answer as a draft. One specific round of feedback often gets you the rest of the way.

Keep your five fixed prompts. In the lab where you build your personal prompt library, they become your first templates.
