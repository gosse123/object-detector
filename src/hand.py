import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

model_path = 'models/hand_landmarker.task'
# Configuration du Hand Landmarker
base_options = python.BaseOptions(model_asset_path=model_path)
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1,
    min_hand_detection_confidence=0.7,
    min_hand_presence_confidence=0.7
)

detector = vision.HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir en RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

    # Détection
    result = detector.detect(mp_image)

    # Dessin des landmarks
    if result.hand_landmarks:
        for hand_landmarks in result.hand_landmarks:
            h, w, _ = frame.shape
            
            # Dessiner les points et connexions
            for landmark in hand_landmarks:
                cx = int(landmark.x * w)
                cy = int(landmark.y * h)
                cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)
            
            # Bout de l'index (landmark 8)
            index_tip = hand_landmarks[8]
            cx = int(index_tip.x * w)
            cy = int(index_tip.y * h)
            cv2.circle(frame, (cx, cy), 12, (255, 0, 0), -1)

    cv2.imshow("Hand Detection - MediaPipe Tasks", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()