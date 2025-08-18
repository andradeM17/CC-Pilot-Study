import pandas as pd
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# Load documents
df = pd.read_csv("Pilot Study 2/Topic modelling/documents.csv")
documents = df['Text'].astype(str).tolist()

# Vectorize the documents
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

# Fit LDA
n_topics = 5  # You can change this
lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
lda.fit(X)

# Print top words for each topic and first 100 chars of each document in topic
n_top_words = 10
feature_names = vectorizer.get_feature_names_out()
doc_topic = lda.transform(X)
doc_main_topic = np.argmax(doc_topic, axis=1)

for topic_idx, topic in enumerate(lda.components_):
    print(f"Topic #{topic_idx + 1}:")
    print("Top words:", " ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))
    # Print only documents where this is the main topic
    for doc_idx, main_topic in enumerate(doc_main_topic):
        if main_topic == topic_idx:
            snippet = documents[doc_idx][:100].replace('\n', ' ')
            print(f"  Doc {doc_idx + 1}: {snippet}...")
    print("\n")