import os
import openai
from pydub import AudioSegment

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

def compress_audio(file_path):
    """
    Compress the given audio file to mp3 format.
    """
    audio = AudioSegment.from_file(file_path)
    compressed_file_path = get_unique_filename("compressed_audio", "mp3")
    audio.export(compressed_file_path, format="mp3", bitrate="64k")
    return compressed_file_path

def transcribe_audio(file_path):
    """
    Transcribe the given audio file using OpenAI Whisper.
    """
    with open(file_path, "rb") as audio_file:
        response = openai.Audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="text"
        )
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
    audio_file_path = input("Please enter the path to the audio file: ").strip('\"')
    
    if not os.path.exists(audio_file_path):
        print("The specified file does not exist. Please check the file path and try again.")
        return

    # Step 1: Compress the audio file
    compressed_audio_file_path = compress_audio(audio_file_path)
    
    # Step 2: Transcribe the compressed audio file
    transcription = transcribe_audio(compressed_audio_file_path)
    
    # Step 3: Save the transcription to a text file
    transcription_file = get_unique_filename("transcription", "txt")
    with open(transcription_file, "w") as f:
        f.write(transcription)
    
    # Step 4: Get summary and Bible references from GPT-4o-mini
    summary = summarize_text(transcription)
    
    # Step 5: Save the summary to a markdown file
    summary_file = get_unique_filename("summary", "md")
    with open(summary_file, "w") as f:
        f.write(f"# Summary\n\n{summary}")
    
    print(f"Transcription saved to {transcription_file}")
    print(f"Summary saved to {summary_file}")

if __name__ == "__main__":
    main()
