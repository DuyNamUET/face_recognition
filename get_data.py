import os
import cv2
import numpy as np
import face_recognition

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    count = 0
    
    # Create new dataset
    img_dir = ""
    while True:
        name = input("Enter your name: ")
        img_dir = ("dataset/"+name).replace(' ', '_')
        if os.path.exists("{}".format(img_dir)):
            print("The name is used. Please enter your name again.")
            continue
        else:
            os.makedirs(img_dir)
            break

    while True:
        _, image = cap.read()
        face_locations = face_recognition.face_locations(image)
        for (t, r, b, l) in face_locations:
            cv2.rectangle(image, (l, t), (r, b), (0, 255, 0), 3)
        cv2.imshow(name, image)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or count == 5:
            break
        if key == ord('c'):
            cv2.imwrite("{}/{}.png".format(img_dir,count), image)
            count += 1
