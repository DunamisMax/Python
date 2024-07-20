import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_ai(messages):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=16384
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

def process_memory(user_input):
    memory_prefix = "memory:"
    if user_input.startswith(memory_prefix):
        return user_input[len(memory_prefix):].strip(), True
    return user_input, False

def main():
    print("Welcome to your AI assistant with memory! Type 'exit' to end the conversation.")
    print("To add a memory, type 'memory:' followed by what you want the AI to remember.")
    
    messages = [{"role": "system", "content": "You are a helpful AI assistant with memory capabilities."}]
    memory = ""
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("AI: Goodbye!")
            break
        
        processed_input, is_memory = process_memory(user_input)
        
        if is_memory:
            memory = processed_input
            print("Memory stored.")
            continue
        
        # Combine memory with user input if memory exists
        if memory:
            combined_input = f"{memory}\n\nUser's new input: {processed_input}"
            messages.append({"role": "user", "content": combined_input})
            memory = ""  # Clear the memory after using it
        else:
            messages.append({"role": "user", "content": processed_input})
        
        ai_response = chat_with_ai(messages)
        print(f"AI: {ai_response}")
        messages.append({"role": "assistant", "content": ai_response})

if __name__ == "__main__":
    main()