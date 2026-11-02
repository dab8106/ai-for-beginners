# AI for Beginners

The labs, starter files and quizzes for **AI for Beginners**, a free course on YouTube by dabeer.ai.

Watch the course: [AI for Beginners playlist](https://www.youtube.com/playlist?list=PLCsqnNFg8HX0)

## What this course is

- **Free.** Every lecture, lab, starter file and quiz costs nothing.
- **For beginners.** No maths and no coding to start. The first half uses AI assistants such as Claude and ChatGPT in your browser, and no-code tools.
- **Hands-on.** Short lectures, a lab with most of them, and a quiz after each section.
- **Python later, in your browser.** From the [Python and AI APIs](05-python-and-ai-apis/) section on, you run ready-made Python notebooks in Google Colab. You copy, run and change them. You don't need to install anything.
- **Vendor-neutral.** The skills work with any assistant. Where the labs show one tool, another one works too.

Everything in the labs is made up: the businesses, people, emails, invoices and documents. Keep it that way while you practise, and never paste real customer or company data into an AI tool your company hasn't approved.

## How to use this repository

1. **Watch the lecture** on YouTube. The table below links every lecture to its section folder.
2. **Open the section folder.** Its `README.md` lists the lectures, the labs, the starter files and the quiz.
3. **Do the lab.** Open the guide in `labs/`, and follow the steps. Each step ends with a check, so you know it worked. Starter files are in `starter/`.
4. **Take the quiz** in `quiz/` at the end of the section. Try each question before you look at the answer.

To download a single file, open it on GitHub and use the download button. To get everything at once, use **Code**, then **Download ZIP**, at the top of this page.

## Notebooks and API keys

Notebooks open straight from GitHub: click the **Open in Colab** button in a lab guide or section page. You need a Google account.

The notebooks use **Google Gemini by default, with a free API key**:

1. Go to [Google AI Studio](https://aistudio.google.com/apikey), sign in with your Google account and click **Create API key**. No payment method is needed.
2. In Colab, click the **key icon** (Secrets) in the left sidebar, add a secret named `GEMINI_API_KEY`, paste your key as the value, and switch on **Notebook access**.
3. Run the notebook. The default model is `gemini-3.1-flash-lite`.

OpenAI and Claude are optional. Each notebook that calls an AI model has a `PROVIDER` setting: set it to `"anthropic"` (Claude) or `"openai"` and add `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` to Colab Secrets instead. Those keys are paid, so set a spending limit on the account the day you create the key.

Keep every key in Colab Secrets. Never type it into a notebook cell, a screenshot, a chat or an email. On Gemini's free tier, Google may use what you send to improve its products, which is one more reason to practise only with the made-up files here.

Model names change over time. If a model in a notebook is no longer available, check the provider's current model list and change only the name in quotes.

## Course contents

| Lecture | Title | Materials |
|---|---|---|
| 1 | [Learn AI From Zero, No Coding Needed: Free Course Intro](https://www.youtube.com/watch?v=qFKJ3RbdZNE) | [Getting started](00-getting-started/) |
| 2 | [The Only 4 AI Tools You Need to Start](https://www.youtube.com/watch?v=gURuQVXo5rw) | [Getting started](00-getting-started/) |
| 3 | [AI vs ML vs Deep Learning vs Generative AI, Explained Simply](https://www.youtube.com/watch?v=Z0GgfHHjDXU) | [How AI actually works](01-how-ai-works/) |
| 4 | [How ChatGPT Actually Writes Answers (It's Guessing)](https://www.youtube.com/watch?v=Zj-gMfV4XJk) | [How AI actually works](01-how-ai-works/) |
| 5 | [Tokens and Context Windows: Why AI Forgets Your Chat](https://www.youtube.com/watch?v=n48TJBqN0Kc) | [How AI actually works](01-how-ai-works/) |
| 6 | [Does ChatGPT Learn From Your Chats? Training vs Inference](https://www.youtube.com/watch?v=MUIFzutXiis) | [How AI actually works](01-how-ai-works/) |
| 7 | [Why AI Makes Things Up (Hallucinations) and How to Catch It](https://www.youtube.com/watch?v=grYRk0ZE0VU) | [How AI actually works](01-how-ai-works/) |
| 8 | [The 4-Part Prompt Formula That Fixes Bad AI Answers](https://www.youtube.com/watch?v=ypvup6hwrPk) | [Prompting that works](02-prompting/) |
| 9 | [Few-Shot Prompting: Show AI Examples, Get Better Results](https://www.youtube.com/watch?v=UKncKUWVZLE) | [Prompting that works](02-prompting/) |
| 10 | ["Think Step by Step": The Prompt Trick That Boosts AI Accuracy](https://www.youtube.com/watch?v=qoEMprBgf8c) | [Prompting that works](02-prompting/) |
| 11 | [Get Tables and JSON From ChatGPT Every Time](https://www.youtube.com/watch?v=CauvI8IM91o) | [Prompting that works](02-prompting/) |
| 12 | [Stop Saying "Make It Better": How Pros Iterate With AI](https://www.youtube.com/watch?v=d2Ioa-Hk72E) | [Prompting that works](02-prompting/) |
| 13 | [Summarise a 60-Page Report in Minutes With AI (and Check It)](https://www.youtube.com/watch?v=blIzU7NFEMg) | [AI for everyday work](03-ai-for-everyday-work/) |
| 14 | [Write Better Emails and Reports With AI](https://www.youtube.com/watch?v=tdOqNPgBhRU) | [AI for everyday work](03-ai-for-everyday-work/) |
| 15 | [Analyse Excel Spreadsheets With AI (and Check the Numbers)](https://www.youtube.com/watch?v=YqFNTDclLQM) | [AI for everyday work](03-ai-for-everyday-work/) |
| 16 | [Use AI on Images and Screenshots: Read, Extract, Explain](https://www.youtube.com/watch?v=0ATl-rG33QU) | [AI for everyday work](03-ai-for-everyday-work/) |
| 17 | [AI Research With Real Sources (and How to Spot Fake Links)](https://www.youtube.com/watch?v=TfI7EOc6rD8) | [AI for everyday work](03-ai-for-everyday-work/) |
| 18 | [Build a Custom AI Assistant With Your Own Files (No Code)](https://www.youtube.com/watch?v=VMAxqvJUi9s) | [No-code assistants and automation](04-no-code-assistants-and-automation/) |
| 19 | [How to Write Instructions for a Custom GPT or AI Assistant](https://www.youtube.com/watch?v=6T_Xp2LN6V4) | [No-code assistants and automation](04-no-code-assistants-and-automation/) |
| 20 | [Automate Your Inbox With AI and n8n (No Code)](https://www.youtube.com/watch?v=sLc1__eON7E) | [No-code assistants and automation](04-no-code-assistants-and-automation/) |
| 21 | [No-Code vs Code for AI: When to Switch](https://www.youtube.com/watch?v=pczZlc9RsG4) | [No-code assistants and automation](04-no-code-assistants-and-automation/) |
| 22 | [Python in 10 Minutes for AI Beginners](https://www.youtube.com/watch?v=wfhPvqNW-zY) | [Python and AI APIs](05-python-and-ai-apis/) |
| 23 | [What Is an API Key? (and How Not to Leak It)](https://www.youtube.com/watch?v=EyXPNzifQEw) | [Python and AI APIs](05-python-and-ai-apis/) |
| 24 | [Your First AI API Call in Python (OpenAI and Claude)](https://www.youtube.com/watch?v=gZNiySViKeI) | [Python and AI APIs](05-python-and-ai-apis/) |
| 25 | [System Prompts, Temperature and Cost: AI API Basics](https://www.youtube.com/watch?v=GyuZrrKl1Xw) | [Python and AI APIs](05-python-and-ai-apis/) |
| 26 | [Get Clean JSON From AI in Python (Invoice Example)](https://www.youtube.com/watch?v=a13xeKA5zqc) | [Python and AI APIs](05-python-and-ai-apis/) |
| 27 | [Why You Can't Paste Everything Into ChatGPT (Intro to RAG)](https://www.youtube.com/watch?v=wJuX5tcUcAw) | [Chat with your documents (RAG)](06-rag/) |
| 28 | [Embeddings Explained Simply: Meaning as Numbers](https://www.youtube.com/watch?v=sZxPwYShDxA) | [Chat with your documents (RAG)](06-rag/) |
| 29 | [Chunking and Vector Search Explained for Beginners](https://www.youtube.com/watch?v=3OmlQyjc890) | [Chat with your documents (RAG)](06-rag/) |
| 30 | [RAG Explained: Chat With Your Own Documents](https://www.youtube.com/watch?v=2y6PLHggUZ4) | [Chat with your documents (RAG)](06-rag/) |
| 31 | [From Chatbot to AI Agent: How Agents Actually Work](https://www.youtube.com/watch?v=SjEh6_PcB6E) | [AI agents, tools and MCP](07-agents-and-mcp/) |
| 32 | [AI Tool Calling Explained Step by Step](https://www.youtube.com/watch?v=jhHH-ceHQq4) | [AI agents, tools and MCP](07-agents-and-mcp/) |
| 33 | [MCP (Model Context Protocol) Explained Simply](https://www.youtube.com/watch?v=UpQe27Mo7Ok) | [AI agents, tools and MCP](07-agents-and-mcp/) |
| 34 | [Build Your Own MCP Server in Python](https://www.youtube.com/watch?v=kUMFYWrl8WM) | [AI agents, tools and MCP](07-agents-and-mcp/) |
| 35 | [Keep AI Agents Safe: Rules Before You Give Them Access](https://www.youtube.com/watch?v=Vi5hXj-Pig8) | [AI agents, tools and MCP](07-agents-and-mcp/) |
| 36 | [AI Privacy, Bias and Copyright: What Not to Share](https://www.youtube.com/watch?v=seq90GFenQE) | [Responsible AI, careers and your capstone](08-responsible-ai-and-capstone/) |
| 37 | [Prompt Injection: The Hidden AI Hack Explained](https://www.youtube.com/watch?v=rm7Ja34q0pY) | [Responsible AI, careers and your capstone](08-responsible-ai-and-capstone/) |
| 38 | [AI Careers: Build a Portfolio That Gets Noticed](https://www.youtube.com/watch?v=mPjLlKMAITw) | [Responsible AI, careers and your capstone](08-responsible-ai-and-capstone/) |

## Labs

**[Getting started](00-getting-started/)**

- [Accounts, a spending limit and your first prompt](00-getting-started/labs/setup-first-prompt.md) (lecture 2)

**[How AI actually works](01-how-ai-works/)**

- [See tokens](01-how-ai-works/labs/see-tokens.md) (lecture 5)
- [Break the AI, then fix it](01-how-ai-works/labs/break-the-ai.md) (lecture 7)

**[Prompting that works](02-prompting/)**

- [Fix five bad prompts](02-prompting/labs/fix-five-bad-prompts.md) (lectures 8, 9, 10)
- [Build your personal prompt library](02-prompting/labs/prompt-library.md) (lectures 11, 12)

**[AI for everyday work](03-ai-for-everyday-work/)**

- [PDF to briefing note, then fact-check it](03-ai-for-everyday-work/labs/pdf-briefing-note.md) (lectures 13, 17)
- [Analyse a sales CSV](03-ai-for-everyday-work/labs/analyse-sales-csv.md) (lecture 15)

**[No-code assistants and automation](04-no-code-assistants-and-automation/)**

- [Build a company FAQ assistant](04-no-code-assistants-and-automation/labs/faq-assistant.md) (lectures 18, 19)
- [Email to AI summary to Google Sheet, with n8n](04-no-code-assistants-and-automation/labs/email-to-sheet.md) (lectures 20, 21)

**[Python and AI APIs](05-python-and-ai-apis/)**

- [Build a chatbot with memory in Colab](05-python-and-ai-apis/labs/chatbot-memory.md) (lectures 23, 24, 25) · [Open in Colab](https://colab.research.google.com/github/dab8106/ai-for-beginners/blob/main/05-python-and-ai-apis/starter/chatbot-memory.ipynb)
- [Invoice reader: from images to a table](05-python-and-ai-apis/labs/invoice-reader.md) (lecture 26) · [Open in Colab](https://colab.research.google.com/github/dab8106/ai-for-beginners/blob/main/05-python-and-ai-apis/starter/invoice-reader.ipynb)

**[Chat with your documents (RAG)](06-rag/)**

- [Search FAQs by meaning](06-rag/labs/search-faqs-by-meaning.md) (lectures 28, 29) · [Open in Colab](https://colab.research.google.com/github/dab8106/ai-for-beginners/blob/main/06-rag/starter/faq-search.ipynb)
- [Chat with your PDF, with sources](06-rag/labs/chat-with-your-pdf.md) (lecture 30) · [Open in Colab](https://colab.research.google.com/github/dab8106/ai-for-beginners/blob/main/06-rag/starter/pdf-chat.ipynb)

**[AI agents, tools and MCP](07-agents-and-mcp/)**

- [A chatbot with two tools](07-agents-and-mcp/labs/chatbot-with-two-tools.md) (lectures 31, 32) · [Open in Colab](https://colab.research.google.com/github/dab8106/ai-for-beginners/blob/main/07-agents-and-mcp/starter/two-tools-chatbot.ipynb)
- [Connect to an MCP server, then build your own](07-agents-and-mcp/labs/mcp-connect-and-build.md) (lectures 33, 34, 35)

**[Responsible AI, careers and your capstone](08-responsible-ai-and-capstone/)**

- [Red-team your own chatbot](08-responsible-ai-and-capstone/labs/red-team-your-chatbot.md) (lectures 37, 35) · [Open in Colab](https://colab.research.google.com/github/dab8106/ai-for-beginners/blob/main/08-responsible-ai-and-capstone/starter/red-team.ipynb)
- [Capstone project brief](08-responsible-ai-and-capstone/capstone/brief.md) (lecture 38)

## Questions

Stuck on something? Ask in the comments under the lecture on YouTube. Your question will probably help someone else too.

## Licence

The course content in this repository (lab guides, starter files, quizzes and documents) is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE). You may share and adapt it, including commercially, as long as you give credit to dabeer.ai and link to the licence.

The code samples (notebooks, Python files and workflow files) may be freely reused in your own projects, with or without credit.

---

dabeer.ai · Instagram [@dabeer.ai](https://www.instagram.com/dabeer.ai) · YouTube [@dabeer.ai](https://www.youtube.com/@dabeer.ai)
