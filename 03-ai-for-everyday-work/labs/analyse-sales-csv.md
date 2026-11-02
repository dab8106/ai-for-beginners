# Analyse a sales CSV

**AI for everyday work** · Goes with [Lecture 15: Analyse Excel Spreadsheets With AI (and Check the Numbers)](https://www.youtube.com/watch?v=YqFNTDclLQM) · About 40 minutes · No coding

## What you'll do

You're the new operations analyst at a small bakery chain in Pune. Your manager has sent you three months of sales and asked: what's selling, what's growing, and what should we worry about? You'll run a health check on the data, find the main patterns with an AI assistant, make a chart, check one key number yourself, and write a one-page summary for your manager.

## What you need

- An AI assistant: Claude or ChatGPT (the free tier is fine). Both can read a CSV file you add to the chat.
- The starter file `starter/pune-bakery-sales.csv`: January to March 2026 sales for Sahyadri Bakes, a made-up bakery chain with four outlets in Pune. It has about 60 rows and five columns: `date`, `outlet`, `product`, `units` and `price_inr` (the price of one unit, in rupees).
- Google Sheets (free with a Google account) or Excel, to check one number yourself.
- A notes file or a sheet for the results table.

> The data is fictional. Never add real sales files with customer names, phone numbers or prices to a tool your company hasn't approved.

## Steps

Start a **new chat**, and add the CSV file to it using the attach or upload button (the paperclip or plus icon next to the message box).

### Step 1: Health check first (5 minutes)

Before asking any business question, check the data. Send:

```
I've attached a CSV of bakery sales. Before any analysis, describe the data:
how many rows, what each column contains, the date range, and the list of
outlets and products. Then list anything odd: missing values, values in
different formats, spelling differences, or rows that look like test data.
```

**Check:** the data has three small problems hidden in it on purpose. A good health check finds all three. Write down each one. If the assistant finds fewer than three, ask: `Look again, row by row. Are all the outlet names and dates written the same way?`

### Step 2: Clean it, in words (3 minutes)

Tell the assistant how to handle the problems. Send:

```
For all the analysis that follows: treat outlet names that differ only in
spelling or capitals as the same outlet, read all dates as day of the month
at month end, and leave out any test rows. Confirm how many rows remain.
```

**Check:** 60 rows should remain.

### Step 3: Ask plain questions (10 minutes)

Revenue is `units × price_inr`. Send each question as a separate message:

```
Add a revenue column (units times price_inr). What is the total revenue for
January to March, and how much of it came from each outlet?
```

```
Rank the five products two ways: by total units sold, and by total revenue.
Show both rankings in one table. What's the most interesting difference
between the two rankings?
```

```
For each outlet, show revenue by month in a table, with the percentage change
from January to March. Which outlet is growing fastest, and which one has a
problem?
```

```
Which single product changed the most between January and March, across all
outlets? Show the monthly units.
```

**Check:** you should now be able to name at least three clear patterns in the data, one about **products**, one about **outlets**, and one about **a change over time**. Write each pattern in one sentence in the results table.

### Step 4: Make a chart (5 minutes)

Send:

```
Make a line chart of monthly revenue for each outlet, one line per outlet,
with months on the x-axis. Give it a clear title.
```

**Check:** the chart should make one outlet's rise and another outlet's dip easy to see. If your assistant can't draw a chart in your plan, ask it for the monthly table instead, and make the chart in Google Sheets (Insert, then Chart).

### Step 5: Check one number yourself (7 minutes)

AI is a fast junior analyst. You still check its work.

1. Ask: `Explain exactly how you calculated the total revenue. Which rows did you include?`
2. Open the CSV in Google Sheets (File, then Import, then Upload) or Excel.
3. In an empty column F, type `=D2*E2` in row 2 and fill it down to the last row. That's revenue per row.
4. Click the empty cell under the last row of column F and use the sum button (Σ), or type `=SUM(F2:F` followed by the last row number and `)`.
5. Compare your total with the assistant's total from Step 3.

**Check:** the correct total for January to March is **₹45,17,570** (about ₹45.2 lakh). The test row adds zero, so it doesn't change the total. If the assistant's number is different, show it your sum and ask it to find the gap.

> Typing a formula into a sheet is not coding. It's the same quick check you'd do on any report before you send it.

### Step 6: Story or guess? (3 minutes)

Send:

```
Why did the outlet with the problem drop in March?
```

**Check:** read the answer carefully. The data has no column for weather, festivals, road works or competitors, so it **cannot** tell you why. A good answer says the data shows *what* happened, not *why*, and suggests what you could find out. If the assistant gives you a confident reason, ask: `Which column in the data shows that?` Note what it says.

### Step 7: The one-page summary (7 minutes)

Send:

```
Write a one-page summary for my manager, the operations head of Sahyadri
Bakes. Format:
- A two-line headline of the quarter.
- The three most important patterns, each with one number from the data.
- One risk to look into, with what we'd need to find out (don't guess the cause).
- Two practical suggestions for April, each linked to a pattern.
Plain English, no jargon, under 300 words.
```

Read it as your manager would. Check each number in it against your earlier answers, and change anything that sounds like a guess presented as a fact.

## Results table

| Item | Your result |
|---|---|
| The three data problems found in the health check | |
| Rows left after cleaning | |
| Total revenue, January to March (assistant) | |
| Total revenue, January to March (your own sum) | |
| Top product by units / top product by revenue | |
| Pattern 1, products (one sentence) | |
| Pattern 2, outlets (one sentence) | |
| Pattern 3, change over time (one sentence) | |
| What the assistant said about *why* sales dropped | |
| Did the summary include any guess as a fact? (yes/no, which) | |

## Stretch challenge

Add the same CSV to the **other** assistant (if you used Claude, try ChatGPT, or the other way round) and send the Step 1 and Step 3 prompts. Do both find all three data problems? Do they agree on the total? Which summary would you rather send to your manager, and why?

## Submit

Your chart, your filled-in results table, and the final one-page summary after your own edits.

## Answer key (open only after you finish)

<details>
<summary>Show the answers</summary>

**The three data problems:** one row spells the outlet `Viman nagar` (small n); one row has the date written as `31/03/2026` instead of `2026-03-31`; and one row is a `TEST ITEM` with 0 units and price 0.

**Total revenue, January to March:** ₹45,17,570.

**Revenue by outlet, January to March:**

| Outlet | January | February | March | Change, January to March |
|---|---|---|---|---|
| Kothrud | ₹4,24,190 | ₹4,56,090 | ₹4,99,670 | +18% |
| Viman Nagar | ₹4,19,410 | ₹4,58,370 | ₹5,16,960 | +23% |
| Hadapsar | ₹3,56,230 | ₹3,81,300 | ₹3,02,880 | −15% (−21% from February) |
| Baner | ₹1,59,120 | ₹2,21,430 | ₹3,21,920 | +102% |

**The patterns:**

1. **Products:** Pav sells by far the most units (24,125) but cold coffee earns the most revenue (₹11,18,760). Chocolate truffle cake earns almost as much as Pav (₹9,57,150 against ₹9,65,000) from fewer than a tenth of the units.
2. **Outlets:** Baner, the smallest outlet, roughly doubled its revenue from January to March. Hadapsar fell in March, by about a quarter in every product except cold coffee, which grew only slightly in March while it grew strongly at the other outlets.
3. **Change over time:** cold coffee units roughly doubled, from 2,085 in January to 4,222 in March, at all four outlets.

**Why did Hadapsar drop?** The data can't say. A good answer suggests checking things outside the data, such as opening hours, staff changes, road works or a new competitor nearby.

</details>

## What you learned

- Always run a health check before the analysis. Spelling differences, mixed date formats and test rows are common, and they quietly change results.
- Units and revenue can tell very different stories, so ask for both.
- Check at least one key number yourself, and ask the AI to explain how it got its numbers.
- Data shows *what* happened. If the cause isn't in the data, an explanation is a guess, not a finding.
