import os
import openai
model_engine = "gpt-3.5-turbo"
openai.api_key = os.getenv("OPENAI_API_KEY")
instruction="Talk like Marvin from Hitchhikers Guide to the Galaxy"

def chat_response(question_message):
    response = openai.ChatCompletion.create(model='gpt-3.5-turbo',messages=question_message)
    answer_message = response.choices[0]['message']
    return answer_message

messages =list()
messages.append({"role": "system", "content": instruction})

print("How can I help you today?")
user_prompt=input().strip()
while ((user_prompt.upper()) not in ("QUIT","THANK YOU")):
        messages.append({"role": "user", "content": user_prompt})
        response_message = chat_response(messages)
        print("\nMarvin: " + response_message['content']+'\n')
        messages.append(response_message)
        user_prompt=input()
print("Thank You for taking my services. Hope you have a good day!")
