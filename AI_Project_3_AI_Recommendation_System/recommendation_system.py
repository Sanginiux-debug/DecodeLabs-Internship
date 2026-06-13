import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("=" * 60)
print("AI COURSE RECOMMENDATION SYSTEM")
print("=" * 60)

# Load dataset
df = pd.read_csv("courses.csv")

print("\nAvailable Skills:")
all_skills = set()

for skills in df["Skills"]:
    for skill in skills.split():
        all_skills.add(skill)

print(", ".join(sorted(all_skills)))

# User input
user_input = input(
    "\nEnter your interests (space separated): "
).lower()

# Create combined corpus
corpus = list(df["Skills"])
corpus.append(user_input)

# TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)

# Similarity
similarity_scores = cosine_similarity(
    tfidf_matrix[-1],
    tfidf_matrix[:-1]
)

df["Similarity Score"] = similarity_scores[0]

recommendations = df.sort_values(
    by="Similarity Score",
    ascending=False
)

print("\nTop Recommendations")
print("-" * 60)

for index, row in recommendations.head(5).iterrows():
    print(
        f"{row['Course']} "
        f"(Score: {row['Similarity Score']:.2f})"
    )
