import hashlib
from pathlib import Path
from openai import OpenAI
from playsound import playsound
from pyaxidraw import axidraw   

client = None
def generate_and_play_sound(input_text, blocking=True):
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
        playsound(str(speech_file_path), blocking)
    except Exception as e:
        print(f"Error playing audio: {e}")

# Example usage
#generate_and_play_sound("Today is a wonderful day to build something people love!")

ad = axidraw.AxiDraw()

generate_and_play_sound("Hello there. Let's talk about drawing with turtles.")
generate_and_play_sound("You can imagine a turtle like this.", False)

ad.plot_setup("svgs/1-turtle.svg")
ad.plot_run()
input()

generate_and_play_sound("A turtle is a metaphor for a pen. It can move around and draw lines, but unlike the pen it has a direction.")
ad.plot_setup("svgs/2-turtle-dir.svg")
ad.plot_run()

generate_and_play_sound("Turtles have instructions like forward which can move them around.")
generate_and_play_sound("Let's try to move our turtle forward 100 units.")

ad.plot_setup("svgs/3-forward.svg")
ad.plot_run()

generate_and_play_sound("And now let's move it back. To get to the bottom of the page we need to go down by 100 units, because we are already on the top of the page", False)
ad.plot_setup("svgs/back.svg")
ad.plot_run()

generate_and_play_sound("Great this is all good then, but it's not very interesting.")

generate_and_play_sound("Another thing we can do is turn the turtle, but first let's move it back to the middle.")

ad.plot_setup("svgs/1-turtle.svg")
ad.plot_run()

generate_and_play_sound("Now let's say we turn the turtle 180 degrees to the right.")

ad.plot_setup("svgs/right.svg")
ad.plot_run()

generate_and_play_sound("Now if we would move forward we would be at the bottom of the page facing downwards.")
generate_and_play_sound("Let's turn left instead and move forward", False)



generate_and_play_sound("But this time let's put the pen down and draw a line.")
generate_and_play_sound("We can put the pen up or the pen down with these commands, named penup and pendown.")

ad.plot_setup("svgs/penuppendown.svg")
ad.plot_run()

generate_and_play_sound("So now we move forward and badabim daboom we have a line.", False)

ad.plot_setup("svgs/left.svg")
ad.plot_run()

generate_and_play_sound("This was just to show you the basics. We won't draw the triangle anymore.")
generate_and_play_sound("When you're ready change the paper and press ENTER to continue.")
