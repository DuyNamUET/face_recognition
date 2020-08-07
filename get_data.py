import os
import pyrealsense2 as rs
import cv2
import numpy as np

def get_data():
    # Create new dataset
    name = ""
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

    cap = cv2.VideoCapture()
    while True:
        _, color_img = cap.read()
        have_face = False
        face_locations = face_recognition.face_locations(color_img)

        if len(face_locations) == 1:
            have_face = True

        for (t, r, b, l) in face_locations:
            size = (b-t)*(r-l)
            print(size)
            if size < 2000:
                continue
            
            # cv2.rectangle(color_img, (l, t), (r, b), (0, 255, 0), 3)
        
        cv2.imshow(name, color_img)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        if key == ord('c') and have_face:
            cv2.imwrite("{}/{}.png".format(img_dir,name.replace(' ', '_')), color_img)
            break

def get_data_realsense():
    import face_recognition

    # config depth and color
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 15)

    # initiaize variables
    face_locations = []

    # stream
    pipeline.start(config)

    # Create new dataset
    name = ""
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

    try:
        while True:
            have_face = False
            # wait for frames
            frames = pipeline.wait_for_frames()
            color_frame = frames.get_color_frame()
            if not color_frame:
                continue
            
            color_img = np.asanyarray(color_frame.get_data())
            
            face_locations = face_recognition.face_locations(color_img)

            if len(face_locations) == 1:
                have_face = True

            for (t, r, b, l) in face_locations:
                size = (b-t)*(r-l)
                print(size)
                if size < 2000:
                    continue
                
                # cv2.rectangle(color_img, (l, t), (r, b), (0, 255, 0), 3)
            
            cv2.imshow(name, color_img)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            if key == ord('c') and have_face:
                cv2.imwrite("{}/{}.png".format(img_dir,name.replace(' ', '_')), color_img)
                break
    finally:
        pipeline.stop()

if __name__ == "__main__":
    get_data()