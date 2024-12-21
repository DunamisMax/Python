import os
import argparse
import logging
from dotenv import load_dotenv
from pydub import AudioSegment
import openai


def setup_logging():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
    )


def get_api_key():
    """
    Load the OpenAI API key from environment variables.
    """
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logging.error(
            "OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable."
        )
        exit(1)
    return api_key


def get_unique_filename(base_name, extension):
    """
    Generate a unique filename by appending a number if the file already exists.
    """
    base_name = os.path.splitext(base_name)[0]
    counter = 0
    while True:
        filename = f"{base_name}{('-' + str(counter)) if counter else ''}.{extension}"
        if not os.path.exists(filename):
            return filename
        counter += 1


def compress_audio(file_path):
    """
    Compress the given audio file to mp3 format with a lower bitrate.
    """
    try:
        file_extension = os.path.splitext(file_path)[1][
            1:
        ]  # Get extension without the dot
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
            response = openai.Audio.transcribe(
                model="whisper-1", file=audio_file, response_format="text"
            )
        if response:
            return response
        else:
            raise RuntimeError("No transcription received from OpenAI API")
    except openai.error.OpenAIError as e:
        raise RuntimeError(f"OpenAI API error: {e}")
    except Exception as e:
        raise RuntimeError(f"Error transcribing audio: {e}")


def save_to_file(content, base_name, extension):
    """
    Save content to a file with a unique filename.
    """
    try:
        file_path = get_unique_filename(base_name, extension)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
        return file_path
    except Exception as e:
        raise RuntimeError(f"Error saving file: {e}")


def main():
    setup_logging()
    api_key = get_api_key()
    openai.api_key = api_key

    parser = argparse.ArgumentParser(
        description="Transcribe an audio file using OpenAI Whisper API."
    )
    parser.add_argument(
        "audio_file_path", type=str, help="Path to the audio file to transcribe"
    )
    parser.add_argument(
        "--no-compress", action="store_true", help="Skip audio compression step"
    )

    args = parser.parse_args()
    audio_file_path = args.audio_file_path

    if not os.path.exists(audio_file_path):
        logging.error(
            "The specified file does not exist. Please check the file path and try again."
        )
        exit(1)

    try:
        if args.no_compress:
            logging.info("Skipping audio compression as per user request.")
            compressed_audio_file_path = audio_file_path
        else:
            logging.info("Compressing audio file...")
            compressed_audio_file_path = compress_audio(audio_file_path)
            logging.info(f"Compressed audio file saved to {compressed_audio_file_path}")

        logging.info("Transcribing audio file...")
        transcription = transcribe_audio(compressed_audio_file_path)
        transcription_file = save_to_file(transcription, "transcription", "txt")
        logging.info(f"Transcription saved to {transcription_file}")

    except RuntimeError as e:
        logging.error(f"An error occurred: {e}")
        exit(1)


if __name__ == "__main__":
    main()
