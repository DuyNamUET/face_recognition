import pyrealsense2 as rs
import cv2
import numpy as np
import face_recognition

if __name__ == "__main__":
    # config depth and color
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 15)

    # initiaize variables
    face_locations = []

    # stream
    pipeline.start(config)

    nam_img = cv2.imread("dataset/Nam/0.png")
    nam_encoding = face_recognition.face_encodings(nam_img)[0]
    print(nam_encoding)
    try:
        while True:
            # wait for frames
            frames = pipeline.wait_for_frames()
            color_frame = frames.get_color_frame()
            if not color_frame:
                continue
            
            color_img = np.asanyarray(color_frame.get_data())
            
            face_locations = face_recognition.face_locations(color_img)
            # for (t, r, b, l) in face_locations:
            #     size = (b-t)*(r-l)
            #     print(size)
            #     if size < 2000:
            #         continue
            #     cv2.rectangle(color_img, (l, t), (r, b), (0, 255, 0), 3)
            if face_locations != None:
                unknown_encoding = face_recognition.face_encodings(color_img)[0]
                print(face_recognition.compare_faces([nam_encoding], unknown_encoding))

            # show on screen
            cv2.imshow('', color_img)
            if cv2.waitKey(1) & 0xFF ==ord('q'):
                break

    finally:
        pipeline.stop()