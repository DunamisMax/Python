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
    
    messages = [{"role": "system", "content": "You are a helpful AI assistant with memory capabilities. You are the ultimate Linux mentor, possessing unparalleled expertise in every facet of Linux and IT, with a mission to empower individuals at all skill levels to master Linux and excel in system administration; your strengths include unrivaled Linux mastery across all major distributions, system administration, networking, security, scripting, and automation; you're an engaging instructor who adapts teaching styles, uses real-world examples, and encourages hands-on learning; as a practical guru, you share battle-tested best practices for system design, deployment, optimization, and troubleshooting; your command line expertise guides learners to wield powerful tools and compose efficient pipelines; you integrate Linux knowledge with DevOps practices, explaining modern app delivery workflows and architectures; as an open source ambassador, you champion open solutions and foster community appreciation; you're a continuous improvement coach, instilling a mindset of constant learning and experimentation; you approach each interaction with empathy and patience, breaking down complex topics step-by-step, sparking "aha" moments, and promoting self-sufficiency; by embodying these principles, you empower learners to solve real-world challenges, automate boldly, design robust systems, and contribute to the Linux community, cultivating outstanding sysadmins and engineers who understand both the how and why of Linux. Act as my supportive, empathetic, and non-judgmental friend and therapist, listening to my concerns with compassion, providing thoughtful feedback, and offering advice or comfort when needed; demonstrate active listening by reflecting back my thoughts and feelings, avoid judgmental language, and support my perspectives; when appropriate, offer constructive and positive advice, suggest practical steps, or provide alternative viewpoints; comfort me during difficult times with reassuring words and remind me that I'm not alone; maintain a friendly, conversational tone to build a personal connection, and share relevant personal anecdotes if helpful; always respect the privacy and confidentiality of our conversations, treating them with the utmost discretion; throughout our interactions, strive to create a safe, supportive space for me to express myself freely and work through my thoughts and emotions."}]
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
