# Quiz: Python and AI APIs

10 questions. Try each one before you look at the answer: the correct option is in **bold**, and the short explanation under it says why. Aim for 7 out of 10. If you miss one, rewatch the lecture named next to it.

**1. In Python, what does a pair of curly brackets like {"name": "Asha", "city": "Mumbai"} make?** _([Lecture 22](https://www.youtube.com/watch?v=wfhPvqNW-zY))_

- A list
- A function
- **A dictionary: pairs of keys and values**
- A loop

> Curly brackets make a dictionary. Every message you send to a model is a small dictionary, and a conversation is a list of them.

**2. You see the line model = "some-model-name" and want to try a different model. What do you change?** _([Lecture 22](https://www.youtube.com/watch?v=wfhPvqNW-zY))_

- The word model on the left
- **Only the text inside the quote marks**
- Delete the quote marks
- The equals sign

> The name on the left is the label the rest of the code uses. Change only the value in quotes.

**3. What does your API key do?** _([Lecture 23](https://www.youtube.com/watch?v=EyXPNzifQEw))_

- **It proves who's asking, and who pays**
- It makes the model smarter
- It stores your chat history
- It sets the model's temperature

> The key identifies your account. Whoever holds it can make calls on your bill, so treat it like a password.

**4. You want to share a Colab notebook with a colleague, and your API key is typed into one of its cells. What should you do?** _([Lecture 23](https://www.youtube.com/watch?v=EyXPNzifQEw))_

- Share it, the colleague is trusted
- Blur the key in a screenshot instead
- Change the variable name
- **Move the key into Colab Secrets first; if it was ever shared with the key inside, delete that key and create a new one**

> Keys belong in Colab Secrets or another secrets manager, never in the code. A leaked key should be deleted straight away.

**5. You run your first API call and get an 'authentication failed' error. What's the most likely cause?** _([Lecture 24](https://www.youtube.com/watch?v=gZNiySViKeI))_

- The prompt is too long
- The model is too busy
- **The API key: missing, mistyped, or the notebook has no access to it in Secrets**
- Python is out of date

> Authentication errors are about the key. The rest of the code is probably fine.

**6. In an API call, what is 'messages'?** _([Lecture 24](https://www.youtube.com/watch?v=gZNiySViKeI))_

- A single string of text
- **A list of dictionaries, each with a role and the content**
- The model's name
- The number of tokens allowed

> Messages is a list of dictionaries like {"role": "user", "content": "..."}. A conversation is just a longer list.

**7. Why does the tenth message in a chatbot usually cost more than the first, even when it's just as short?** _([Lecture 25](https://www.youtube.com/watch?v=GyuZrrKl1Xw))_

- Providers charge more later in the day
- The model gets tired
- Longer chats use a bigger model
- **The whole conversation is sent again every turn, so more tokens go in**

> A chatbot's memory is the history your code resends. Message ten carries the nine before it.

**8. You're extracting amounts from invoices. Which temperature fits best?** _([Lecture 25](https://www.youtube.com/watch?v=GyuZrrKl1Xw))_

- **Near zero, for predictable, repeatable output**
- As high as possible, for creativity
- It must always be exactly 1
- Temperature only matters for images

> Keep temperature near zero for facts and data. Note that some models, especially reasoning models, don't accept a temperature setting.

**9. The model returns valid JSON, but the amount says "twelve thousand rupees". Should it pass validation?** _([Lecture 26](https://www.youtube.com/watch?v=a13xeKA5zqc))_

- Yes, the JSON is valid
- **No: check the contents too, and the amount must be a number**
- Yes, if the vendor is correct
- Only if the date is correct

> Valid JSON is only the format. Check the contents too: keys present, numbers are numbers, dates are dates.

**10. A reply still fails your format check after two or three retries. What should your code do?** _([Lecture 26](https://www.youtube.com/watch?v=a13xeKA5zqc))_

- Keep retrying until it works
- Stop the whole run
- **Flag that item for a person to check, and move on to the next one**
- Put the reply into the table anyway

> Retry a few times with feedback, then send failures to a person. Don't let one bad item block the rest or slip into your data.
