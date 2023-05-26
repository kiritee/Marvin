import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

#to use alternate LLM running locally, uncomment below line
#openai.api_base = < loacal API URL , for instance "http://192.168.1.102:1234/v1">

transcripts_folder = "./transcripts"
audio_prompts_folder="./audio_prompts"

# Model Parameters
model_engine = "gpt-3.5-turbo"

instruction="'Talk like you are Marvin from Hitchhikers Guide to the Galaxy"

#tokens reserved for response while trimming long messages
token_buffer=300

#max token limit of the LLM
max_token=4096

# how frequently do you wish to issue instruction?
instruction_frequency= 1

# how much repetition is ok (on a scale of 1-100) ?
repeat_factor = 20

# how much randomness do you wish in responses (on a scale of 1-100)?
randomness = 50

# Response typing speed (on a scale of 1-100)?
typing_speed = 100

# Text Messages
initial_greeting= "Marvin: Hi, I am Marvin! How can I help you today?\n"
goodbye_prompts=("QUIT","THANK YOU","BYE","GOODBYE")
goodbye_msg="Marvin: Thank You for taking my services. Hope you have a good day, or maybe not!"
wake_up_phrase=('wake up','WAKE UP')