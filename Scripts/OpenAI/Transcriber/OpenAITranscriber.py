import os
import openai
from pydub import AudioSegment
from dotenv import load_dotenv

# Load environment variables from a .env file if present
load_dotenv()

# Set the OpenAI API key from an environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")
openai.api_key = api_key

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

def compress_audio(file_path):
    """
    Compress the given audio file to mp3 format.
    """
    try:
        audio = AudioSegment.from_file(file_path)
        compressed_file_path = get_unique_filename("compressed_audio", "mp3")
        audio.export(compressed_file_path, format="mp3", bitrate="64k")
        return compressed_file_path
    except Exception as e:
        raise RuntimeError(f"Error compressing audio: {e}")

def transcribe_audio(file_path):
    """
    Transcribe the given audio file using OpenAI Whisper.
    """
    try:
        with open(file_path, "rb") as audio_file:
            response = openai.Audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="text"
            )
        return response['text']
    except Exception as e:
        raise RuntimeError(f"Error transcribing audio: {e}")

def summarize_text(text):
    """
    Summarize the given text and extract Bible references using GPT-4o-mini.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Summarize the following text and extract Bible references:\n\n{text}"}
            ],
            max_tokens=1000  # Adjust as needed
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        raise RuntimeError(f"Error summarizing text: {e}")

def save_to_file(content, base_name, extension):
    """
    Save content to a file with a unique filename.
    """
    try:
        file_path = get_unique_filename(base_name, extension)
        with open(file_path, "w") as file:
            file.write(content)
        return file_path
    except Exception as e:
        raise RuntimeError(f"Error saving file: {e}")

def main():
    # Prompt the user to input the audio file path
    audio_file_path = input("Please enter the path to the audio file: ").strip('\"')
    
    if not os.path.exists(audio_file_path):
        print("The specified file does not exist. Please check the file path and try again.")
        return

    try:
        # Step 1: Compress the audio file
        compressed_audio_file_path = compress_audio(audio_file_path)
        print(f"Compressed audio file saved to {compressed_audio_file_path}")

        # Step 2: Transcribe the compressed audio file
        transcription = transcribe_audio(compressed_audio_file_path)
        transcription_file = save_to_file(transcription, "transcription", "txt")
        print(f"Transcription saved to {transcription_file}")

        # Step 3: Get summary and Bible references from GPT-4o-mini
        summary = summarize_text(transcription)
        summary_file = save_to_file(summary, "summary", "md")
        print(f"Summary saved to {summary_file}")
    except RuntimeError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
