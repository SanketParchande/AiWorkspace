import os
os.environ["GEMINI_API_KEY"] = "YOUR_API_KEY_HERE"

import google.generativeai as genai


model = genai.GenerativeModel('models/gemini-3.6-flash')


import PIL.Image
img = PIL.Image.open(r'C:\Users\Sanket\AiWorkspace\GenAI\Multimodel\AnushriDrawing.png')

import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  
response = model.generate_content(img)
to_markdown(response.text)