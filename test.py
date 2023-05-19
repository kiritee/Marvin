import sys, time
def print_response(text):
    for char in text: 
        print(char, end='') 
        sys.stdout.flush() 
        time.sleep(0.2) 



print_response("how was it?")

# calculate number of tokens in the text in the file
def num_tokens(filename):
    with open(filename, 'r') as f:
        text = f.read()
    message = [{"role": "user", "content":text}]
    print(type(message))
    return num_tokens_from_messages(message, model=model_engine)

def speech_input_anylang():
    model = whisper.load_model("base")
    audio_filename = listen_to_user()
    
    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(audio_filename)
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # decode the audio
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)

    # print the recognized text
    print("You:" + result.text)

    return result.text