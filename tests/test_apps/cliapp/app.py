from flask import Flask, request
import openai

app = Flask(__name__)
openai.api_key = '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'

messages = []
while True:
    content = input("User:")
    messages.append({"role":"user","content":content})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    chat_response = completion.choices[0].message.content
    print(f'ChatGPT: {chat_response}')
    messages.append({"role":"assistant", "content":chat_response})
