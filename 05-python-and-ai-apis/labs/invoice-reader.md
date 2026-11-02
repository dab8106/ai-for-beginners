# Invoice reader: from images to a table

**Python and AI APIs** · Goes with [Lecture 26: Get Clean JSON From AI in Python (Invoice Example)](https://www.youtube.com/watch?v=a13xeKA5zqc) · About 50 minutes · Copy, run and change

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dab8106/ai-for-beginners/blob/main/05-python-and-ai-apis/starter/invoice-reader.ipynb)

## What you'll do

You'll run a Colab notebook where an AI model reads three supplier invoices (images), returns the details as JSON, and your code checks every reply before it goes into a pandas table. One of the invoices has a mistake printed on it. Your checks should catch it, not the AI.

## What you need

- Google Colab and the API key in Colab Secrets from the lab "Build a chatbot with memory in Colab". The free Gemini key (`GEMINI_API_KEY`) is the easiest; an Anthropic or OpenAI key works too, with your spending limit still set.
- The starter notebook `starter/invoice-reader.ipynb`.
- The three invoice images in [`starter/invoices/`](../starter/invoices/). Download them to your computer first: open each image on GitHub and use the download button.
  - `invoice-kaveri.png`, from an office supplies shop
  - `invoice-marina.png`, from an IT services company
  - `invoice-annapoorna.png`, from a caterer
- A notes file or a sheet for the results tables.

> All three companies and invoices are fictional, made up for this lab. Before you send real invoices to an AI provider, check what your company allows: they may contain bank details and other private data. Never send real invoices with the free Gemini key: on the free tier, Google may use what you send to improve its products.

> **Three invoices, not ten.** The lecture mentions ten sample invoices. This lab uses three, each with a different layout, date style and tax split, and one with a mistake printed on it. That's enough to see every check at work. To try more, make a few invoices of your own for made-up businesses and upload them in Step 3: the notebook reads every image you choose.

## Steps

### Step 1: Look at the invoices yourself (5 minutes)

Open the three images on your computer. Notice how different they are: different layouts, a date written `03/10/2026` on one and `12 October 2026` on another, the tax split into CGST and SGST on one, and `₹`, `Rs.` and no symbol at all. That's why a fixed template or simple copy-paste doesn't work, and why we ask for one fixed JSON shape.

Now check the arithmetic on each invoice with a calculator. Does every total add up? Write down what you find.

### Step 2: Open the notebook and connect (5 minutes)

1. Click the **Open in Colab** button at the top of this guide. (Or download the notebook from the [`starter/`](../starter/) folder, and in Colab choose **File**, then **Upload notebook**.)
2. Check that your API key secret is listed under the key icon, with **Notebook access** on.
3. In the **Step 2** settings cell, set `PROVIDER` (`"gemini"` is the default). The default models are `gemini-3.1-flash-lite`, `claude-sonnet-5-5` and `gpt-5-mini`. The model must accept images; check the provider's model list for current names.
4. Run the cells for Steps 1 to 3.

**Check:** Step 3 prints `Ready. Provider: ... | Model: ...`.

### Step 3: Upload the invoices (5 minutes)

Run the **Step 4** cell and choose all three PNG files when asked.

**Check:** it prints `Found 3 invoices` and shows the first one.

### Step 4: Read the prompt, then send one invoice (5 minutes)

1. Run the **Step 5** cell and read the prompt. Find the four things the lesson said to be exact about: the keys, the date format, numbers with no rupee sign, and one example of the shape.
2. Run **Step 6**. It sends the first invoice and prints the raw reply.

**Check:** the reply looks like JSON, with keys like `vendor`, `invoice_date` and `total`. If the model wrapped it in ```` ```json ```` fences, that's fine; the next step removes them.

### Step 5: Run the format checks (5 minutes)

Run **Step 7**. It first tests the checks on a deliberately bad reply, `{"vendor": "Test", "total": "twelve thousand rupees"}`, then on the real reply from Step 6.

**Check:** the bad reply produces a list of problems, including `total is not a number`. That's the lesson's quiz question: valid JSON, wrong contents. The real reply should print `First reply passed the format check.`

### Step 6: Read all three and build the table (10 minutes)

1. Run **Step 8** (ask again with feedback) and **Step 9** (check the numbers). These cells only define functions, so nothing prints.
2. Run **Step 10**. It reads every invoice, retries any reply that fails the format check, runs the number checks, and shows two tables.
3. Run **Step 11**. It adds up the totals, lists invoices with warnings, and saves two CSV files.
4. Fill in the results table.

**Check:** compare the table with the expected values below.

| File | Vendor | Invoice number | Date | Subtotal | Tax | Total | checks |
|---|---|---|---|---|---|---|---|
| invoice-kaveri.png | Kaveri Office Supplies | INV-2026-0412 | 2026-10-03 | 10,100 | 18%, 1,818 | 11,918 | ok |
| invoice-marina.png | Marina Tech Services | MTS/883 | 2026-10-12 | 16,350 | 18%, 2,943 | 19,293 | ok |
| invoice-annapoorna.png | Annapoorna Caterers | AC-1177 | 2026-10-21 | 11,700 | 5%, 585 | 12,825 | warning |

- **Kaveri:** the date `03/10/2026` must become `2026-10-03` (3 October), not 10 March. Indian dates are day first.
- **Marina:** CGST 9% plus SGST 9% must be added up to 18% and 2,943.
- **Annapoorna:** 11,700 plus 585 is **12,285**, but the bill says **12,825**: two digits swapped. The `checks` column should say so. If the AI "fixed" the total to 12,285, your prompt's rule "copy every number exactly as printed" didn't hold; that's worth noting.
- Total payable across all three, as printed: **44,036**.

### Step 7: Break the prompt on purpose (10 minutes)

1. In the **Step 5** cell, delete the line `- All amounts are plain numbers: no currency symbol, no commas, no words.` and the line about Indian dates. Run Step 5, then run Step 10 again.
2. Watch the output. Do any invoices fail the format check and get retried? Do any end up in "Send these to a person to check"? Did a date come back wrong but still pass, because it was a real date in the wrong order?
3. Put the two lines back and run Steps 5 and 10 once more.

**Check:** without exact rules, you'll often see retries or a wrongly ordered date. Note what happened in the second results table. The retries are the "ask again, with feedback" loop doing its job, and the date shows why you check the contents, not just the format.

## Results table

**Your table (Step 6)**

| File | Vendor | Date | Total | checks | Matches the expected values? (yes/no) |
|---|---|---|---|---|---|
| invoice-kaveri.png | | | | | |
| invoice-marina.png | | | | | |
| invoice-annapoorna.png | | | | | |

**Everything else**

| Item | Your result |
|---|---|
| Provider and model | |
| Did your calculator spot the Annapoorna mistake in Step 1? | |
| Total payable across all three (Step 11) | |
| Number of retries in the normal run | |
| What happened without the two rules (Step 7) | |

## Stretch challenge

- **A fourth invoice.** Make your own invoice image (a screenshot of a table you type in a spreadsheet works) with a mistake in one line, for example quantity 3 times 250 written as 700. Upload it and run Steps 4 and 10. Does the line check catch it?
- **A new field.** Add `"due_date": "YYYY-MM-DD or null"` to the prompt, add it to `REQUIRED_KEYS`, and add it to the summary table in Step 10. Only one invoice has a due date. What does the model return for the others?
- **Provider schema settings.** Gemini, Anthropic and OpenAI all offer a setting that makes replies follow a JSON schema you define (search their docs for "structured outputs"). Try it, and see whether you still need the format check. (Hint: keep the number checks either way.)
- **Ten times the volume.** Two hundred invoices a month means 200 API calls. Using the token counts from the chatbot lab's method, how would you estimate the monthly cost before switching it on?

## Submit

- A screenshot of the two tables from Step 10, and the warning list from Step 11. Check that no key is visible.
- Your filled-in results tables.
- Two or three sentences: why should the AI copy the wrong total exactly, instead of fixing it?

## What you learned

- Ask for JSON with exact keys and formats, and show one example of the shape.
- Check every reply with code: first the format (valid JSON, keys present, numbers are numbers, dates are dates), then the contents (do the numbers agree).
- When the format check fails, ask again with the problems listed, a few times at most, then send it to a person and move on.
- Once the data is in a pandas table, it's ordinary data you can add up, filter and save.
