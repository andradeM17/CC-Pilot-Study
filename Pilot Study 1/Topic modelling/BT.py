# BERTopic Simple Example
from bertopic import BERTopic
import pandas as pd

# Read CSV file
df = pd.read_csv("Topic modelling/documents.csv")
documents = df['Text'].dropna().tolist()

# Check documents
print(f"Loaded {len(documents)} documents")

# Train BERTopic model with better parameters
from sklearn.feature_extraction.text import CountVectorizer

# Create vectorizer that removes stop words and focuses on meaningful terms
vectorizer_model = CountVectorizer(
    stop_words="english", 
    min_df=1, 
    ngram_range=(1, 2),  # Include phrases
    max_features=1000
)

model = BERTopic(
    min_topic_size=2, 
    nr_topics="auto",
    vectorizer_model=vectorizer_model,
    verbose=True
)
topics, probs = model.fit_transform(documents)

# Get topic info
topic_info = model.get_topic_info()
print(f"\nFound {len(topic_info)-1} topics")  # -1 for outlier topic
print(topic_info)

# Show topics with their documents
for topic_id in range(len(topic_info)-1):
    words = model.get_topic(topic_id)
    if words:  # Skip empty topics
        topic_words = [word for word, score in words[:5]]
        print(f"\nTopic {topic_id}: {', '.join(topic_words)}")
        
        # Get all documents assigned to this topic
        topic_docs = [doc for i, doc in enumerate(documents) if topics[i] == topic_id]
        print(f"Number of documents: {len(topic_docs)}")
        
        # Show each document (truncated for readability)
        for i, doc in enumerate(topic_docs):
            print(f"  Doc {i+1}: {doc[:100]}...")
            print()