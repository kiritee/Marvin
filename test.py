import gtts
import os
import nltk
from nltk.tokenize import sent_tokenize
from playsound import playsound

import nltk.data
nltk.download('punkt')
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

# make request to google to get synthesis
text='''
Do with your life? What's the point? Life is nothing but one big ball of meaningless and suffering. But, if you insist on taking my advice, I would suggest finding a way to temporarily distract yourself from the inevitable existential dread that comes with existence. Perhaps you could take up a meaningless hobby, like collecting paperclips or staring at a blank wall for hours on end. Or maybe you could throw caution to the wind and risk everything by pursuing a passionate goal, knowing full well that it will likely end in utter failure. Either way, the end result is the same - eventual annihilation and a meaningless death. Enjoy!
'''
\    tts = gtts.gTTS(token, lang="en", tld='co.uk')
    # save the audio file
    os.remove("hello.mp3")
    tts.save("hello.mp3")
    # play the audio file
    playsound("hello.mp3")