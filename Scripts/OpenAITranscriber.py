import os
import openai

# Set the OpenAI API key from an environment variable
openai.api_key = os.getenv("OPENAIAPI")

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

def transcribe_audio(file_path):
    """
    Transcribe the given audio file using OpenAI Whisper.
    """
    with open(file_path, "rb") as audio_file:
        response = openai.Audio.transcribe("whisper-1", audio_file)
    return response['text']

def summarize_text(text):
    """
    Summarize the given text and extract Bible references using GPT-4o-mini.
    """
    response = openai.Completion.create(
        model="gpt-4o-mini",
        prompt=f"Summarize the following text and extract Bible references:\n\n{text}",
        max_tokens=500
    )
    return response.choices[0].text.strip()

def main():
    # Prompt the user to input the audio file path
    audio_file_path = input("Please enter the path to the audio file: ")
    
    if not os.path.exists(audio_file_path):
        print("The specified file does not exist. Please check the file path and try again.")
        return
    
    # Step 1: Transcribe the audio file
    transcription = transcribe_audio(audio_file_path)
    
    # Step 2: Save the transcription to a text file
    transcription_file = get_unique_filename("transcription", "txt")
    with open(transcription_file, "w") as f:
        f.write(transcription)
    
    # Step 3: Get summary and Bible references from GPT-4o-mini
    summary = summarize_text(transcription)
    
    # Step 4: Save the summary to a markdown file
    summary_file = get_unique_filename("summary", "md")
    with open(summary_file, "w") as f:
        f.write(f"# Summary\n\n{summary}")
    
    print(f"Transcription saved to {transcription_file}")
    print(f"Summary saved to {summary_file}")

if __name__ == "__main__":
    main()
