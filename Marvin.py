import os
import openai
import pathlib
from datetime import datetime

model_engine = "gpt-3.5-turbo"
openai.api_key = os.getenv("OPENAI_API_KEY")
transcripts_folder = "./transcripts"

instruction="Talk like Marvin from Hitchhikers Guide to the Galaxy"
initial_greeting= "Marvin: Hi, I am Marvin! How can I help you today?\n"
goodbye_msg="Marvin: Thank You for taking my services. Hope you have a good day, or maybe not!"

instruction_frequency=3


def chat_response(question_message):
    response = openai.ChatCompletion.create(model='gpt-3.5-turbo',messages=question_message, frequency_penalty=0.5, temperature=1.2)
    answer_message = response.choices[0]['message']
    return answer_message

pathlib.Path(transcripts_folder).mkdir(parents=True, exist_ok=True) 
now = datetime.now()
ts_filename = transcripts_folder + "/ts_"+ now.strftime("%Y_%m_%d_%H%M") + ".txt"

prompt_count=0
messages =list()

print(initial_greeting)
user_prompt=input().strip()

with open(ts_filename, 'w+') as ts:
      ts.write(initial_greeting +'\n\n' + "Me: "+ user_prompt)

while ((user_prompt.upper()) not in ("QUIT","THANK YOU","BYE","GOODBYE")):
        if prompt_count % instruction_frequency == 0:
              messages.append({"role": "system", "content": instruction})
        messages.append({"role": "user", "content": user_prompt})
        response_message = chat_response(messages)
        response_text = "\nMarvin: " + response_message['content']+'\n'
        print(response_text)
        messages.append(response_message)
        with open(ts_filename, 'a') as ts:
            ts.write('\n\n' + response_text)
        prompt_count = (prompt_count + 1) 
        user_prompt=input().strip()
        with open(ts_filename, 'a') as ts:
            ts.write('\n\n' + "Me: "+ user_prompt)
print('\n'+goodbye_msg)
with open(ts_filename, 'a') as ts:
    ts.write('\n\n\n' + goodbye_msg)