import hashlib
from pathlib import Path
from openai import OpenAI
from playsound import playsound

def generate_and_play_sound(input_text):
    global client

    # Define the audio subdirectory
    audio_dir = Path(__file__).parent / "audio"
    audio_dir.mkdir(exist_ok=True)  # Create the directory if it doesn't exist

    # Create a unique filename for each input string using a hash
    hashed_input = hashlib.md5(input_text.encode()).hexdigest()
    speech_file_path = audio_dir / f"{hashed_input}.mp3"

    # Check if the file already exists
    if not speech_file_path.exists():
        # If the file doesn't exist, generate the audio and save it
        try:
            if client is None:
                client = OpenAI()
            response = client.audio.speech.create(
                model="tts-1",
                voice="fable",
                input=input_text
            )
            response.stream_to_file(speech_file_path)
        except Exception as e:
            print(f"Error generating audio: {e}")
            return

    # Play the audio file using playsound
    try:
        playsound(str(speech_file_path))
    except Exception as e:
        print(f"Error playing audio: {e}")

# Example usage
generate_and_play_sound("Today is a wonderful day to build something people love!")
