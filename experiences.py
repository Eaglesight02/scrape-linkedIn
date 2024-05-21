import os
from dotenv import load_dotenv
import google.generativeai as genai

class generate_Experiences:
    def __init__(self) -> None:
        experiences_dict = None
        generation_config = None
        safety_settings = None
        model_name = None
    
    def __authenticate(self) -> bool:
        try:
            if load_dotenv("dotfiles/.env"):
                genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
                models = genai.list_models()
                return True
        except Exception as e:
            print("API KEY is invalid")
            return False

    def initial_config(self) -> bool:
        try:
            self.generatin_config = {
                "temperature": 1.0,
                "top_p": 1,
                "top_k": 0,
                "max_output_tokens": 14000,
                "response_mime_type": "text/plain" 
            }
    
    def get_Experiences(self, experiences_text = None) -> dict:
        if self.__authenticate():
            
        else:
            print("Cannot get the dictionary, taking all experiences in a single dictionary....")
            self.experiences_dict["Experience"] = experiences_text
        return self.experiences_dict.copy()