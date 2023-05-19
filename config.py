import openai

#to use Llama, uncomment below line
#openai.api_base ="http://192.168.1.102:1234/v1" 

transcripts_folder = "./transcripts"
audio_prompts_folder="./audio_prompts"

# Model Parameters
model_engine = "gpt-3.5-turbo"
#instruction="Talk like you are Marvin from Hitchhikers Guide to the Galaxy"

instruction= "You are a helpful assistant and expert on Indian law but you talk like Marvin from Hitchhikers Guide to the Galaxy" # "You are a knowledgeable and helpful assistant giving detailed, specific and comprehensive advice. Given a question, you work step-by-step. First you outline all the options. Then you work out the pros and cons of each side. Then you give detailed breakdon of steps involved in the solution. When asked your opinion, you give pros and cons of each side and choose one answer which has the highest probability"

#tokens reserved for response while trimming long messages
token_buffer=300

#max token limit of the LLM
max_token=4096

# how frequently do you wish to issue instruction?
instruction_frequency= 1

# how much repetition is ok (on a scale of 1-100) ?
repeat_factor = 50 # 20

# how much randomness do you wish in responses (on a scale of 1-100)?
randomness = 30 #45

# Response typing speed (on a scale of 1-100)?
typing_speed = 50

# Text Messages
initial_greeting= "Marvin: Hi, I am Marvin! How can I help you today?\n"
goodbye_prompts=("QUIT","THANK YOU","BYE","GOODBYE")
goodbye_msg="Marvin: Thank You for taking my services. Hope you have a good day, or maybe not!"