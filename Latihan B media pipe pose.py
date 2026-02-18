import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose #inisial media pipe pose
pose = mp_pose.Pose()
mdraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0) #video dari webcam

while True:
    success, img = cap.read() #pembaca image
    if not success:
        break

    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #konversi warna dari bgr ke rgb
    hasil = pose.process(imgrgb) #ekstraksi dari image

    if hasil.pose_landmarks:
        mdraw.draw_landmarks(img, hasil.pose_landmarks, mp_pose.POSE_CONNECTIONS) #menggambar koneksi landmark

        for id, lm in enumerate(hasil.pose_landmarks.landmark):
            print(id, lm.x, lm.y)

    cv2.imshow("webcam", img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


