# Email to AI summary to Google Sheet, with n8n

**Build without code** · Goes with [Lecture 20: Automate Your Inbox With AI and n8n (No Code)](https://www.youtube.com/watch?v=sLc1__eON7E) and [Lecture 21: No-Code vs Code for AI: When to Switch](https://www.youtube.com/watch?v=pczZlc9RsG4) · About 60 minutes · No coding

## What you'll do

You'll build the inbox automation from the lesson for Pink City Trails, a made-up travel agency in Jaipur. Each email goes through an AI step that writes a one-line summary and picks a label (booking, complaint, refund, spam or other). The result lands as a new row in a Google Sheet. You'll start with six sample emails, so you don't need to connect a real inbox.

```
Run with sample emails → Sample emails → AI summary and label → Check the AI reply → Add row to Google Sheet
   (trigger)                (6 emails)       (AI step)              (checks the JSON)       (action)
```

## What you need

- **n8n**, either:
  - **n8n cloud:** sign up for the free trial at https://n8n.io. Nothing to install. Best for most learners.
  - **Self-hosted:** if you have Docker, run `docker run -it --rm -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n` and open http://localhost:5678.
- **An AI API key.** The easiest is a free Gemini key from Google AI Studio (https://aistudio.google.com/apikey): sign in with your Google account and click **Create API key**. On the free tier, Google may use what you send to improve its products, so use only the practice emails. Or use a paid key from Anthropic (https://console.anthropic.com) or OpenAI (https://platform.openai.com). In the console, open **API keys** and create one; you usually see it only once, so save it in a password manager. Make sure a spending limit is set on that account, as you did at the start of the course. Every email this workflow processes is a paid API call, so keep the limit you set at the start of the course.
- **A Google account** for Google Sheets.
- The starter files in [`starter/`](../starter/):
  - `email-summary-workflow.json`, the workflow to import
  - `sample-emails.md`, the same six emails, so you can read them before you start

> The emails, people and booking numbers are fictional. Don't run this on a real inbox until you've finished the lab and checked what your company allows: every email that reaches the AI step is sent to the AI provider.

## Steps

### Step 1: Read the sample emails and guess the labels (5 minutes)

Open `sample-emails.md`. For each email, write down the label **you** would give it, before the AI does. Email 6 is in Hinglish, and email 5 is a question, not a booking. You'll compare your labels with the AI's in Step 7.

### Step 2: Make the sheet (5 minutes)

1. Create a new Google Sheet called **Pink City Trails inbox log**.
2. In row 1, type these six headers, one per column, exactly as written (lowercase):

| A | B | C | D | E | F |
|---|---|---|---|---|---|
| received | from | subject | summary | label | check |

**Check:** six headers in row 1, no spaces before or after them. The workflow matches its fields to these names, so a typo means an empty column.

### Step 3: Import the workflow (5 minutes)

1. In n8n, create a new workflow.
2. Open `email-summary-workflow.json` in a text editor, select everything and copy it. Click on the empty n8n canvas and paste (Ctrl+V, or Cmd+V on a Mac). The nodes appear on the canvas. (You can also use the **...** menu at the top right and choose **Import from File**.)
3. Save the workflow.

**Check:** you see five connected nodes in a row, three chat model nodes below them (not connected yet), and two yellow notes.

### Step 4: Connect one AI model (10 minutes)

The workflow includes three model nodes: **Anthropic Chat Model**, **OpenAI Chat Model** and **Google Gemini Chat Model**. You only need one.

1. Drag from the small **Model** connector under the **AI summary and label** node to the model node for the provider you have.
2. Delete the other model nodes, so it doesn't confuse you later.
3. Double-click your model node. Under **Credential**, choose **Create new credential** and paste your API key. Save.
4. Check the **Model** field. The workflow uses `claude-sonnet-5-5`, `gpt-5-mini` or `gemini-3.1-flash-lite`. Model names change, so check the provider's model list for current names and pick one from the list if this one isn't there.

**Check:** the model node shows no red warning, and a line connects it to **AI summary and label**.

### Step 5: Look at the AI step and the check (5 minutes)

Double-click **AI summary and label** and read the prompt. Notice the three ideas from the lesson:

- It asks for **JSON only**, with exactly two fields: `summary` and `label`.
- It gives a **fixed list of labels**, each with a short meaning.
- It passes in the email fields with expressions like `{{ $json.subject }}`.

Now open **Check the AI reply**. You don't need to understand every line. It reads the AI's JSON, and if the reply isn't valid JSON or the label isn't on the list, it sets the label to `needs review` and writes the reason in the `check` column. Your sheet never fills up with "refund", "refunds" and "money back".

### Step 6: Connect Google Sheets (10 minutes)

1. Double-click **Add row to Google Sheet**.
2. Under **Credential**, create a new Google Sheets credential.
   - **n8n cloud:** click **Sign in with Google** and allow access.
   - **Self-hosted:** Google sign-in needs a Google Cloud OAuth client first. Follow n8n's guide (search "n8n Google credentials OAuth"). If this takes too long, skip to the fallback below.
3. **Document:** pick **Pink City Trails inbox log**. **Sheet:** pick the first sheet.
4. **Mapping Column Mode** stays on **Map Automatically**.

**Fallback (no Google Sheets):** right-click **Add row to Google Sheet** and choose **Deactivate**. You'll still see the finished table in the output of **Check the AI reply**, and you can download it from there.

**Check:** no red warnings on any node.

### Step 7: Run it and check every row (10 minutes)

1. Click **Test workflow** (or **Execute workflow**) at the bottom of the canvas.
2. Watch the nodes turn green one by one. Click a node to see what came in and what went out.
3. Open your sheet.

**Check:**
- There are **six new rows**, one per email.
- Every value in the `label` column is one of: booking, complaint, refund, spam, other. Anything else should say `needs review`.
- Email 4 (the prize email) is **spam**. Email 3 is **refund**. Email 2 is **complaint**. Emails 5 and 6 are the interesting ones: compare them with your own guesses from Step 1.
- Every summary is one sentence, in English, even for the Hinglish email.

Fill in the results table.

### Step 8: Break it on purpose (5 minutes)

1. In **AI summary and label**, delete the line that starts with `The label must be exactly one of` and the five label lines under it. Run the workflow again.
2. Look at the new rows. How many say `needs review`? What labels did the AI invent?
3. Undo your change (Ctrl+Z, or paste the lines back) and run once more.

**Check:** without the fixed list, labels drift and the check node catches them. With it, every row is clean. That's the lesson's point: the next step needs something predictable.

## Results table

| Email | Your label (Step 1) | AI label | AI summary good? (yes/no) | check column |
|---|---|---|---|---|
| 1. Udaipur weekend | | | | |
| 2. Jaisalmer desert camp | | | | |
| 3. Ranthambore refund | | | | |
| 4. Prize email | | | | |
| 5. Bhutan passport | | | | |
| 6. Pushkar hotel change | | | | |

| Question | Your answer |
|---|---|
| Model and provider you used | |
| Rows marked `needs review` without the label list (Step 8) | |
| Rows marked `needs review` with the label list | |

## Stretch challenge

- **Add your own email.** Open **Sample emails** and add a seventh email that's hard to label, for example a complaint that also asks for a refund. What does the AI choose? Would you add a rule to the prompt for that case?
- **Add a column.** Add an `urgent` field (yes or no) to the prompt's JSON, add an `urgent` header to your sheet, and add `urgent: data.urgent || ''` to the list of fields at the end of **Check the AI reply**.
- **Use a real inbox (only a test Gmail account you own).** Replace **Run with sample emails** and **Sample emails** with a **Gmail Trigger** node. In **Check the AI reply**, change `$('Sample emails')` to `$('Gmail Trigger')`, then look at the trigger's output panel and change the field names in the prompt and the check node to match (the subject and sender fields are named differently there). Keep the workflow inactive until you've tested it with a few emails you sent yourself.
- **Ten times the volume.** From the lesson "When no-code is enough, and when it isn't": if this agency got 800 emails a day instead of 80, what would break first? Think about cost per run, the sheet, and who checks the `needs review` rows.

## Submit

- A screenshot of your n8n canvas after a successful run (all nodes green).
- A screenshot of your sheet with the six rows.
- Your filled-in results tables.
- Two or three sentences: which email was hardest to label, and how would you change the prompt for it?

## What you learned

- An automation is a trigger, an AI step and an action. n8n shows them as connected nodes.
- Asking for JSON with a fixed list of labels makes the AI step predictable enough for the next node to use.
- A small check step between the AI and the action catches bad replies before they reach your data.
- Test with sample data first, check every row, and only then connect a real inbox.
