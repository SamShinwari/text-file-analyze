import re
from collections import Counter

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_sentences(text):
    sentences = re.split(r'[.!?]+', text)
    sentences = [s for s in sentences if s.strip()]
    return len(sentences)

def count_characters(text):
    return len(text)

def most_common_words(text, n=5):
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    return word_counts.most_common(n)

def analyze_text(filepath):
    text = read_file(filepath)
    
    print("📊 Text Analysis Results:\n")
    print(f"Total Words: {count_words(text)}")
    print(f"Total Sentences: {count_sentences(text)}")
    print(f"Total Characters: {count_characters(text)}")
    
    print("\n🔥 Most Common Words:")
    for word, freq in most_common_words(text):
        print(f"{word}: {freq}")

if __name__ == "__main__":
    file_path = "data/sample.txt"
    analyze_text(file_path)
