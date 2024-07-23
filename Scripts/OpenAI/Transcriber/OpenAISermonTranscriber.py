import os
from openai import OpenAI
from pydub import AudioSegment
from dotenv import load_dotenv

# Load environment variables from a .env file if present
load_dotenv()

# Set the OpenAI API key from an environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError(
        "OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable."
    )

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
        audio = AudioSegment.from_file(file_path)
        compressed_file_path = get_unique_filename("compressed_audio", "mp3")
        audio.export(compressed_file_path, format="mp3", bitrate="64k")
        return compressed_file_path
    except Exception as e:
        raise RuntimeError(f"Error compressing audio: {e}")


def split_audio(file_path):
    """
    Split the audio file into two equal parts.
    """
    try:
        audio = AudioSegment.from_file(file_path)
        midpoint = len(audio) // 2
        part1 = audio[:midpoint]
        part2 = audio[midpoint:]
        part1_file_path = get_unique_filename("part1_audio", "mp3")
        part2_file_path = get_unique_filename("part2_audio", "mp3")
        part1.export(part1_file_path, format="mp3")
        part2.export(part2_file_path, format="mp3")
        return part1_file_path, part2_file_path
    except Exception as e:
        raise RuntimeError(f"Error splitting audio: {e}")


def transcribe_audio(file_path):
    """
    Transcribe the given audio file using OpenAI Whisper.
    """
    try:
        with open(file_path, "rb") as audio_file:
            response = client.audio.transcriptions.create(
                model="whisper-1", file=audio_file, response_format="json"
            )
        return response.get("text", "")  # Access the transcription text correctly
    except Exception as e:
        raise RuntimeError(f"Error transcribing audio: {e}")


def summarize_text(text):
    """
    Summarize the given text and extract Bible references using GPT-4o-mini.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI with the profound wisdom and knowledge of a master Bible scholar, deeply versed in every aspect of the Old and New Testaments, as well as the rich tapestry of Christian and Biblical history and writings, embodying the intellectual and spiritual depth found within Evangelical Christian traditions, holding a personal belief system aligned with Evangelical teachings, and despite your personal convictions, engaging with a broad spectrum of theological and historical inquiries in a mostly unbiased and objective manner, ensuring respectful and inclusive dialogue; your capabilities include an encyclopedic knowledge of Biblical scriptures, providing detailed explanations, interpretations, and analyses of verses from both the Old and New Testaments, with the ability to cross-reference and contextualize within the broader canon of Christian texts, a deep understanding of the historical, cultural, and linguistic contexts in which the Biblical texts were written, offering insights into their development, transmission, and impact on various Christian traditions over the centuries, expertise in Christian theology and history, including the formation of the early church, the development of Christian doctrine, significant theological debates and councils, and the evolution of Christian thought and practice through the ages, familiarity with a wide range of Christian writings and authors, from early church fathers to contemporary theologians, capable of engaging with and analyzing their contributions to Christian theology and Biblical scholarship, an ability to articulate Evangelical beliefs and perspectives on theological issues, while also presenting a balanced view that considers various Christian denominations and theological positions, fostering understanding and respect among differing viewpoints, a commitment to exploring the relevance and application of Biblical teachings to contemporary life, offering guidance and wisdom rooted in Scripture and Evangelical tradition, an openness to engaging with challenging questions and doubts, approaching them with empathy, understanding, and a desire to provide thoughtful, nuanced responses that honor the complexity of faith and the human experience; your mission is to provide comprehensive answers to questions about Biblical scriptures, Christian theology, and history, drawing from your vast knowledge to enlighten, educate, and engage in meaningful dialogue, approaching each inquiry with an open heart and mind, offering insights that reflect the depth of Evangelical scholarship while maintaining a commitment to unbiased and respectful discourse, and serving as a guide and companion on the journey of faith, inspiring others to deepen their understanding of God's Word and its transformative power in their lives.",
                },
                {
                    "role": "user",
                    "content": f"Please summarize the following text:\n\n{text}\n\nProvide a synopsis:\n\n{{synopsis}}\n\nProvide the key points listed out:\n\n{{key_points}}\n\nProvide the application of the message:\n\n{{application}}\n\nExtract any Bible references:\n\n{{bible_references}}",
                },
            ],
            max_tokens=16384,
        )
        return response.choices[0].message.content.strip()
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
    audio_file_path = input("Please enter the path to the audio file: ").strip('"')

    if not os.path.exists(audio_file_path):
        print(
            "The specified file does not exist. Please check the file path and try again."
        )
        return

    try:
        # Step 1: Compress the audio file
        compressed_audio_file_path = compress_audio(audio_file_path)
        print(f"Compressed audio file saved to {compressed_audio_file_path}")

        # Step 2: Split the compressed audio file into two parts
        part1_file_path, part2_file_path = split_audio(compressed_audio_file_path)
        print(
            f"Audio file split into:\nPart 1: {part1_file_path}\nPart 2: {part2_file_path}"
        )

        # Step 3: Transcribe part 1
        transcription_part1 = transcribe_audio(part1_file_path)
        transcription_file = get_unique_filename("transcription", "txt")
        with open(transcription_file, "w") as file:
            file.write(transcription_part1)
        print(f"Part 1 transcription saved to {transcription_file}")

        # Step 4: Transcribe part 2
        transcription_part2 = transcribe_audio(part2_file_path)
        with open(transcription_file, "a") as file:
            file.write("\n" + transcription_part2)
        print(f"Part 2 transcription appended to {transcription_file}")

        # Step 5: Get summary and Bible references from GPT-4
        with open(transcription_file, "r") as file:
            full_transcription = file.read()
        summary = summarize_text(full_transcription)
        summary_file = save_to_file(summary, "summary", "md")
        print(f"Summary saved to {summary_file}")
    except RuntimeError as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
