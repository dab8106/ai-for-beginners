# PDF to briefing note, then fact-check it

**AI for everyday work** · Goes with [Lecture 13: Summarise a 60-Page Report in Minutes With AI (and Check It)](https://www.youtube.com/watch?v=blIzU7NFEMg) and [Lecture 17: AI Research With Real Sources (and How to Spot Fake Links)](https://www.youtube.com/watch?v=TfI7EOc6rD8) · About 45 minutes · No coding

## What you'll do

Your director has a Board meeting tomorrow and has sent you a 13-page feasibility study with one line: "Give me one page on this by this evening." You'll get an AI assistant to read the PDF, turn it into a one-page briefing note with a page number for every key point, and then fact-check three of its claims against the original, the way a careful analyst would.

## What you need

- An AI assistant: Claude or ChatGPT (the free tier is fine). Both can read a PDF you add to the chat.
- The starter file `starter/solar-feasibility-report.pdf`: a rooftop solar feasibility study for Deccan Cold Chain, a made-up company with four warehouses near Pune. The same text is in `starter/solar-feasibility-report.md` if a tool can't open the PDF.
- A PDF viewer (your browser is fine) to open the original side by side with the chat.
- A notes file or a sheet for the results table.

> The report is fictional. At work, never upload contracts, customer data or other confidential documents to a tool your company hasn't approved.

## Steps

Start a **new chat** and add the PDF using the attach or upload button.

### Step 1: Can it actually read the file? (3 minutes)

Send:

```
Before anything else: how many pages does this PDF have, and what is the
first sentence of the section that starts on page 6?
```

**Check:** the PDF has 13 pages, and page 6 starts the technical design section with "The proposed system at each site has four parts." If the answer is wrong or vague, the tool may not have read the whole file. Try adding it again, or use the Markdown version.

### Step 2: The lazy prompt, for comparison (3 minutes)

Send:

```
Summarise this.
```

Keep this answer. You'll compare it with the next one.

### Step 3: The briefing note (8 minutes)

Start a **new chat**, add the PDF again, and send:

```
You are a senior analyst preparing a director for a Board meeting.
The director has two minutes to read this and must vote on the proposal.

Write a one-page briefing note on the attached feasibility study, with:
1. The decision being asked for, in one sentence.
2. Five key facts the director needs (costs, savings, payback, scope, timing).
3. Conditions, exceptions and risks that could change the decision.
4. Two questions the director should ask in the meeting.

After every fact, add the page number in brackets, like this: (p. 4).
Use only what is in the document. If something isn't in it, say so.
Under 300 words.
```

**Check:** compare it with the lazy summary from Step 2. Which one could your director act on? Write one sentence on the difference.

### Step 4: Fact-check three claims (15 minutes)

This is the most important part of the lab. A summary can drop an exception, mix up two numbers, or lose the condition attached to a number. Check these three claims against the PDF itself, not against the chat.

**Claim A: the payback period.** Find what your briefing note says about the payback period. Open the page it cites, and read that page and the section on savings.

**Check:** is the number right? Is there a condition attached to it in the original? Does your briefing note mention that condition?

**Claim B: which warehouses are in the project.** Find what your briefing note says about where the panels will go. Open the site assessment section and read every site.

**Check:** does the briefing note make it clear which warehouses are, and aren't, part of the decision? Would your director come away with the right picture?

**Claim C: your choice.** Pick one more number or fact from your briefing note, for example the capital cost, the yearly saving or the start date. Open the page it cites and find the exact sentence.

**Check:** is the page number right? Is the number exactly the same as in the document? Is it the same kind of number (for example, a yearly figure and not a 25-year one)?

For each claim, write in the results table what the note said, what the document says (with the page), and whether the note was **correct**, **incomplete** or **wrong**.

### Step 5: Fix the note (8 minutes)

Go back to the chat with your briefing note. For anything you found incomplete or wrong, give specific feedback, for example:

```
Two corrections. First, on the payback period: add the condition the report
attaches to it, and the payback if that condition isn't met, with page
numbers. Second, make clear which warehouses are in Phase 1 and which are
not, and why. Keep everything else the same.
```

Then ask:

```
List every condition, exception or "this is not guaranteed" statement in the
document, with the page number and a short quote for each.
```

**Check:** compare this list with your own reading. Did it find things the briefing note had dropped?

### Step 6: Ask about a section directly (3 minutes)

With long files, a tool can skim the middle. Ask one direct question about a section in the middle of the report:

```
In the costs section, what is not included in the Phase 1 capital cost
and the payback calculation? Quote the sentences.
```

Check the answer against the PDF.

## Results table

| Item | Your result |
|---|---|
| Did Step 1 confirm the tool read the file? (pages, first sentence) | |
| Lazy summary vs briefing note: the main difference (one sentence) | |
| Claim A: what the note said | |
| Claim A: what the document says (page) | |
| Claim A: correct / incomplete / wrong | |
| Claim B: what the note said | |
| Claim B: what the document says (page) | |
| Claim B: correct / incomplete / wrong | |
| Claim C: what the note said | |
| Claim C: what the document says (page) | |
| Claim C: correct / incomplete / wrong | |
| Were all the page numbers in the note right? | |

## Stretch challenge

Run Step 3 and Step 4 in the **other** assistant (if you used Claude, try ChatGPT, or the other way round). Did both notes catch the condition and the exception? Did either one get a page number wrong? Then write the final version of the briefing note yourself, taking the best parts of both.

## Submit

Your final briefing note (after your corrections), your filled-in results table, and a screenshot of one claim you checked, with the PDF page open next to the chat.

## Answer key (open only after Step 4)

<details>
<summary>Show the answers</summary>

**Claim A.** The executive summary (page 2) says the payback is about 4.6 years. Page 8 says this **assumes net-metering approval by June 2027**, which is not guaranteed. Without it, the payback is about **6.9 years**. A note that only says "4.6 years" is incomplete, and the condition matters for a Board vote.

**Claim B.** The company has four warehouses, but Phase 1 covers only three: Chakan, Talegaon and Ranjangaon. **Bhosari is excluded** because its roof needs repair first (page 4). It may come back later as Phase 2. A note that says "solar on all four warehouses" is wrong.

**Other facts for Claim C:** Phase 1 is 1,100 kWp at a capital cost of ₹4.70 crore (pages 2 and 7). Expected yearly saving is about ₹1.08 crore before maintenance, or ₹1.02 crore after it (pages 2 and 8). Installation starts in October 2026, after the monsoon, at Ranjangaon (page 10). The roughly ₹23 crore figure is a 25-year saving, not a yearly one (page 8).

**Step 6.** Page 7: the ₹38 lakh Bhosari roof repair is not part of the project cost, and the ₹35 lakh set aside for replacing inverters is not included in the payback calculation.

</details>

## What you learned

- A good summary starts with a purpose: who it's for and what they must decide.
- Ask for a page number after every fact, so each point can be checked in seconds.
- Summaries tend to lose conditions and exceptions. Those are exactly what a decision-maker needs.
- For anything someone will act on, the source has the final say. Open the page and read it yourself.
