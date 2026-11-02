# Build a chatbot with memory in Colab

**Python and AI APIs** · Goes with [Lecture 23: What Is an API Key? (and How Not to Leak It)](https://www.youtube.com/watch?v=EyXPNzifQEw) and [Lecture 24: Your First AI API Call in Python (OpenAI and Claude)](https://www.youtube.com/watch?v=gZNiySViKeI) and [Lecture 25: System Prompts, Temperature and Cost: AI API Basics](https://www.youtube.com/watch?v=GyuZrrKl1Xw) · About 50 minutes · Copy, run and change

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dab8106/ai-for-beginners/blob/main/05-python-and-ai-apis/starter/chatbot-memory.ipynb)

## What you'll do

You'll set up an API key safely, with a spending limit, and run a ready-made Colab notebook that turns a single API call into a chatbot that remembers the conversation. You'll watch the token count grow with every turn, estimate what a conversation costs, and try a system prompt and two temperatures.

## What you need

- A Google account, for Google Colab: https://colab.research.google.com
- An API key from **one** provider. The easiest is a **free Gemini API key** from Google AI Studio (https://aistudio.google.com/apikey): no payment method needed. It has rate limits, and on the free tier Google may use what you send, and the replies, to improve its products, so use only practice data like the samples in this lab. Or use a paid API account with Anthropic (https://console.anthropic.com) or OpenAI (https://platform.openai.com). Those APIs are billed separately from any chat subscription, so you may need to add a payment method or prepaid credit. Check the provider's pricing page.
- The starter notebook `starter/chatbot-memory.ipynb`.
- A notes file or a sheet for the results tables.

> Your API key is like a password that can spend money. Never type it into a notebook cell, a screenshot, a chat or an email. In this lab it lives only in Colab Secrets.

## Steps

### Step 1: Set a spending limit first (5 minutes)

Do this **before** you create a key, so a mistake can only ever cost a little.

- **Anthropic Console:** open **Settings**, then **Limits**, and set a monthly spend limit you're comfortable with.
- **OpenAI platform:** open **Settings**, then **Limits** (in some accounts it's under **Billing**), and set a monthly budget and an email alert.
- **Free Gemini key:** the free tier has no billing, so there's nothing to limit. You can skip this step.
- On Anthropic or OpenAI, if your account uses **prepaid credits**, switch **auto-reload** or **auto-recharge** off. Then you can't spend more than the credit you've added.

Menu names change from time to time. If you can't find it, search the provider's help pages for "spend limit".

**Check:** you can see your limit on the limits or billing page, and auto-reload is off.

### Step 2: Create an API key (5 minutes)

1. In the console, open **API keys** and create a new key. Name it `colab-course`, so you know where it's used. For the free Gemini key, go to https://aistudio.google.com/apikey and click **Create API key**.
2. Copy it straight away. You often see it only once. Keep a copy in a password manager, not in a text file.

**Check:** the key appears in the list of keys with the name `colab-course`.

### Step 3: Put the key in Colab Secrets (5 minutes)

1. Click the **Open in Colab** button at the top of this guide. (Or download the notebook from the [`starter/`](../starter/) folder, and in Colab choose **File**, then **Upload notebook**.)
2. In the left sidebar, click the **key icon** (Secrets).
3. Click **Add new secret**. Name it exactly `GEMINI_API_KEY`, `ANTHROPIC_API_KEY` or `OPENAI_API_KEY`, and paste your key as the value.
4. Switch on **Notebook access** for that secret.

**Check:** the secret is listed with Notebook access on, and your key is not visible anywhere in the notebook.

### Step 4: Settings and connection (5 minutes)

1. Run the **Step 1** cell (installs the libraries).
2. In the **Step 2** settings cell, set `PROVIDER` to `"gemini"` (the default), `"anthropic"` or `"openai"`, to match your key. The default models are `gemini-3.1-flash-lite`, `claude-sonnet-5-5` and `gpt-5-mini`; model names change, so check the provider's model list for current names if you get a "model not found" error.
3. Run the **Step 2** and **Step 3** cells.
4. Run the **Step 4** cell. It sends one test message.

**Check:** Step 3 prints `Ready. Provider: ... | Model: ...`, and Step 4 prints a short hello plus a line with tokens in and tokens out. If you see "authentication failed", the key is missing, mistyped, or Notebook access is off. The code is fine.

### Step 5: Memory, on and off (10 minutes)

1. Read the comments in the **Step 5** cell. The "memory" is a plain Python list called `history`.
2. Run **Step 5**, then **Step 6**. The bot should answer the third question ("What's my name, and what's the cake for?") correctly.
3. Run **Step 7**. It asks the same question with **no** history.

**Check:** with memory, the bot knows your name is Asha and the cake is for a seventh birthday. Without memory, it has no idea. The model itself never remembered anything; your code sent the whole conversation each time.

### Step 6: Chat, and watch the tokens grow (10 minutes)

1. Run **Step 8** and have at least five more turns with the bot. Keep your messages short. Type `quit` to stop.
2. Run **Step 9**. You'll see a table and a bar chart of tokens per turn.
3. Fill in the first results table.

**Check:** the **tokens in** column goes up every turn, even when your message is just a few words, because each turn resends everything before it. Tokens out stays roughly flat.

### Step 7: Estimate the cost (5 minutes)

1. Open your provider's pricing page and find the input and output prices for your model, per 1 million tokens. On the free Gemini key you pay nothing, so use Gemini's paid prices to see what the same chat would cost.
2. Type them into the **Step 10** cell and run it.

**Check:** you get a cost for this conversation and for 1,000 conversations like it. It's a small number for one chat. Now imagine every turn for a whole team, all month.

### Step 8: System prompt and temperature (5 minutes)

1. Run **Step 11**. It asks for a cake name three times at temperature 0, then three times at 1.
2. In the **Step 2** settings cell, change `SYSTEM_PROMPT`, for example: `Only talk about Sweet Crumbs cakes and orders. Politely refuse anything else. Reply in Hindi.` Run Step 2, then run **Step 12**.

**Check:**
- At temperature 0 the three names should be the same or very close; at 1 they should vary more.
- If you see "This model did not accept temperature", that's expected for some models, especially reasoning models. Write it down. That's the lesson's point: not every model takes every setting. If you want to compare, pick another model from the provider's list that accepts temperature.
- With the new system prompt, the bot replies in Hindi and refuses the maths homework.

## Results table

**Tokens per turn (Step 6)**

| Turn | Your message (short) | Tokens in | Tokens out |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |

**Everything else**

| Item | Your result |
|---|---|
| Provider and model | |
| Your spending limit is set (yes/no), auto-reload off (yes/no) | |
| Bot's answer to "What's my name" with memory | |
| The same question without memory | |
| Estimated cost of your conversation / of 1,000 conversations | |
| Three names at temperature 0 | |
| Three names at temperature 1 (or "not accepted") | |
| Did the new system prompt work? What changed? | |

## Stretch challenge

- **Shorter memory.** Run the **Stretch** cell at the bottom. It sends only the last five messages. Compare its tokens in with Step 9. Then look at the last answer: does the bot still remember Asha's name? What's the trade-off?
- **Switch provider.** If you have keys for two providers, add the second secret, change `PROVIDER`, run Steps 2 to 6 again and compare the token counts for the same conversation. They differ, because each provider splits text into tokens differently.
- **Your own bot.** Change `SYSTEM_PROMPT` into a helper for your own job (for example, a polite reply-writer for customer emails), and test it with three realistic questions.

## Submit

- A screenshot of the Step 9 table and chart. Check that no key is visible.
- Your filled-in results tables.
- Two or three sentences: why does tokens in grow every turn, and what's one way to keep a chatbot's cost down?

## What you learned

- An API key proves who's asking and who pays. Keep it in Colab Secrets, and set a spending limit before you use it.
- An API call is: create a client, send a model name, a reply limit and a list of messages, and read the text out of the response.
- A chatbot's "memory" is your code resending the whole conversation each turn, so tokens in, and cost, grow with every turn.
- The system prompt sets rules for every reply; temperature changes how varied the replies are, and some models don't accept it.
