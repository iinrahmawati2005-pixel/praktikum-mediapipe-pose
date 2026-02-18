import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose #Inisialisasi MediaPipe Pose
pose = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0) #video dari Webcam

while True:
    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(img_rgb)

    if results.pose_landmarks:
        mp_draw.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        landmarks = results.pose_landmarks.landmark
        left_shoulder = landmarks[11]
        right_shoulder = landmarks[12]
        left_wrist = landmarks[15]
        right_wrist = landmarks[16]

        if left_wrist.y < left_shoulder.y:
            cv2.putText(img, "Tangan Kiri Terangkat",
                        (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (0, 255, 0),2)

        if right_wrist.y < right_shoulder.y:
            cv2.putText(img, "Tangan Kanan Terangkat",
                        (30, 90),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (0, 255, 0),2)

    cv2.imshow("Deteksi Angkat Tangan", img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


