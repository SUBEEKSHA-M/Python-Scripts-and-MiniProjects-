# train_model.py

from caption_preprocessing import load_doc, clean_captions
from tokenizer_helper import create_tokenizer, create_sequences
from model_definition import define_model
import pickle
import numpy as np

# Step 1: Load and clean captions
doc = load_doc('data/captions.txt')
cleaned = clean_captions(doc)

# Step 2: Organize captions by image filename
captions_dict = {}
for img, cap in cleaned:
    captions_dict.setdefault(img, []).append(cap)

# Step 3: Load extracted features
with open('features.pkl', 'rb') as f:
    features = pickle.load(f)

# Step 4: Tokenizer and sequence setup
all_captions = [c for caps in captions_dict.values() for c in caps]
tokenizer = create_tokenizer(all_captions)
vocab_size = len(tokenizer.word_index) + 1
max_length = max(len(c.split()) for c in all_captions)

# Save tokenizer for later use
with open('tokenizer.pkl', 'wb') as f:
    pickle.dump(tokenizer, f)

# Step 5: Create training sequences
X1, X2, y = create_sequences(tokenizer, max_length, captions_dict, features, vocab_size)

# Step 6: Define and train the model
model = define_model(vocab_size, max_length)
model.fit([X1, X2], y, epochs=20, batch_size=4)

# Step 7: Save trained model
model.save('caption_model.h5')
print("✅ Model training complete and saved as caption_model.h5")
