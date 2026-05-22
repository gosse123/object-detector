import cv2,os

dossier_cascade = cv2.data.haarcascades

chemin_visage = os.path.join(dossier_cascade,'haarcascade_frontalface_default.xml')

cascadeClassifier = cv2.CascadeClassifier(chemin_visage)

#utilisation de la webcam 
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("problem avec la webcam")
    exit(1)

print("detection en cours.... ")
while True:
    ret,frame = cap.read()

    if not ret:
        print("impossible de recevoir le flux de la webcam")
        break

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    visages = cascadeClassifier.detectMultiScale(gray,scaleFactor = 1.1,minNeighbors=3,minSize=(30,30))

    for (x,y,w,h) in visages:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("detection de visage",frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()