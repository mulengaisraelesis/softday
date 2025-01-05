import cv2 as cv
import serial
import time

faces = []
last_detected_state = False

# Initialiser la communication série avec arduino
arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # Ajuste le port série ici
time.sleep(2)  # Attendre que la communication soit établie

# Charger le classificateur de visages
face_classifier = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialiser la capture vidéo
video_capture = cv.VideoCapture(4)  # Assure-toi que l'index de la webcam est correct
video_capture.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
video_capture.set(cv.CAP_PROP_FRAME_HEIGHT, 720)

def detect_bounding_box(vid):
    gray_image = cv.cvtColor(vid, cv.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))  # Ajuste cette valeur selon les besoins

    for (x, y, w, h) in faces:
        cv.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return vid, len(faces) > 0

def wait_before_execution():
    for i in range(10):
        print(f"Starting in {10 - i} seconds")
        time.sleep(1)

while True:
    result, video_frame = video_capture.read()
    if not result:
        break
    # Détecter les visages et obtenir l'image avec les bounding boxes
    video_frame, faces_detected = detect_bounding_box(video_frame.copy())  # Utiliser une copie pour la détection

    # Envoyer les données à arduino uniquement si l'état de détection change
    if faces_detected and not last_detected_state:
        arduino.write(b'1')
        last_detected_state = True
        wait_before_execution()
    elif not faces_detected and last_detected_state:
        arduino.write(b'0')
        last_detected_state = False
    
    # Afficher la vidéo en couleur dans une fenêtre
    cv.imshow('My Face Detection', video_frame)
    if cv.waitKey(10) & 0xFF == ord('q'):
        break

# Libérer la capture vidéo et fermer les fenêtres
video_capture.release()
cv.destroyAllWindows()
arduino.close()
