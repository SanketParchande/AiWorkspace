import os
os.environ["GEMINI_API_KEY"] = ""

import google.generativeai as genai


model = genai.GenerativeModel('models/gemini-3.6-flash')

#response = model.generate_content("Write a short poem about the beauty of nature.")
#print(response.text)

#2
import pathlib
import textwrap

import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
##To find the history of LLM's 
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name, m.description)
        
#%%time
#response = model.generate_content("Write a short poem about the beauty of nature.")
#to_markdown(response.text)