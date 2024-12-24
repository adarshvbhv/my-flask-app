# genai_module.py

import os
import google.generativeai as genai


# Suppress logging warnings
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

def remove_non_bmp_characters(text):
    # Remove characters that are outside of the BMP (Basic Multilingual Plane)
    return ''.join([char for char in text if ord(char) <= 0xFFFF])

def generate_ai_content(prompt):
    # Configure the API key
    genai.configure(api_key="AIzaSyBPbbU14dj8LsZyHOZoH3T_gzN7X7scNJg")
    
    # Create the GenerativeModel instance
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    # Generate content
    response = model.generate_content(prompt)
    
    return remove_non_bmp_characters(response.text)


# text_path = "C:\\Users\\ADARSH KUMAR\\Success\\hiii\\2024-12-20_03-54-10_UTC.txt"
# with open(text_path, 'r', encoding='utf-8') as file:
#     text_content = file.read()
# title = generate_ai_content(text_content + "       :make the above under 100 characters and return only the answer so that i can directly copy paste to be written")
# print(f"title generated {title}")

  