import cv2
import easyocr
from PIL import Image
from ocrmac import ocrmac

# Initialize the webcam
cap = cv2.VideoCapture(1)  # '0' is usually the default value for the primary webcam
reader = easyocr.Reader(['en'])  # 'en' is for English

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if frame is read correctly
    if not ret:
        print("Failed to grab frame")
        break

    # Display the resulting frame
    cv2.imshow('Webcam Live', frame)

    # Wait for a key press
    key = cv2.waitKey(1)

    # If 'c' is pressed, capture the frame and perform OCR
    if key == ord('c'):
        # Save the captured frame to an image file
        cv2.imwrite('capture.jpg', frame)
        annotations = ocrmac.OCR('capture.jpg').recognize()
        print("ocrmac")
        print(annotations)

    # If 'q' is pressed, break from the loop
    elif key == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
