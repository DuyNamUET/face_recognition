import cv2
import numpy as np
import face_recognition

def detect_using_realsense():
    import pyrealsense2 as rs
    # config depth and color
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

    # initiaize variables
    face_locations = []

    # stream
    pipeline.start(config)

    try:
        while True:
            # wait for frames
            frames = pipeline.wait_for_frames()
            color_frame = frames.get_color_frame()
            if not color_frame:
                continue
            
            color_img = np.asanyarray(color_frame.get_data())
            
            face_locations = face_recognition.face_locations(color_img)
            for (t, r, b, l) in face_locations:
                size = (b-t)*(r-l)
                print(size)
                if size < 2000:
                    continue
                cv2.rectangle(color_img, (l, t), (r, b), (0, 255, 0), 3)

            # show on screen
            cv2.imshow('', color_img)
            if cv2.waitKey(1) & 0xFF ==ord('q'):
                break

    finally:
        pipeline.stop()

def detect_using_webcam():
    cap = cv2.VideoCapture(0)

    while True:
        _, image = cap.read()

        face_locations = face_recognition.face_locations(image)
        for (t, r, b, l) in face_locations:
            size = (b-t)*(r-l)
            print(size)
            if size < 2000:
                continue
            cv2.rectangle(image, (l, t), (r, b), (0, 255, 0), 3)

        cv2.imshow("", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_using_webcam()
    # detect_using_realsense()