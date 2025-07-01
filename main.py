from src.gemini import GeminiAssistant
import os
from dotenv import load_dotenv



def main():
    load_dotenv()
    ai = GeminiAssistant(api_key=os.getenv("gemini_api_key"))
    user = input("USER : ")
    response = ai.response(content=user)
    if response:
        print(response)
            

if __name__ == "__main__":
    main()