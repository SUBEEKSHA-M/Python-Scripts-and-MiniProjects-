# extract_features.py

from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
import pickle

def extract_features(directory):
    model = InceptionV3(weights='imagenet')
    model = Model(inputs=model.input, outputs=model.layers[-2].output)

    features = {}
    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            path = os.path.join(directory, filename)
            image = load_img(path, target_size=(299, 299))
            image = img_to_array(image)
            image = np.expand_dims(image, axis=0)
            image = preprocess_input(image)
            feature = model.predict(image, verbose=0)
            features[filename] = feature[0]
    
    return features

if __name__ == '__main__':
    features = extract_features('data/images')
    with open('features.pkl', 'wb') as f:
        pickle.dump(features, f)
    print("✅ features.pkl saved.")
