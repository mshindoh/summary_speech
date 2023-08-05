"""
Convert text file to an audio file
gTTS doc: https://pypi.org/project/gTTS/
This code references the code in https://inprogrammer.com/gingerit-python-grammer-correction-using-python/
"""

from gingerit.gingerit import GingerIt
text = input("Enter a sentence >>: ")
corrected_text = GingerIt().parse(text)
print(corrected_text['result'])