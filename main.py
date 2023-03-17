import cv2
import pytesseract

# Path to the Tesseract executable, change this to the path on your system
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Initialize the video capture device (use 0 for webcam or path to a video file)
cap = cv2.VideoCapture(0)

# Define the region of interest (ROI) for the car number plate
plate_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

while True:
    # Read the next frame from the video feed
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect the car number plate in the ROI
    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    # Iterate over the detected plates and apply OCR
    for (x, y, w, h) in plates:
        plate_roi = gray[y:y+h, x:x+w]
        plate_text = pytesseract.image_to_string(plate_roi, config='--psm 11')

        # Draw the plate text on the frame
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, plate_text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Show the frame
    cv2.imshow('Car Number Plate Scanner', frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture device and close all windows
cap.release()
cv2.destroyAllWindows()
