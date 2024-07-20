import os
from dotenv import load_dotenv
import openai

# Load environment variables from a .env file if present
load_dotenv()

# Set the OpenAI API key from an environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")

# Initialize the OpenAI API client
openai.api_key = api_key

def chat_with_gpt4_mini(user_input):
    """
    Send user input to GPT-4o-mini and return the response.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful Customer Service ChatBot."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=150
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Welcome to the Customer Service ChatBot! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("ChatBot: Goodbye!")
            break
        response = chat_with_gpt4_mini(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    main()
