import string

# Load the caption text file into a single string
def load_doc(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"❌ File not found: {filename}")
        return ""

# Clean and preprocess the captions
def clean_captions(doc):
    cleaned = []
    for line in doc.strip().split('\n'):
        if ',' not in line:
            continue  # Skip malformed lines
        img, caption = line.split(',', 1)
        caption = caption.lower()
        caption = caption.translate(str.maketrans('', '', string.punctuation))
        caption = 'startseq ' + caption.strip() + ' endseq'
        cleaned.append((img.strip(), caption))
    return cleaned

#test block
if __name__ == '__main__':
    doc = load_doc('data/captions.txt')  # Ensure this path is correct
    cleaned = clean_captions(doc)

    print("✅ Showing 5 cleaned captions:")
    for i in range(min(5, len(cleaned))):
        print(cleaned[i])
