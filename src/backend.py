from flask import Flask, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Load and process dataset
df = pd.read_csv("public/Updated_Netflix.csv")
df["tags"] = df["title"] + df["description"] + df["type"] + df["listed_in"]

vec = TfidfVectorizer(stop_words='english')
vector = vec.fit_transform(df["tags"])
similarity = cosine_similarity(vector)

# Find top 5 recommendations
def find(movie):
    movie = movie.lower()
    matches = df[df["title"].str.lower() == movie]
    if matches.empty:
        return ["Movie not found"]
    
    index = matches.index[0]
    similarity_scores = list(enumerate(similarity[index]))
    sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    top_5 = sorted_scores[1:6]
    movie_indices = [i[0] for i in top_5]
    return df['title'].iloc[movie_indices].tolist()

# Fetch posters from OMDB
def show_posters(movie_list):
    posters = []
    for title in movie_list:
        url = f"https://www.omdbapi.com/?t={title}&apikey=857db68"
        data = requests.get(url).json()
        poster_url = data.get("Poster", "N/A")
        posters.append(poster_url)
    return posters

# Flask endpoint
@app.route("/<movie>")
def recommend(movie):
    top = find(movie)
    if top == ["Movie not found"]:
        return jsonify({"top": top, "poster": []})
    
    posters = show_posters(top)
    return jsonify({"top": top, "poster": posters})

if __name__ == "__main__":
    app.run(debug=True)
