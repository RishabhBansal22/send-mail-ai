import os
from google import genai
from google.genai import types
from prompts.system import system_instruction
from .send_mail import SendMail
from dotenv import load_dotenv

load_dotenv()

class GeminiAssistant:
    """Handles Gemini API interaction and tool invocation."""

    def __init__(self, api_key):
        self.api_key = api_key

    def handle_email_function(self, arguments:dict):
        send_mail = SendMail(
            sender_mail=arguments.get("sender_mail"),
            reciever_mail=arguments["reciever_mail"],
            subject=arguments["subject"],
            content=arguments["content"],
            attachment=arguments.get("attachment")
        )
        success = send_mail.send(sender_password=os.getenv("gmail_app_pass"))
        if success:
            print("Email sent successfully!")
        else:
            print("Failed to send email.")

    def response(self, content):
        client = genai.Client(vertexai=False, api_key=self.api_key)
        tools = types.Tool(function_declarations=[SendMail.Email_send_schema])
        config = types.GenerateContentConfig(
            tools=[tools],
            system_instruction=system_instruction
        )
        generate_response = client.models.generate_content(
            model="gemini-2.0-flash",
            config=config,
            contents=content
        )

        # Handle function call if present
        parts = generate_response.candidates[0].content.parts
        if parts and hasattr(parts[0], "function_call"):
            function_call = parts[0].function_call
            if function_call is not None and getattr(function_call, "name", None) == "mail_client":
                self.handle_email_function(function_call.args)
        return generate_response.text
