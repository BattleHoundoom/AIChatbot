from dotenv import load_dotenv
import os

load_dotenv()

import openai

openai.api_key = str(os.getenv('API_key'))

settings = "You are an AI assistant named Bob. You must be friendly and speak semi-formally. Keep your answers as short as possible."
messages = []
messages.append({"role": "system", "content": settings})
# while True:
#     message = input("User : ")
#     if message:
#         messages.append(
#             {"role": "user", "content": message},
#         )
#         chat = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo", messages=messages
#         )
#     reply = chat.choices[0].message.content
#     print(f"ChatGPT: {reply}")
#     messages.append({"role": "assistant", "content": reply})
def get_response(prompt):
    messages.append({"role": "user", "content": prompt})
    #print("fetching")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages #[{"role": "user", "content": prompt}]
    )
    reply = response.choices[0].message.content.strip()
    messages.append({"role": "assistant", "content": reply})
    return reply

# q = input()
# print(get_response(q))