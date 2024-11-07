import os
import nltk

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

nltk.download('stopwords')

def preprocess(text):
    stemmer = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    tokens = nltk.word_tokenize(text.lower())
    tokens = [stemmer.stem(word) for word in tokens if word.isalnum() and word not in stop_words]
    return ' '.join(tokens)

def index_documents(doc_folder='C:/Users/naman/OneDrive/Desktop/NLP/SEARCH ENGINE/documents'):

    documents = []
    doc_names = []
    
    for file_name in os.listdir(doc_folder):
        if file_name.endswith(".txt"):
            with open(os.path.join(doc_folder, file_name), 'r', encoding='utf-8') as file:
                content = file.read()
                processed_content = preprocess(content)
                documents.append(processed_content)
                doc_names.append(file_name)
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    # Save the vectorizer and tfidf matrix
    with open('tfidf_matrix.pkl', 'wb') as f:
        pickle.dump(tfidf_matrix, f)
    
    with open('vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)
    
    with open('doc_names.pkl', 'wb') as f:
        pickle.dump(doc_names, f)
    
    print("Indexing completed successfully!")

if __name__ == "__main__":
    index_documents()
