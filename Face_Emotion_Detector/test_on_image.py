import tensorflow as tf
import cv2
import numpy as np

# Load model
model = tf.keras.models.load_model("emotion_model.h5")
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Load image
img_path = "test_face.jpg"
img = cv2.imread(img_path)

if img is None:
    print("❌ Error: Image not found.")
    exit()

# Load Haarcascade for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

if len(faces) == 0:
    print("❌ No face detected.")
else:
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        resized = cv2.resize(roi_gray, (48, 48))
        normalized = resized / 255.0
        reshaped = np.reshape(normalized, (1, 48, 48, 1))

        result = model.predict(reshaped)
        emotion = emotion_labels[np.argmax(result)]
        print(f"✅ Predicted Emotion: {emotion}")
