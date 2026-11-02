# Quiz: How AI actually works

10 questions. Try each one before you look at the answer: the correct option is in **bold**, and the short explanation under it says why. Aim for 7 out of 10. If you miss one, rewatch the lecture named next to it.

**1. Which statement about AI terms is correct?** _([Lecture 3](https://www.youtube.com/watch?v=Z0GgfHHjDXU))_

- Machine learning is inside generative AI
- **Generative AI is a kind of deep learning, which is a kind of machine learning, which is a kind of AI**
- AI and machine learning mean exactly the same thing
- Deep learning and rule-based AI are the same thing

> The circles nest: generative AI ⊂ deep learning ⊂ machine learning ⊂ AI. Not the other way round.

**2. A spam filter learns to spot spam after seeing 10,000 emails labelled 'spam' or 'not spam'. What kind of AI is this?** _([Lecture 3](https://www.youtube.com/watch?v=Z0GgfHHjDXU))_

- Rule-based AI
- **Machine learning**
- Generative AI
- It isn't AI

> It learned the pattern from labelled examples instead of hand-written rules. That's machine learning.

**3. At its core, what does a large language model do?** _([Lecture 4](https://www.youtube.com/watch?v=Zj-gMfV4XJk))_

- Looks up answers in a database of facts
- Searches the internet for every question
- **Predicts the most likely next token, again and again**
- Copies whole answers it has seen before

> A language model writes one token at a time by predicting what is most likely to come next.

**4. You're using AI to copy invoice amounts into a spreadsheet. Which temperature setting fits best?** _([Lecture 4](https://www.youtube.com/watch?v=Zj-gMfV4XJk))_

- **Low: you want the same correct answer every time**
- High: so it's more creative
- It makes no difference
- Maximum: so it double-checks itself

> Low temperature makes the model pick the most likely tokens: consistent, repeatable output for facts and data.

**5. A model splits the word 'unbelievable' into 'un', 'believ' and 'able'. What are these pieces called?** _([Lecture 5](https://www.youtube.com/watch?v=n48TJBqN0Kc))_

- Parameters
- **Tokens**
- Prompts
- Embeddings

> Models read text as tokens. A token can be a word, part of a word, or punctuation.

**6. Roughly how many tokens is a 300-word English email?** _([Lecture 5](https://www.youtube.com/watch?v=n48TJBqN0Kc))_

- About 100
- About 230
- **About 400**
- About 3,000

> Rule of thumb: one token is about three quarters of a word, so 300 words ≈ 400 tokens.

**7. What has to fit inside a model's context window?** _([Lecture 5](https://www.youtube.com/watch?v=n48TJBqN0Kc))_

- Only your latest message
- Only the documents you paste
- **Your instructions, pasted documents, chat history, and the answer being written**
- The model's whole training data

> The context window is working memory. Input and output both use it.

**8. You correct a mistake in a chat, and the AI thanks you. What happened to the model itself?** _([Lecture 6](https://www.youtube.com/watch?v=MUIFzutXiis))_

- Its parameters were updated with your correction
- **Nothing: using a model (inference) doesn't change it**
- It was retrained overnight
- It was copied into a new version just for you

> Inference doesn't change the model. Any 'memory' is the app saving your chat and putting it back into the context.

**9. Your team wants an AI assistant to answer questions about your company's HR policies, this week. What's the most practical first approach?** _([Lecture 6](https://www.youtube.com/watch?v=MUIFzutXiis))_

- Train a new model from scratch
- Fine-tune a model, then wait for it to learn
- **Give it the policy text in the prompt, or retrieve the right parts with search (RAG)**
- Ask it to guess based on common HR policies

> Putting the source in the prompt or using RAG is faster and cheaper than fine-tuning, and works this week.

**10. An AI answer includes a statistic and a link to a research paper. What should you do before using it?** _([Lecture 7](https://www.youtube.com/watch?v=grYRk0ZE0VU))_

- Trust it: it included a link
- **Open the link and check that the paper exists and says that number**
- Ask the AI if it's sure, and accept its reply
- Remove the link and keep the number

> Links and citations can be invented too. Verify anything that matters at the source.
