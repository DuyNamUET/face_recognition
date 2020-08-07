import pyrealsense2 as rs
import cv2
import numpy as np
import face_recognition
import glob
import pickle
import os

def load_resource(dir, ext=["jpg", "png"]):
    if not os.path.exists(dir):
        print("No source directory.")
        return
    
    boxes = {}
    all_img_paths = []

    for i in glob.glob("{}/*/*".format(dir)):
        if i.split(".")[-1] in ext:
            all_img_paths.append(i)
    
    # print(all_img_paths)
    for img_path in all_img_paths:
        name = img_path.split("/")[1]
        img = cv2.imread(img_path)
        endcoding = face_recognition.face_encodings(img)[0]
        boxes[name] = endcoding
    
    pickle.dump(boxes, open("coords.txt", 'wb'))
        

def recognition(coords):
    # config depth and color
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 15)

    # initiaize variables
    face_locations = []

    # stream
    pipeline.start(config)

    name = []; encoding = []
    for key, value in coords.items():
        name.append(key)
        encoding.append(value)

    font = cv2.FONT_HERSHEY_SIMPLEX 
    try:
        while True:
            # wait for frames
            frames = pipeline.wait_for_frames()
            color_frame = frames.get_color_frame()
            if not color_frame:
                continue
            color_img = np.asanyarray(color_frame.get_data())
            
            face_locations = face_recognition.face_locations(color_img)

            if len(face_locations) != 0:
                unknown_encoding = face_recognition.face_encodings(color_img)[0]
                results = face_recognition.compare_faces(encoding, unknown_encoding)
                index = [i for i,x in enumerate(results) if x == True]

                for (t, r, b, l) in face_locations:
                    cv2.rectangle(color_img, (l, t), (r, b), (0,255,0), 3)
                    cv2.putText(color_img, name[index[0]], (l,t), font, 1, (0,255,0), 2, cv2.LINE_AA) 

            # show on screen
            cv2.imshow('', color_img)
            if cv2.waitKey(1) & 0xFF ==ord('q'):
                break

    finally:
        pipeline.stop()

if __name__ == "__main__":
    # Load all dataset to file
    load_resource(dir="dataset")
    
    coords = pickle.load(open("coords.txt", 'rb'))
    recognition(coords)