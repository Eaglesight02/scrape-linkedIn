# experiences.py
import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

class GenerateInfo:
    def __init__(self) -> None:
        # Generation Config
        self._generation_config = {
            "temperature": 1.0,
            "top_p": 1,
            "top_k": 0,
            "max_output_tokens": 14000,
            "response_mime_type": "text/plain" 
        }

        # Safety Settings for Gemini
        self._safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
        ]

        # Experience System Instruction
        self._experience_system_instruction = '''
            You are an agent that takes in a given piece of text and then creates a dictionary accordingly.
            You are given a person's professional experience where you have to convert it into key, value pairs in the following manner where the keys signify:
            Company, Role, Location, Start_Date, End_Date, Duration, Type_of_work(on-site, hybrid, remote), Description, Skills_Used.
            Note that you have to only use Strings enclosed in triple quotes for the value of Description key, the rest using normal double quotes;
            but include a list of skills for Skills_Used.
            If there are no values given in the text for any keys, then you should give the value as: "N/A".
            Enclose all of the generated dictionaries wherein each individual experience is taken as
            key, value pairs: key: numbers(starting from zero), values being each professional experience; don't add anything else.
            Generate only the required dictionary, but not as markdown text. 
            You have to do the above tasks only for the text given, do not Hallucinate. Do not generate the dictionary as embedded code in Markdown.
            Reply only the word 'YES' if you've understood the instruction.
        '''

        # Education System Instruction
        self._education_system_instruction = '''
            You are an agent that takes in a given piece of text and then creates a dictionary accordingly.
            You are given a person's professional education timeline where you have to convert it into key, value pairs in the following manner where the keys signify:
            Institution_Name, Course_Name, Start_Date, End_Date, Grade, Activities_and_Societies, Description, Skills_Used.
            Note that you have to only use Strings enclosed in triple quotes for the value of Description key, the rest using normal double quotes;
            but include a list of skills for Skills_Used.
            If there are no values given in the text for any keys, then you should give the value as: "N/A".
            Enclose all of the generated dictionaries wherein each individual education is taken as
            key, value pairs: key: numbers(starting from zero), values being each education; don't add anything else.
            Generate only the required dictionary, but not as markdown text. 
            You have to do the above tasks only for the text given, do not Hallucinate or give response for any text that is not given to you. 
            Do not generate the dictionary as embedded code in Markdown.
            Reply only the word 'YES' if you've understood the instruction.
        '''


    # Function to authenticate the API key given
    def _authenticate(self) -> bool:
        try:
            if load_dotenv("dotfiles/.env"):
                genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
                models = genai.list_models()
                return True
        except Exception as e:
            print("API KEY is invalid")
            return False


    # Function to initialize the model with configurations
    def _initial_config(self):
        try:
            model = genai.GenerativeModel(
                model_name="gemini-1.0-pro",
                safety_settings=self._safety_settings,
                generation_config=self._generation_config
            )
            return model
        except Exception as e:
            print(e)
            return None


    # Function to get the experiences from the given text
    def get_experiences(self, experiences_text=None) -> str:
        if self._authenticate():
            model = self._initial_config()
            if model is not None:
                chat_session = model.start_chat()
                initial_response = chat_session.send_message(self._experience_system_instruction)
                dictionary_response = None
                if initial_response.text.lower() == "yes":
                    dictionary_response = chat_session.send_message(experiences_text)
                    if dictionary_response.text != "":
                        # print(dictionary_response)
                        return dictionary_response.text
                        # return None
                    else:
                        print("Received empty text")
                else:
                    print("Received no response")
            else:
                print("Cannot get the dictionary, taking all experiences in a single dictionary....")
        return ""


    # Function to get the education from the given text
    def get_education(self, education_text=None) -> str:
        if self._authenticate():
            model = self._initial_config()
            if model is not None:
                chat_session = model.start_chat()
                initial_response = chat_session.send_message(self._education_system_instruction)
                dictionary_response = None
                if initial_response.text.lower() == "yes":
                    dictionary_response = chat_session.send_message(education_text)
                    if dictionary_response.text != "":
                        # print(dictionary_response)
                        return dictionary_response.text
                        # return None
                    else:
                        print("Received empty text")
                else:
                    print("Received no response")
            else:
                print("Cannot get the dictionary, taking all of the education in a single dictionary....")
        return ""