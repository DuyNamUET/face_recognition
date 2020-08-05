import cv2
import numpy as np
import face_recognition

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    # initiaize variables
    face_locations = []
    while True:
        ret, frame = cap.read()
        face_locations = face_recognition.face_locations(frame, model='cnn')
        for (t, r, b, l) in face_locations:
            cv2.rectangle(frame, (l, t), (r, b), (0, 255, 0), 3)

        # show on screen
        cv2.imshow('', frame)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()