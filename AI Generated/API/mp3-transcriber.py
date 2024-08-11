import os
import sys
from openai import OpenAI
from pydub import AudioSegment
from dotenv import load_dotenv

# Load environment variables from a .env file if present
load_dotenv()

# Set the OpenAI API key from an environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    sys.exit("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")

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

def compress_audio(file_path):
    """
    Compress the given audio file to mp3 format.
    """
    try:
        file_extension = os.path.splitext(file_path)[1][1:]  # Get the extension without the dot
        audio = AudioSegment.from_file(file_path, format=file_extension)
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
            response = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="json"
            )
        
        transcription_text = response.text
        if transcription_text:
            return transcription_text
        else:
            raise RuntimeError("Transcription text not found in response")
    except openai.APIError as e:
        raise RuntimeError(f"OpenAI API error: {e}")
    except Exception as e:
        raise RuntimeError(f"Error transcribing audio: {e}")

def save_to_file(content, base_name, extension):
    """
    Save content to a file with a unique filename.
    """
    try:
        file_path = get_unique_filename(base_name, extension)
        with open(file_path, "w", encoding='utf-8') as file:
            file.write(content)
        return file_path
    except Exception as e:
        raise RuntimeError(f"Error saving file: {e}")

def main():
    audio_file_path = input("Please enter the path to the audio file: ").strip('"')

    if not os.path.exists(audio_file_path):
        print("The specified file does not exist. Please check the file path and try again.")
        return

    try:
        compressed_audio_file_path = compress_audio(audio_file_path)
        print(f"Compressed audio file saved to {compressed_audio_file_path}")

        transcription = transcribe_audio(compressed_audio_file_path)
        transcription_file = save_to_file(transcription, "transcription", "txt")
        print(f"Transcription saved to {transcription_file}")

    except RuntimeError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()