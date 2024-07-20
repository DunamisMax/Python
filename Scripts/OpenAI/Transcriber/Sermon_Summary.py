import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from a .env file if present
load_dotenv()

# Set the OpenAI API key from an environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")

# Instantiate the OpenAI client
client = OpenAI(api_key=api_key)

def get_unique_filename(base_name, extension):
    """
    Generate a unique filename by appending a number if the file already exists.
    """
    counter = 0
    while True:
        filename = f"{base_name}{('-' + str(counter)) if counter else ''}.{extension}"
        if not os.path.exists(filename):
            return filename
        counter += 1

def summarize_text(text):
    """
    Summarize the given text and extract Bible references using GPT-4o-mini.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Summarize the following text and extract Bible references:\n\n{text}"}
            ],
            max_tokens=16384
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise RuntimeError(f"Error summarizing text: {e}")

def read_transcription(file_path):
    """
    Read the transcription from the specified file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The specified transcription file '{file_path}' does not exist.")
    
    with open(file_path, "r") as f:
        return f.read()

def save_summary(summary, base_name="summary", extension="md"):
    """
    Save the summary to a file with a unique filename.
    """
    summary_file = get_unique_filename(base_name, extension)
    try:
        with open(summary_file, "w") as f:
            f.write(f"# Summary\n\n{summary}")
        print(f"Summary saved to {summary_file}")
    except Exception as e:
        raise RuntimeError(f"Error saving summary: {e}")

def main():
    transcription_file = "transcription.txt"
    try:
        transcription = read_transcription(transcription_file)
        summary = summarize_text(transcription)
        save_summary(summary)
    except (FileNotFoundError, RuntimeError) as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
