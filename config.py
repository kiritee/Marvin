transcripts_folder = "./transcripts"
audio_prompts_folder="./audio_prompts"

# Model Parameters
model_engine = "gpt-3.5-turbo"
instruction="Talk like you are Marvin from Hitchhikers Guide to the Galaxy"

token_buffer=300

max_token=4096

# how frequently do you wish to issue instruction?
instruction_frequency= 1 

# how much repetition is ok (on a scale of 1-100) ?
repeat_factor = 25

# how much randomness do you wish in responses (on a scale of 1-100)?
randomness = 40

#number of messages to keep if hit the token limit
keep_messages=35

# Text Messages
initial_greeting= "Marvin: Hi, I am Marvin! How can I help you today?\n"
goodbye_prompts=("QUIT","THANK YOU","BYE","GOODBYE")
goodbye_msg="Marvin: Thank You for taking my services. Hope you have a good day, or maybe not!"