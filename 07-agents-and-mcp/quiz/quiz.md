# Quiz: AI agents, tools and MCP

10 questions. Try each one before you look at the answer: the correct option is in **bold**, and the short explanation under it says why. Aim for 7 out of 10. If you miss one, rewatch the lecture named next to it.

**1. What makes an agent different from a plain chatbot?** _([Lecture 31](https://www.youtube.com/watch?v=SjEh6_PcB6E))_

- It uses a bigger model
- **It has tools and works in a loop: decide, use a tool, look at the result, repeat**
- It always answers faster
- It never makes mistakes

> A model, tools and a loop. A chatbot replies once; an agent keeps going until the job is done or it hits a limit.

**2. An agent tries to book a room, and the tool replies 'that room is already taken'. What should a good agent do?** _([Lecture 31](https://www.youtube.com/watch?v=SjEh6_PcB6E))_

- Stop and report success anyway
- Call the same tool again forever
- Ignore the result
- **Read the result and try another step, like a different room or time**

> Looking at each result and deciding again is the whole point of the loop.

**3. Why should every agent loop have a step limit?** _([Lecture 31](https://www.youtube.com/watch?v=SjEh6_PcB6E))_

- **So it can't run forever, using time and money**
- To make answers shorter
- Because tools only work once
- It's required by the model's licence

> A limit stops runaway loops when the agent gets stuck.

**4. In tool calling, who actually runs the tool?** _([Lecture 32](https://www.youtube.com/watch?v=jhHH-ceHQq4))_

- The language model
- The user
- **Your code (the application)**
- The tool runs itself when the model mentions it

> The model only asks for a tool, with inputs. Your application runs it and sends the result back.

**5. You give the model a tool named 'tool_1' with no description. What's the likely problem?** _([Lecture 32](https://www.youtube.com/watch?v=jhHH-ceHQq4))_

- The tool runs twice
- The tool becomes faster
- **The model can't tell when to use it**
- Nothing: names don't matter

> The model picks tools by reading names and descriptions. Write them for a new colleague.

**6. In MCP, what are the three parts of the architecture?** _([Lecture 33](https://www.youtube.com/watch?v=UpQe27Mo7Ok))_

- **Host, client, server**
- Browser, router, database
- Prompt, token, model
- Agent, tool, loop

> The host is the AI app. Inside it, each client keeps one connection to one server, which wraps a tool or data source.

**7. Your assistant should create a Jira ticket when someone asks. In MCP terms, what is that?** _([Lecture 33](https://www.youtube.com/watch?v=UpQe27Mo7Ok))_

- A resource
- A prompt
- A client
- **A tool**

> It's an action that changes something in the outside world, and the model decides when to call it. That's a tool.

**8. Your local MCP server works, but the app breaks when you add print() lines to debug it. Why?** _([Lecture 34](https://www.youtube.com/watch?v=kUMFYWrl8WM))_

- print() is not allowed in Python 3
- **A local server talks to the app over standard output, so stray prints corrupt the messages**
- The app blocks all text
- print() deletes the tool list

> Send logs to standard error instead, for example with the logging module.

**9. Your MCP server is listed in the app, but the model never uses your tool. What do you check first?** _([Lecture 34](https://www.youtube.com/watch?v=kUMFYWrl8WM))_

- **The tool's description**
- Your internet speed
- The colour theme of the app
- The model's temperature

> A vague description means the model can't tell when the tool fits. Then check the app really lists the tool.

**10. Your agent can read web pages and send emails. Which action should always need a person's approval?** _([Lecture 35](https://www.youtube.com/watch?v=Vi5hXj-Pig8))_

- Reading a web page
- Listing its tools
- **Sending an email**
- Counting words

> Sending leaves your system and can't be undone. Reading is lower risk, though what it reads can still carry an injection.
