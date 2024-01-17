# Used as a base to send OCR text to Logo to be interpreted
# [ * OCR ] -> [ LOGO ] -> [ AXIDRAW ]

import os
import time
from ocrmac import ocrmac
from PIL import Image
import subprocess
import re
import cv2

logo_folder = '/Users/tudvari/Documents'
pipe_name = 'logo_in_pipe'
pipe_path = logo_folder + os.sep + pipe_name
pipe_axidraw = logo_folder + os.sep + 'axidraw'

replace_dict = {
    "lsb": "[",
    "rsb": "]",
    "lcb": "{",
    "rcb": "}",
    "lp": "(",
    "rp": ")",
    "[": "",
    "]": "",
    "{": "",
    "}": "",
    "(": "",
    ")": "",
    "lt": "axilt",
    "left": "axilt",
    "rt": "axirt",
    "right": "axirt",
    "fd": "axifd",
    "forward": "axifd",
    "bk": "axibk",
    "back": "axibk",
    "pu": "axipu",
    "penup": "axipu",
    "pd": "axipd",
    "pendown": "axipd",
    "cs": "axics"
}

def run_applescript(script):
    subprocess.run(["osascript", "-e", script])

def send_stop_to_logo():
    # if in the loop waiting for command send this
    #send_to_logo("continue")

    # if in an infinite logo loop send this
    run_applescript('tell application "UCBLogo" to activate')
    time.sleep(1)
    run_applescript('tell application "System Events" to keystroke "s" using option down')
    #pyautogui.hotkey('alt', 's')  # Use 'option' for macOS


def setup():
    if not os.path.exists(pipe_path):
        os.mkfifo(pipe_path)
    if not os.path.exists(pipe_axidraw):
        os.mkfifo(pipe_axidraw)

    #copy axidraw.logo file to logo folder
    os.system("cp axidraw.logo " + logo_folder + os.sep + "axidraw.logo")    
    # send_to_logo("load \"axidraw.logo")
    send_to_logo("print [Message from python]")
    
def send_to_logo(text):
    if text.strip().startswith("to"):
        def_logo_function(text)
        return
    print(f"sending {text} to logo")
    with open(pipe_path, 'w') as pipe:
        pipe.write(text + "\n")

def read_text_from_image(img_name):
    # ocr = ocrmac.OCR(img_name, recognition_level='fast', language_preference=['en-US']) 
    ocr = ocrmac.OCR(img_name, recognition_level='accurate', language_preference=['en-US']) 
    data = ocr.recognize()

    #image = ocr.annotate_PIL()
    #image.show()

    data = sorted(data, key=lambda x: x[2][0] + int((1 - x[2][1]) * 5) * 1000 )
    print(data)
    p = [d[0].lower() for d in data if d[1] >= 0.01]
    p = [replace_dict.get(x, x) for x in p]

    # Hack
    p = [x.replace(".", "") for x in p]
    text = ' '.join(p) 
    return text

def def_logo_function(text):
    assert text.startswith("to")
    assert text.endswith("end")

    name = text.split(" ")[1] # first word should be to
    
    # insert a newline before end
    text = text.replace("end", "\nend")

    # insert a newline after the name of the function and possible arguments
    text = re.sub(r'(to [^:]*(:[^ ]*)*)', r'\1\n', text)

    # make a file with the name of the function in the logo dir
    with open(logo_folder + os.sep + name + ".logo", "w") as f:
        f.write(text)

    # write the text to the file
    send_to_logo("load \"" + name + ".logo")

def webcam_loop():
    cap = cv2.VideoCapture(1) 
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    while True:
    # Capture frame-by-frame
        ret, frame = cap.read()

        # Check if frame is read correctly
        if not ret:
            print("Failed to grab frame")
            break

        cv2.imshow('Webcam Live', frame)

        key = cv2.waitKey(1)
        if key == ord('c'):
            # Save the captured frame to an image file
            cv2.imwrite('capture.jpg', frame)
            text = read_text_from_image('capture.jpg')
            send_to_logo(text)

        elif key == ord('q'):
            return

if __name__ == "__main__":
    setup()
    webcam_loop()