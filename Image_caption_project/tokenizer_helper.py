# tokenizer_helper.py

try:
    from tensorflow.keras.preprocessing.text import Tokenizer
    from tensorflow.keras.preprocessing.sequence import pad_sequences
except ImportError:
    print("❌ TensorFlow is not installed properly. Please run: pip install tensorflow")

import numpy as np

def create_tokenizer(captions):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(captions)
    return tokenizer

def create_sequences(tokenizer, max_length, captions_dict, features, vocab_size):
    X1, X2, y = [], [], []

    for img_id, captions in captions_dict.items():
        feature = features.get(img_id)
        if feature is None:
            continue

        for caption in captions:
            seq = tokenizer.texts_to_sequences([caption])[0]
            for i in range(1, len(seq)):
                in_seq, out_word = seq[:i], seq[i]
                in_seq = pad_sequences([in_seq], maxlen=max_length)[0]
                out_seq = np.zeros(vocab_size)
                out_seq[out_word] = 1.0  # one-hot encode

                X1.append(feature)
                X2.append(in_seq)
                y.append(out_seq)

    return np.array(X1), np.array(X2), np.array(y)