import tensorflow as tf
import cv2
import numpy as np

# Load trained model
model = tf.keras.models.load_model("emotion_model.h5")

# Emotion labels as per FER2013
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Load image for testing (replace with your image path)
img_path = "test_face.jpg"  # <- You must have a test image in the same folder
img = cv2.imread(img_path)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
resized = cv2.resize(gray, (48, 48))

# Normalize and reshape
normalized = resized / 255.0
reshaped = np.reshape(normalized, (1, 48, 48, 1))

# Predict
result = model.predict(reshaped)
emotion_index = np.argmax(result)
predicted_emotion = emotion_labels[emotion_index]

print(f"✅ Predicted Emotion: {predicted_emotion}")
