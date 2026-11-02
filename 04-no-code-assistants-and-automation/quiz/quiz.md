# Quiz: Build without code

10 questions. Try each one before you look at the answer: the correct option is in **bold**, and the short explanation under it says why. Aim for 7 out of 10. If you miss one, rewatch the lecture named next to it.

**1. What is a custom assistant, such as a Claude Project or a custom GPT?** _([Lecture 18](https://www.youtube.com/watch?v=VMAxqvJUi9s))_

- A new AI model trained on your company's files
- **A chat you set up once with your own files and instructions, so every conversation starts with that context**
- A browser extension that reads all your emails
- A paid add-on that removes all mistakes

> You don't train anything. You save files and instructions once, and every new chat starts already knowing them.

**2. Your company changes its travel policy, but the assistant still quotes the old daily allowance. What's the best fix?** _([Lecture 18](https://www.youtube.com/watch?v=VMAxqvJUi9s))_

- Ask the assistant to forget the old number
- Add the new policy next to the old one
- **Remove the old file and add the new one, then ask the same question again**
- Switch to a bigger model

> The files are a snapshot. With both versions uploaded, the assistant may quote either one, so replace the old file.

**3. Before you upload company documents to an AI assistant, what should you check first?** _([Lecture 18](https://www.youtube.com/watch?v=VMAxqvJUi9s))_

- That the files are in PDF format
- That the files are shorter than one page
- Nothing: assistants never store files
- **What your company allows, and your account's data settings**

> Uploading shares the content with the provider. Check company rules and data settings before you upload.

**4. Your FAQ assistant answers a question about parental leave, but that topic isn't in any of its files. Which instruction is missing?** _([Lecture 19](https://www.youtube.com/watch?v=6T_Xp2LN6V4))_

- **The boundary: answer only from the files, and say you don't know otherwise**
- The format rule
- The role
- A longer greeting

> Without that boundary, the assistant fills the gap from general knowledge, which may be wrong for your company.

**5. Which of these belongs in an assistant's instructions?** _([Lecture 19](https://www.youtube.com/watch?v=6T_Xp2LN6V4))_

- The admin password for the HR portal
- **Answer only from the attached policy files and name the document you used**
- The salaries of every employee
- Your personal API key

> Instructions guide behaviour but are not a lock. A determined user can sometimes talk past them, so never put secrets in them.

**6. Your assistant gives a wrong answer in testing. What's the best next step?** _([Lecture 19](https://www.youtube.com/watch?v=6T_Xp2LN6V4))_

- Rewrite all the instructions from scratch
- Delete the files and start over
- **Change one instruction, then ask the same test questions again**
- Ignore it if the other answers are fine

> Change one thing at a time, so you know which change fixed it, and retest with the same questions.

**7. In an automation that summarises new emails into a sheet, which part is the trigger?** _([Lecture 20](https://www.youtube.com/watch?v=sLc1__eON7E))_

- **A new email arriving**
- The AI writing a summary
- A new row being added to the sheet
- The spending limit

> The trigger is the event that starts the chain. The AI step reads and decides; the action adds the row.

**8. Your automation runs, but the label column fills up with 'refund', 'refunds' and 'money back'. What should you change?** _([Lecture 20](https://www.youtube.com/watch?v=sLc1__eON7E))_

- Use a different spreadsheet
- Run the automation less often
- Turn off the AI step
- **The prompt: ask for JSON and give a fixed list of allowed labels**

> A fixed list and a fixed JSON shape make the output predictable, so the next node can use it.

**9. You've just built an email automation with an AI step. What should you do before switching it on for the real inbox?** _([Lecture 20](https://www.youtube.com/watch?v=sLc1__eON7E))_

- Nothing, it's ready
- **Test it with a few sample emails, check every row, and check what your company allows**
- Delete the test data
- Remove the spending limit so it never stops

> Test on sample data first. Every real email that reaches the AI step is sent to the provider.

**10. A hospital wants AI to read thousands of patient reports a month, connect to its own record system and keep an audit trail. No-code or code?** _([Lecture 21](https://www.youtube.com/watch?v=pczZlc9RsG4))_

- No-code: drag a few more boxes
- Neither: AI can't read reports
- **Code, built with developers: high volume, sensitive data, a custom system and audit needs**
- No-code, because it's always cheaper

> Volume, sensitive data, custom systems and audit needs are all signs you need code. No-code can still help test the idea first.
