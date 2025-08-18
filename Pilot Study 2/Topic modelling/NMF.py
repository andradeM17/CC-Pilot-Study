import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

# --- Load data ---
# abc.csv should have a column named 'text'
df = pd.read_csv("Pilot Study 2/Topic modelling/documents.csv")
documents = df['Text'].fillna("").tolist()

# --- TF-IDF transformation ---
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

# --- Fit NMF ---
n_topics = 2  # change as needed
nmf_model = NMF(n_components=n_topics, random_state=42)
W = nmf_model.fit_transform(X)

# --- Display top words for each topic ---
def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        top_features_indices = topic.argsort()[:-no_top_words - 1:-1]
        top_features = [feature_names[i] for i in top_features_indices]
        print(f"\nTopic {topic_idx + 1}:\n" + ", ".join(top_features))

print("\n=== Topics and Top Words ===")
display_topics(nmf_model, vectorizer.get_feature_names_out(), no_top_words=5)

# --- Assign each document to a topic ---
doc_topics = W.argmax(axis=1) + 1  # +1 for 1-based topic index

# Group documents by topic
topic_groups = {}
for i, topic_num in enumerate(doc_topics):
    topic_groups.setdefault(topic_num, []).append(documents[i])

print("\n=== Documents Grouped by Topic ===")
for topic_num, docs in topic_groups.items():
    print(f"\nTopic {topic_num}:")
    for doc in docs:
        print(f" - {doc[:100]}{'...' if len(doc) > 100 else ''}")
