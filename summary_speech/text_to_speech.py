"""
Convert text file to an audio file
gTTS: https://pypi.org/project/gTTS/
gingerit: https://pypi.org/project/gingerit/
Reference:
 https://inprogrammer.com/text-to-speech-using-python/
 https://inprogrammer.com/gingerit-python-grammer-correction-using-python/
"""

from gtts import gTTS
from gingerit.gingerit import GingerIt
import os.path

TYPE_TEXT = 0
TYPE_MP3 = 1

def get_file(type):
    if type == TYPE_TEXT:
        file = input("Enter the input filename (without .txt): ")
        file = "../data/" + file + ".txt"

        if not os.path.isfile(file):
            print('The file did not found. Terminating the program.')
            return None

    elif type == TYPE_MP3:
        file = input("Enter the filename for output (without .mp3): ")
        file += "../data/" + file + ".mp3"

    return file

def correct_grammar(text):
    corrected_text = GingerIt().parse(text)
    return corrected_text['result']

def text_to_audio():

    input_file = get_file(TYPE_TEXT)
    out_file = get_file(TYPE_MP3)

    with open(input_file) as f:
        text = f.read()

    text = correct_grammar(text)
    obj = gTTS(text=text, lang='en', slow=False)
    obj.save(out_file)

    print("The output audio file " + out_file + " is created.")

if __name__ == '__main__':
    text_to_audio()
