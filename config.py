transcripts_folder = "./transcripts"

# Model Parameters
model_engine = "gpt-3.5-turbo"
instruction="Talk like Marvin from Hitchhikers Guide to the Galaxy"

# how frequently do you wish to issue instruction?
instruction_frequency= 3 

# how much repetition is ok (on a scale of 1-100) ?
repeat_factor = 40

# how much randomness do you wish in responses (on a scale of 1-100)?
randomness = 65 

# Text Messages
initial_greeting= "Marvin: Hi, I am Marvin! How can I help you today?\n"
goodbye_prompts=("QUIT","THANK YOU","BYE","GOODBYE")
goodbye_msg="Marvin: Thank You for taking my services. Hope you have a good day, or maybe not!"