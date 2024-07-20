import os
import openai

# Set the OpenAI API key from an environment variable
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

def get_unique_filename(base_name, extension):
    """
    Generate a unique filename by appending a number if the file already exists.
    """
    counter = 0
    while True:
        if counter == 0:
            filename = f"{base_name}.{extension}"
        else:
            filename = f"{base_name}-{counter}.{extension}"
        if not os.path.exists(filename):
            return filename
        counter += 1

def summarize_text(text):
    """
    Summarize the given text and extract Bible references using GPT-4o-mini.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Summarize the following text and extract Bible references:\n\n{text}"}
        ],
        max_tokens=16384
    )
    return response.choices[0].message.content.strip()

def main():
    # Read the transcription from the file
    transcription_file = "transcription.txt"
    if not os.path.exists(transcription_file):
        print("The specified transcription file does not exist. Please check the file path and try again.")
        return

    with open(transcription_file, "r") as f:
        transcription = f.read()

    # Get summary and Bible references from GPT-4o-mini
    summary = summarize_text(transcription)
    
    # Save the summary to a markdown file
    summary_file = get_unique_filename("summary", "md")
    with open(summary_file, "w") as f:
        f.write(f"# Summary\n\n{summary}")
    
    print(f"Summary saved to {summary_file}")

if __name__ == "__main__":
    main()
