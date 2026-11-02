# Lab: See tokens

**How AI actually works** · Goes with [Lecture 5: Tokens and Context Windows: Why AI Forgets Your Chat](https://www.youtube.com/watch?v=n48TJBqN0Kc) · About 30 minutes · No coding

## What you'll do

You'll look at text the way an AI model sees it, as tokens, and work out what a long document costs to send and whether it fits in a model's context window.

## What you need

- A web browser.
- A tokenizer page. We use the free Tiktokenizer (no account needed): https://tiktokenizer.vercel.app/?model=o200k_base. In the top-right menu, `o200k_base` is the tokenizer used by recent OpenAI models.
- The starter file [`starter/see-tokens-texts.md`](../starter/see-tokens-texts.md) (the English and Hindi paragraphs below are also in it).
- A notes file or a sheet to fill in the results table.

> Every model family splits text a little differently, so your exact numbers can differ from a classmate's. That's expected. What matters is the pattern.

## Steps

### Step 1: Split one word

1. Open the tokenizer page.
2. Type `Unbelievable!` and look at the coloured blocks under the box.
3. Count the tokens. Now try `unbelievable` (lowercase, no "!") and `UNBELIEVABLE`.

**Check:** do capital letters and punctuation change the number of tokens? Note it down.

### Step 2: Measure a paragraph

1. Paste the English paragraph from the starter file. It has exactly 100 words.
2. Write down the token count.
3. Work out: tokens ÷ words.

**Check:** you should land somewhere around 1.1 to 1.4 tokens per word (with `o200k_base` the starter paragraph is 114 tokens, about 1.14). That's the "one token is about three quarters of a word" rule from the lesson.

### Step 3: Compare a second language

1. Paste the Hindi paragraph from the starter file. It says the same thing as the English one.
2. Write down the token count.

**Check:** is it higher or lower than English? By how much? (Most tokenizers need noticeably more tokens for Hindi.)

### Step 4: What does a long report cost?

A 30-page report is about 15,000 English words.

1. Using your ratio from Step 2, estimate its tokens.
2. Open the pricing page of any AI provider you like (search "<provider> API pricing") and find the price for **input tokens**, usually given per 1 million tokens. Write down the provider, model and price.
3. Calculate the cost to send the report once, then 100 times (for example, 100 employees each asking a question about it).

### Step 5: Does it fit?

1. Look up the **context window** of the same model on the provider's documentation page.
2. How many copies of your 30-page report would fit in it? Remember the answer has to fit too.

## Results table

| Item | Your result |
|---|---|
| Tokens in "Unbelievable!" | |
| Tokens in the 100-word English paragraph | |
| Tokens per word (English) | |
| Tokens in the Hindi paragraph | |
| Estimated tokens in a 15,000-word report | |
| Provider, model and input price per 1M tokens | |
| Cost to send the report once / 100 times | |
| Model's context window (tokens) | |
| How many reports fit | |

## Stretch challenge

Paste a line of code (for example `for i in range(10): print(i)`) and a line of emojis. Which is the most "expensive" per character: English, Hindi, code or emojis?

## Submit

A screenshot of the tokenizer showing your English paragraph, and your filled-in results table.

## What you learned

- Models see tokens, not words. In English, a token is roughly three quarters of a word.
- The same meaning can cost more tokens in some languages.
- Token counts drive both **cost** and whether something **fits** in the context window.
