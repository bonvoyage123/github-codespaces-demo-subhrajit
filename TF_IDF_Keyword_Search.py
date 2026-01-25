documents = [
    "AWS Lambda is a serverless compute service",
    "Python is widely used for data engineering",
    "TF IDF is a technique for keyword search",
    "Data engineering pipelines run on AWS",
    "Serverless architectures reduce operational overhead"
]

from sklearn.feature_extraction.text import *

vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english"
)

tfidf_matrix = vectorizer.fit_transform(documents)

query = "AWS serverless data pipeline"

query_vector = vectorizer.transform([query])

from sklearn.metrics.pairwise import cosine_similarity

similarity_scores = cosine_similarity(query_vector, tfidf_matrix)[0]

results = sorted(
    enumerate(similarity_scores),
    key=lambda x: x[1],
    reverse=True
)

for idx, score in results:
    print(f"Score: {score:.3f} | Document: {documents[idx]}")

