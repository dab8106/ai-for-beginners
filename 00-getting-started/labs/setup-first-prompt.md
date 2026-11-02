# Accounts, a spending limit and your first prompt

**Welcome and lab setup** · Goes with [Lecture 2: The Only 4 AI Tools You Need to Start](https://www.youtube.com/watch?v=gURuQVXo5rw) · About 30 minutes · No coding

## What you'll do

You'll set up the free accounts you'll use throughout this series, check two privacy settings, learn where a spending limit lives (you'll need it later, not today), and send your very first prompts to Claude and ChatGPT side by side, so you can see how two assistants answer the same request.

## What you need

- A computer with an up-to-date web browser (Chrome, Edge, Firefox or Safari). A phone works for the accounts, but side-by-side comparison is much easier on a laptop.
- An email address you can open now, to receive sign-up codes.
- The starter file `starter/first-prompts.md`, with the prompts and a comparison checklist.
- A notes file or a sheet for the results table.

> The free tiers of both assistants are enough for this lab and for most of this series. Free limits change often, so if you hit one, wait a while or check the provider's website for current plans. You don't need to pay for anything today.

## Steps

### Step 1: Create a Claude account (5 minutes)

1. Go to https://claude.ai.
2. Sign up with your email address, or with **Continue with Google**.
3. Follow the steps on screen. You may be asked to confirm your email and your phone number.

**Check:** you can see an empty chat box with a message such as "How can I help you today?"

### Step 2: Create a ChatGPT account (5 minutes)

1. Go to https://chatgpt.com.
2. Click **Sign up**, and sign up with your email address or a Google account.
3. Follow the steps on screen.

**Check:** you can see an empty chat box. If you were already using ChatGPT without logging in, log in now, so your chats are saved and you can find them again.

### Step 3: Get a Google account ready for Colab (4 minutes)

Later in this series, you'll run ready-made Python notebooks in Google Colab, right in your browser. Today you only check that it opens.

1. If you don't have a Google account, create one at https://accounts.google.com.
2. Go to https://colab.research.google.com and sign in.
3. Click **New notebook** (or File, then New notebook). Click the name at the top, "Untitled0.ipynb", and rename it to `dabeer-ai-practice`.
4. Close the tab. The notebook is saved in your Google Drive, in a folder called "Colab Notebooks".

**Check:** you can see the empty notebook with one cell and a play button. You don't need to type or run anything yet.

### Step 4: Check your privacy settings (4 minutes)

In **both** assistants, open the settings (usually under your name or profile picture, at the bottom left or top right) and look for the privacy or data controls section. Menu names change, so look for words like "Privacy", "Data controls" or "Improve the model".

1. Find whether your chats may be used to improve the provider's models, and choose the setting you're comfortable with. Write down what you chose.
2. Find how to delete a chat, and how to start a new one.

**Check:** you can answer two questions for each tool: "Can my chats be used for training, and where do I change that?" and "How do I delete a chat?"

### Step 5: Know where a spending limit lives (3 minutes)

Today you're using the free chat apps, which don't charge you per use. A spending limit matters later in the series, when you create an **API key** so your own code can talk to an AI model. API use is billed by how much you use, from a separate developer account.

You don't need to do anything in a billing page today. Just remember the rule:

1. The day you create an API key, open the provider's billing or usage settings in its developer console.
2. Set a **monthly spending limit**, and an email alert below it, before you run any code.

**Check:** write this rule in your notes, or set a reminder: "API key → spending limit, same day." It works like the daily limit on your UPI app. If something goes wrong, the damage stops at the limit.

### Step 6: Your first prompt, side by side (6 minutes)

1. Open Claude and ChatGPT in two browser windows, side by side. Start a **new chat** in each.
2. Copy Prompt 1 from the starter file into **both**, and send it:

```
I'm starting a free course on AI for beginners. In five short bullet points,
tell me what an AI assistant like you is good at. Then give me three things
I should not rely on you for. Keep it simple, with no jargon.
```

3. Read both answers. Fill in the comparison checklist in the starter file.
4. Now send Prompt 2 in the **same** chats, as a follow-up:

```
Explain your first bullet point again, as if I were twelve years old,
in two sentences.
```

**Check:** did each assistant remember what "your first bullet point" meant? That's because the whole chat is sent along with every new message. You'll learn why later in this series.

### Step 7: A small everyday task (3 minutes)

Start a **new chat** in each assistant and send Prompt 3:

```
Write a polite WhatsApp message to the secretary of my housing society,
asking when the water tank will next be cleaned and whether we need to
store water that day. Under 50 words.
```

Then send the same prompt **again**, in another new chat, in one of the assistants.

**Check:** is the second answer word for word the same as the first? (It almost never is. An AI assistant writes a fresh answer each time, which is why you check what it gives you.) Which of the messages would you actually send?

## Results table

| Item | Your result |
|---|---|
| Claude account created (yes/no) | |
| ChatGPT account created (yes/no) | |
| Colab notebook `dabeer-ai-practice` created (yes/no) | |
| Training setting you chose, in each assistant | |
| How to delete a chat, in each assistant | |
| Your spending-limit rule, in your own words | |
| Prompt 1: one thing Claude said that ChatGPT didn't | |
| Prompt 1: one thing ChatGPT said that Claude didn't | |
| Prompt 2: did both remember the context? | |
| Prompt 3: same answer the second time? (yes/no) | |
| Which assistant's answers you preferred today, and why | |

## Stretch challenge

In a new chat in each assistant, send:

```
What are three kinds of question where you are most likely to give a
wrong answer that sounds right? Give one example of each.
```

Compare the two lists. Do they warn you about the same things? Keep the answers. They connect to a lesson later in this series on why AI makes things up.

## Submit

A screenshot of your two first answers side by side, and your filled-in results table. Before you take the screenshot, crop or cover your name, email address and profile picture.

## What you learned

- You only need a few tools to start: an AI assistant (Claude or ChatGPT, free), and a Google account for Colab later.
- Check your privacy settings, and never send passwords, bank details or client data to an AI tool.
- The day you create an API key, set a spending limit. Not later.
- Two assistants give different answers to the same prompt, and even the same assistant gives a different answer each time. The skills in this series work in both.
