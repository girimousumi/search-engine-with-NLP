import pickle
from sklearn.metrics.pairwise import cosine_similarity
import nltk

def preprocess_query(query):
    stemmer = nltk.PorterStemmer()
    tokens = nltk.word_tokenize(query.lower())
    stop_words = set(nltk.corpus.stopwords.words('english'))
    tokens = [stemmer.stem(word) for word in tokens if word.isalnum() and word not in stop_words]
    return ' '.join(tokens)

def search_query(query):
    # Load the vectorizer, tfidf matrix, and document names
    with open('tfidf_matrix.pkl', 'rb') as f:
        tfidf_matrix = pickle.load(f)
    
    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    
    with open('doc_names.pkl', 'rb') as f:
        doc_names = pickle.load(f)
    
    # Preprocess the query
    processed_query = preprocess_query(query)
    query_vector = vectorizer.transform([processed_query])
    
    # Compute cosine similarity
    similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
    
    # Rank documents by similarity
    ranked_indices = similarities.argsort()[::-1]
    ranked_documents = [(doc_names[i], similarities[i]) for i in ranked_indices if similarities[i] > 0]
    
    return ranked_documents

if __name__ == "__main__":
    query = input("Enter your search query: ")
    results = search_query(query)
    
    if results:
        print("Search Results:")
        for doc_name, score in results:
            print(f"{doc_name} - Score: {score}")
    else:
        print("No relevant documents found.")
