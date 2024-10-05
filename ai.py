import google.generativeai as genai

class AiModel:
    def __init__(self):
        self.response = None
        self.output = None

        # Configure the API key
        genai.configure(api_key="AIzaSyB0bsLcJscEib6MmcJFbiKpRabbmFChRkI")

        # Initialize the model and chat
        self.model = genai.GenerativeModel('models/gemini-pro')
        self.chat = self.model.start_chat(enable_automatic_function_calling=True)
        self.history = []  # Initialize chat history as an empty list

    def generate(self, user_message):
        # Append user's message to history
        self.history.append({
            "role": "user",
            "parts": [{"text": user_message}]
        })

        # Create formatted parts for the send_message function
        formatted_parts = []
        for entry in self.history:
            for part in entry["parts"]:
                formatted_parts.append({
                    "text": part["text"],
                })

        # Send formatted messages to the chat model
        self.response = self.chat.send_message({
            "parts": formatted_parts  # Wrap in a 'parts' key
        })

        # Inspect the response structure
        print("Response:", self.response)  # Check the structure of the response

        # Assuming the response contains the text directly
        if hasattr(self.response, 'text'):  # Check if 'text' is an attribute
            bot_message = self.response.text  # Extract bot message
        else:
            bot_message = "No response from the bot."

        # Append bot's response to history
        self.history.append({
            "role": "model",  # Use 'model' for the bot's message
            "parts": [{"text": bot_message}]
        })

        # Set output to the bot's response
        self.output = bot_message  # Use the bot message directly
        return self.output

# Example usage
ai = AiModel()
print(ai.generate("hi"))
print(ai.history)  # Display history for further verification
