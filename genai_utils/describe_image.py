#!/usr/bin/env python 

'''
python -m genai_utils.index_imges --directory </path/to/images>

'''
from ollama import generate

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DEFAULT_MODEL = 'qwen2.5vl'

DEFAULT_SYSTEM_PROMPT = """
You are an image analyst who has been tasked with describing images.
Your goal is to enable retrieving the images based on the content of your descriptions.
"""

DEFAULT_USER_PROMPT = """
Describe this image.
Provide a thorough and detailed description, focusing on identifying and describing objects in the image.
Use denotative rather than connotative language. 
Read the text in the images and include it in the description without including the location of font name.
Do not explain how you are describing the image. Do not use any "I" statements.
"""

def describe_image(image_data, prompt=DEFAULT_USER_PROMPT, system=DEFAULT_SYSTEM_PROMPT, model=DEFAULT_MODEL):
    result = generate(model=model, prompt=prompt, images=[image_data])
    return result['response']
