#generate user friendly respose using groq api

import os

from groq import Groq
def generator(ans, query):
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Based on the following context:\n\n{'\n\n'.join(ans)}\n\nAnswer this question using only the context above: {query}",
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    return chat_completion.choices[0].message.content