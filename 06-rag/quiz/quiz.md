# Quiz: Chat with your documents

10 questions. Try each one before you look at the answer: the correct option is in **bold**, and the short explanation under it says why. Aim for 7 out of 10. If you miss one, rewatch the lecture named next to it.

**1. Your company has 2,000 policy documents that change every month. Why not put all of them into every prompt?** _([Lecture 27](https://www.youtube.com/watch?v=wJuX5tcUcAw))_

- Models can't read policy documents
- **It would hit the context limit, cost more on every message, hide details, go out of date, and show people text they shouldn't see**
- Prompts can only contain one document
- It would make the model retrain itself

> Limit, cost, attention, freshness and permissions all get worse when you send everything.

**2. You have one ten-page PDF and a single question about it. What's the simplest good approach?** _([Lecture 27](https://www.youtube.com/watch?v=wJuX5tcUcAw))_

- Build a full RAG system first
- Fine-tune a model on it
- Split it into 500 chunks by hand
- **Add the document to your chat and ask**

> RAG pays off with lots of content, frequent changes, or different permissions. One short PDF fits in the chat.

**3. What is an embedding?** _([Lecture 28](https://www.youtube.com/watch?v=sZxPwYShDxA))_

- **A list of numbers that represents the meaning of a piece of text**
- A summary of a text, written by AI
- A password that protects a document
- A picture of the text

> An embedding places text on a 'map of meaning'. Similar meanings get similar numbers.

**4. Which two sentences should sit closest together on the meaning map?** _([Lecture 28](https://www.youtube.com/watch?v=sZxPwYShDxA))_

- 'Cancel my subscription' and 'Subscribe to the newsletter'
- 'Subscribe to the newsletter' and 'Stop my monthly plan'
- **'Cancel my subscription' and 'Stop my monthly plan'**
- All three are equally close

> Same intent, different words. Sharing the word 'subscribe' doesn't make the meaning similar.

**5. You embedded your FAQs with one model. Can you embed questions with a different embedding model and compare them?** _([Lecture 28](https://www.youtube.com/watch?v=sZxPwYShDxA))_

- Yes, all embeddings are compatible
- Only if both models are from the same company
- **No: use the same model for documents and questions**
- Only for short questions

> Each model creates its own map. Numbers from different models can't be compared.

**6. Why split documents into chunks instead of making one embedding per whole document?** _([Lecture 29](https://www.youtube.com/watch?v=3OmlQyjc890))_

- **One embedding for a long document blurs many topics together, so search can't find the exact part**
- Chunks are cheaper to print
- Embedding models refuse documents over one page
- Chunks remove the need for a language model

> Like one pin for a whole city: you know the city, not the street. Smaller chunks have a sharper meaning.

**7. What should you store with every chunk, so you can show sources later?** _([Lecture 29](https://www.youtube.com/watch?v=3OmlQyjc890))_

- The author's phone number
- A random ID only
- Nothing: the model remembers where it came from
- **Its source label: file, page or section**

> Without the file and page, nobody can check the answer.

**8. Meaning search keeps missing exact codes like invoice number INV-20931. What helps most?** _([Lecture 29](https://www.youtube.com/watch?v=3OmlQyjc890))_

- Make the chunks bigger
- **Hybrid search: combine meaning search with keyword search**
- Remove numbers from the documents
- Use a higher temperature

> Keyword search is good at exact matches; meaning search is good at reworded questions. Hybrid uses both.

**9. What are the three steps of RAG, in order?** _([Lecture 30](https://www.youtube.com/watch?v=2y6PLHggUZ4))_

- **Retrieve, augment, generate**
- Generate, retrieve, train
- Augment, train, answer
- Search, delete, rewrite

> Retrieve the relevant chunks, augment the prompt with them, and generate the answer.

**10. Your RAG bot gives a wrong answer, and the source it shows doesn't mention the topic at all. Where do you look first?** _([Lecture 30](https://www.youtube.com/watch?v=2y6PLHggUZ4))_

- The model's temperature
- The font of the PDF
- **Retrieval: the right chunk never reached the model**
- The length of the answer

> If the right chunk isn't retrieved, no prompt can fix it. Check retrieval first, then the documents, then the prompt.
