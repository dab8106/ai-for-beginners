# A chatbot with two tools

**AI agents, tools and MCP** · Goes with [Lecture 31: From Chatbot to AI Agent: How Agents Actually Work](https://www.youtube.com/watch?v=SjEh6_PcB6E) and [Lecture 32: AI Tool Calling Explained Step by Step](https://www.youtube.com/watch?v=jhHH-ceHQq4) · About 45 minutes · Python in Colab, API key needed

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dab8106/ai-for-beginners/blob/main/07-agents-and-mcp/starter/two-tools-chatbot.ipynb)

## What you'll do

You'll give a model two tools, a weather lookup and a currency calculator, and watch the tool-call loop happen one step at a time: the model asks for a tool, your code runs it, the result goes back, and the model answers. You'll run the same loop with both Claude and an OpenAI model, and see how tool descriptions and input checks change the result.

## What you need

- A Google account, to open Google Colab: https://colab.research.google.com
- An API key. The easiest is a **free Gemini API key** from Google AI Studio (https://aistudio.google.com/apikey): no payment method needed, but it has rate limits, and on the free tier Google may use what you send to improve its products, so stick to the practice data here. Anthropic and OpenAI keys work too, from the lesson "What an API Is, and Your API Key", with your spending limit switched on. One key is enough for the main lab; a second provider's key is for Step 7.
- The starter notebook `starter/two-tools-chatbot.ipynb`, in this section's [`starter/`](../starter/) folder.

> Both tools use **made-up practice data**. The weather and the exchange rates are not real, so don't plan a trip with them.

## Steps

### Step 1: Open the notebook and add your key

1. Click the **Open in Colab** button at the top of this guide. (Or download the notebook from the [`starter/`](../starter/) folder, and in Colab choose **File**, then **Upload notebook**.)
2. Open **Secrets** (key icon) in the left sidebar, add `GEMINI_API_KEY`, `ANTHROPIC_API_KEY` or `OPENAI_API_KEY`, and switch on **Notebook access**.
3. In the **Settings** cell, set `PROVIDER` to the provider you have a key for (`"gemini"` is the default). Run the install, Settings and API key cells.

**Check:** it prints `Ready: gemini` (or `anthropic`, or `openai`), and no key appears in any cell.

### Step 2: Run the tools without AI

Run the cell with `get_weather` and `convert_currency`. These are normal Python functions: the "kitchen" from the lesson.

**Check:** you see Delhi at 31 degrees, `100 USD` as `8500.0` rupees, and `5000 INR` as `217.39` dirhams. No model was involved.

### Step 3: Read the "menu"

Run the cell that describes the tools. Read each tool's **name**, **description** and **parameters**.

**Check:** you can answer two questions. Which tool would the model pick for "Will it rain in Mumbai?" Which parameters does `convert_currency` need? (`amount`, `from_currency`, `to_currency`.)

### Step 4: Watch the loop

Run the tool-call loop cell. It asks `What's the weather in Delhi right now?`

**Check:** you see a line `step 1  MODEL ASKS: get_weather({'city': 'Delhi'})`, then `OUR CODE RETURNS: ...`, then a final `ANSWER:` in plain words that mentions 31 degrees. The model asked; your code ran the tool.

### Step 5: Watch the model choose

Run the four cells in Step 7 of the notebook one at a time, and fill in the results table.

**Check:**

- The dollars question calls `convert_currency` once (about 21,250 rupees at the practice rate).
- The Karnataka question calls **no tool**. The model already knows the answer.
- The Mumbai-to-Dubai question needs **both** tools. Some models ask for both in one step, others take two steps. Either is fine.
- The Shimla question gets an error back from your code, because Shimla isn't in the data. A good answer says it doesn't have data for Shimla, instead of making up a temperature.

### Step 6: Break a description

In the tools cell, change the `get_weather` description to just `"Tool one."`, and change its name to `"tool_1"` in **both** `TOOLS` and `TOOL_FUNCTIONS`. Run that cell, then ask the Delhi weather question again.

**Check:** note whether the model still picks the tool, and whether it hesitates or asks you what the tool does. Then put the original name and description back and run the cell again.

### Step 7: Same question, other provider

Add a second provider's key to Secrets, set `OTHER` to that provider in the "other provider" cell, and run it.

**Check:** the same tool is called with the same inputs. The answer wording differs, and the code wrapper differs (Gemini uses `function_call` parts, Anthropic uses `tool_use` blocks, OpenAI uses `tool_calls`), but the loop is the same idea.

### Step 8: Test your input checks

Your code, not the model, decides what actually runs. In a new cell, call the function directly with bad inputs:

```python
print(convert_currency("lots", "USD", "INR"))
print(convert_currency(-50, "USD", "INR"))
print(convert_currency(100, "BTC", "INR"))
```

**Check:** each one returns a clear `error` instead of crashing or returning a wrong number. Then ask the chatbot `Convert 100 bitcoin to rupees` and see how the model handles that error.

### Step 9: Chat with memory

Run the last cell, and have a short conversation. Try `How much is 500 euros in rupees?` and then `And in pounds?`. Type `quit` to stop.

**Check:** the follow-up works, because the chat keeps the last few turns.

## Results table

| Question | Tools called, in order | Steps taken | Answer correct, given the practice data? |
|---|---|---|---|
| Weather in Delhi | | | |
| 250 US dollars in rupees | | | |
| Capital of Karnataka | | | |
| Mumbai to Dubai with 40,000 rupees | | | |
| Weather in Shimla | | | |
| Delhi weather with "Tool one." as the description | | | |
| Same dollars question, other provider | | | |
| 100 bitcoin to rupees | | | |

## Stretch challenge

1. **Add a third tool.** Write `get_train_status(train_number)` with made-up data for three trains, add it to `TOOLS` and `TOOL_FUNCTIONS`, and ask a question that needs it.
2. **Hit the limit.** Set `MAX_STEPS = 1` and ask the Mumbai-to-Dubai question. What happens, and why is a step limit important?
3. **Ask before acting.** Add `input("Run this tool? (y/n) ")` before `run_tool` in the loop, so a person approves each call. That's human in the loop, from the lesson "Keeping Agents Safe".

## Submit

The filled-in results table, a screenshot of the printed loop for the Mumbai-to-Dubai question, and two sentences on what happened when you broke the tool description.

## What you learned

- An agent is a model in a loop with tools: it decides, asks for a tool, looks at the result, and repeats.
- The model only **asks** for a tool. Your code runs it, so your code must check the inputs.
- Clear tool names and descriptions are how the model knows which tool fits.
- All three providers use the same loop; only the message format differs.
