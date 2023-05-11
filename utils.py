from config import *
import os
import pathlib
from datetime import datetime
import time
import openai
import tiktoken
import speech_recognition as sr


openai.api_key = os.getenv("OPENAI_API_KEY")

# function to get speech input
def speech_input():
    # obtain audio from the microphone
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

    with open(audio_filename,'rb') as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file, language='en')["text"]
    print("You: " + transcript)
    return transcript


  # function to remove item from a list
def remove_items(test_list, item):
    res = [i for i in test_list if i != item]
    return res

# Chat Response Function
def chat_response(question_message):
    try:
        response = openai.ChatCompletion.create(model=model_engine,messages=question_message)
        #, frequency_penalty=2-repeat_factor/25, temperature=randomness/50)
    except openai.error.RateLimitError:
        time.sleep(60)
        response = openai.ChatCompletion.create(model=model_engine,messages=question_message, frequency_penalty=2-repeat_factor/25, temperature=randomness/50)
    answer_message = response.choices[0]['message']
    return answer_message

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
      raise NotImplementedError(f"""num_tokens_from_messages() is not presently implemented for model {model}.
             See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens.""")