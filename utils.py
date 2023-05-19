from config import *
import os
import pathlib
from datetime import datetime
import time
import sys
import openai
import tiktoken
import speech_recognition as sr
import whisper

# listen to speech input from microphone and record on to a wav file
def listen_to_user() :
    r = sr.Recognizer()
    r.energy_threshold = 4000
    with sr.Microphone() as source:
        print("speak now")
        audio = r.listen(source, timeout=None, phrase_time_limit=None)

    pathlib.Path(audio_prompts_folder).mkdir(parents=True, exist_ok=True) 
    now = datetime.now()
    audio_filename = audio_prompts_folder + "/ap_"+ now.strftime("%Y_%m_%d_%H%M") + ".wav"
    with open(audio_filename, 'wb') as audio_file:
        audio_file.write(audio.get_wav_data())
    return audio_filename

# take speech input in any language
def speech_input(lang):
    if lang == 'en':
        return speech_input_en()
    else: return speech_input_lang(lang)

# function to get speech input in English
def speech_input_en():
    audio_filename = listen_to_user()
    with open(audio_filename,'rb') as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file, language='en')["text"]
    print("You: " + transcript)
    return transcript

# function to get speech input in non-English language
def speech_input_lang(lang):
    audio_filename = listen_to_user()
    with open(audio_filename,'rb') as audio_file:
        audio_ts = openai.Audio.translate("whisper-1", audio_file)
    with open(audio_filename,'rb') as audio_file:
        transcript_orig = openai.Audio.transcribe("whisper-1", audio_file, language=lang)["text"]
    transcript = audio_ts["text"]
    print("You: " + transcript_orig)
    print("("+transcript+")")
    return transcript



# print text on screen one character at a time
def print_response(text):
    for char in text: 
        print(char, end='') 
        sys.stdout.flush() 
        time.sleep(0.03) 


  # function to remove item from a list
def remove_items(test_list, item):
    res = [i for i in test_list if i != item]
    return res

# Chat Response Function
def chat_response(question_message):
    try:
        response = openai.ChatCompletion.create(model=model_engine,messages=question_message, frequency_penalty=2-repeat_factor/25, temperature=randomness/50)
    except openai.error.RateLimitError:
        time.sleep(60)
        response = openai.ChatCompletion.create(model=model_engine,messages=question_message, frequency_penalty=2-repeat_factor/25, temperature=randomness/50)
    answer_message = response.choices[0]['message']
    return answer_message

# stream chat Response Function
def chat_response_stream(question_message):
    try:
        response = openai.ChatCompletion.create(model=model_engine,messages=question_message, frequency_penalty=2-repeat_factor/25, temperature=randomness/50, stream=True)
    except openai.error.RateLimitError:
        time.sleep(60)
        response = openai.ChatCompletion.create(model=model_engine,messages=question_message, frequency_penalty=2-repeat_factor/25, temperature=randomness/50, stream=True)
    return response

# truncate message if too long; drop old messages in conversation
def trimmed(messages, token_buffer = token_buffer, max_token = max_token, model_engine=model_engine):
    while num_tokens_from_messages(messages, model=model_engine) > max_token - token_buffer :
        messages=messages[-1:]
    return messages

# count number of tokens in message
def num_tokens_from_messages(messages, model=model_engine):
  """Returns the number of tokens used by a list of messages."""
  try:
      encoding = tiktoken.encoding_for_model(model)
  except KeyError:
      encoding = tiktoken.get_encoding("cl100k_base")
  if model == model_engine:  # note: future models may deviate from this
      num_tokens = 0
      for message in messages:
          num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
          for key, value in message.items():
              num_tokens += len(encoding.encode(value))
              if key == "name":  # if there's a name, the role is omitted
                  num_tokens += -1  # role is always required and always 1 token
      num_tokens += 2  # every reply is primed with <im_start>assistant
      return num_tokens
  else:
      raise NotImplementedError(f"""num_tokens_from_messages() is not presently implemented for model {model}""")
  
# define our clear function
def clear(): 
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


