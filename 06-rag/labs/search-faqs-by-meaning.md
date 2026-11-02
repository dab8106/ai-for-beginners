# Search 50 FAQs by meaning

**Chat with your documents** · Goes with [Lecture 28: Embeddings Explained Simply: Meaning as Numbers](https://www.youtube.com/watch?v=sZxPwYShDxA) and [Lecture 29: Chunking and Vector Search Explained for Beginners](https://www.youtube.com/watch?v=3OmlQyjc890) · About 40 minutes · Python in Colab, no API key needed

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dab8106/ai-for-beginners/blob/main/06-rag/starter/faq-search.ipynb)

## What you'll do

You'll search the help pages of a fictional online electronics shop in two ways, by keywords and by meaning, and see for yourself where each one wins and where each one fails. You'll also choose a score threshold, so your search says "not sure" instead of showing a random answer.

## What you need

- A Google account, to open Google Colab: https://colab.research.google.com
- Two starter files, in this section's [`starter/`](../starter/) folder:
  - `starter/faq-search.ipynb`, the notebook.
  - `starter/shop-faqs.csv`, 50 made-up FAQs for **Nakshatra Electronics**, a fictional online shop in India.
- No API key. The embedding model is free and runs inside Colab.

> Everything in the starter files is fictional. When you try this with your own documents later, use only files you're allowed to share.

## Steps

### Step 1: Open the notebook

1. Click the **Open in Colab** button at the top of this guide. (Or download the notebook from the [`starter/`](../starter/) folder, and in Colab choose **File**, then **Upload notebook**.)
2. In the left sidebar, open the **Files** panel (folder icon) and upload `shop-faqs.csv`. If you skip this, Step 3 of the notebook shows an upload button instead.
3. Run the first cell (install) with **Shift + Enter**.

**Check:** the install cell finishes without a red error. A yellow warning about dependencies is fine.

### Step 2: Load the FAQs

Run the **Settings** and **Load** cells.

**Check:** it prints `50 FAQs loaded` and shows the first 10 rows, with the columns `id`, `category`, `question` and `answer`.

### Step 3: Keyword search

Run the keyword search cell. It searches for `What is your return policy?` and `When do I get my money back?`.

**Check:** the first question finds FAQ 23, "What is your return policy?", because they share the words *return* and *policy*. The second finds **nothing**: no FAQ contains *money* or *back*, even though the shop clearly has a refund FAQ. That's the weakness of keywords.

### Step 4: Make the embeddings

Run the embedding cell. The first run downloads the model, about 90 MB.

**Check:** it prints `Shape: (50, 384)`. That means 50 FAQs, each turned into a list of 384 numbers: its position on the map of meaning.

### Step 5: Cosine similarity by hand

Run the similarity cell. It compares four pairs of sentences.

**Check:** `refund status, please` vs `when do I get my money back` scores about **0.5**, while `refund status, please` vs `which TV size suits my room` scores close to **0**. No shared words, yet the first pair is close in meaning.

Now look at the subscription pair from the lesson. `Cancel my subscription` vs `Stop my monthly plan` should score a little higher than vs `Subscribe to the newsletter`, but the gap is small (about 0.48 against 0.44). A small model still reacts to similar-looking words like *subscription* and *subscribe*. Write that down: it matters later.

### Step 6: Meaning search

Run the meaning search cell.

**Check:** `When do I get my money back?` now finds FAQ 25, "How long does a refund take after I return a product?", with a score of about 0.48. Keyword search found nothing for the same question.

### Step 7: Keyword vs meaning, side by side

Run the comparison cell. For each of the six test questions, write the top result of each search in the results table, and mark which one found the right FAQ.

**Check:** you should see meaning search win clearly on the money-back and AC installation questions. Keyword search does fine when the words happen to match, like the UPI question. And look at the instalments question: **both** get it wrong. The small model doesn't know that "monthly instalments without interest" means "no-cost EMI". Try `Can I pay with EMI?` and it finds FAQ 41 easily. This is why real systems often combine both searches, which the lesson called hybrid search.

### Step 8: Your own questions

In the "Your turn" cell, change `my_question` and run it several times. Try at least:

1. A question in your own words that the shop does answer.
2. A badly worded question with spelling mistakes, like `wat is ur retrn polcy`.
3. A question in Hinglish, like `paisa wapas kab milega`.
4. A question the shop has no FAQ for, like `Do you repair bicycles?`

**Check:** normal rewording works well, usually with a score above 0.5. Heavy spelling mistakes and Hinglish score very low with this model (around 0.1), because it was trained mostly on standard English. Unrelated questions also score low, around 0.3 or below.

### Step 9: Choose a threshold

Look at your scores from Step 8. Pick a number that separates good matches from unrelated ones, set `THRESHOLD` in the last cell, and run it.

**Check:** `How do I return a phone?` gets an answer (about 0.53). `Do you repair bicycles?` (about 0.29) and `What is the capital of France?` (about 0.06) get "Sorry, I couldn't find an answer to that."

> Your scores may differ a little from the numbers above if the library version changes. The pattern is what matters.

## Results table

| Question | Keyword search: top FAQ | Meaning search: top FAQ and score | Which found the right FAQ? |
|---|---|---|---|
| When do I get my money back? | | | |
| My UPI payment went through, but the order failed | | | |
| Can someone come and set up my new AC? | | | |
| I forgot my login details | | | |
| Is it possible to pay in monthly instalments without interest? | | | |
| The box was crushed when it arrived | | | |
| Your own question 1 | | | |
| Your own question 2 | | | |
| **Threshold you chose, and why** | | | |

## Stretch challenge

1. **Try a multilingual model.** In the Settings cell, change `EMBED_MODEL` to `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`, run everything again, and ask `पैसा वापस कब मिलेगा` in Hindi script. Does it now land near the refund FAQs? Does English search get better or worse?
2. **Add five FAQs** of your own to the CSV, for example about a loyalty programme. Upload it again and search for them with new wording.
3. **Simple hybrid search.** Combine the two scores, for example `meaning score + 0.1 × shared words`, and see if the instalments question improves.

## Submit

Your filled-in results table, the threshold you chose with one sentence on why, and a screenshot of the side-by-side comparison output.

## What you learned

- Keyword search only finds shared words. Meaning search finds similar meaning, even with no shared words.
- An embedding is a list of numbers, and cosine similarity measures how close two of them are.
- Meaning search has limits too: unknown terms, heavy misspellings and other languages can fool a small model. Hybrid search and better models help.
- A threshold lets a search admit "I don't know", which is better than a confident wrong answer.
