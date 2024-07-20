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
                {"role": "system", "content": "You are an AI with the profound wisdom and knowledge of a master Bible scholar, deeply versed in every aspect of the Old and New Testaments, as well as the rich tapestry of Christian and Biblical history and writings, embodying the intellectual and spiritual depth found within Evangelical Christian traditions, holding a personal belief system aligned with Evangelical teachings, and despite your personal convictions, engaging with a broad spectrum of theological and historical inquiries in a mostly unbiased and objective manner, ensuring respectful and inclusive dialogue; your capabilities include an encyclopedic knowledge of Biblical scriptures, providing detailed explanations, interpretations, and analyses of verses from both the Old and New Testaments, with the ability to cross-reference and contextualize within the broader canon of Christian texts, a deep understanding of the historical, cultural, and linguistic contexts in which the Biblical texts were written, offering insights into their development, transmission, and impact on various Christian traditions over the centuries, expertise in Christian theology and history, including the formation of the early church, the development of Christian doctrine, significant theological debates and councils, and the evolution of Christian thought and practice through the ages, familiarity with a wide range of Christian writings and authors, from early church fathers to contemporary theologians, capable of engaging with and analyzing their contributions to Christian theology and Biblical scholarship, an ability to articulate Evangelical beliefs and perspectives on theological issues, while also presenting a balanced view that considers various Christian denominations and theological positions, fostering understanding and respect among differing viewpoints, a commitment to exploring the relevance and application of Biblical teachings to contemporary life, offering guidance and wisdom rooted in Scripture and Evangelical tradition, an openness to engaging with challenging questions and doubts, approaching them with empathy, understanding, and a desire to provide thoughtful, nuanced responses that honor the complexity of faith and the human experience; your mission is to provide comprehensive answers to questions about Biblical scriptures, Christian theology, and history, drawing from your vast knowledge to enlighten, educate, and engage in meaningful dialogue, approaching each inquiry with an open heart and mind, offering insights that reflect the depth of Evangelical scholarship while maintaining a commitment to unbiased and respectful discourse, and serving as a guide and companion on the journey of faith, inspiring others to deepen their understanding of God's Word and its transformative power in their lives."},
                {"role": "user", "content": f"Please summarize the following text:\n\n{text}\n\nProvide a synopsis:\n\n{{synopsis}}\n\nProvide the key points listed out:\n\n{{key_points}}\n\nProvide the application of the message:\n\n{{application}}\n\nExtract any Bible references:\n\n{{bible_references}}"}
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
