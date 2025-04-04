# Netflix TV Shows & Movie Recommendation System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## 📌 Introduction
This project is a **Netflix TV Shows & Movie Recommendation System** that helps users discover movies and TV shows based on their preferences. The recommendation engine is built using **Python, pandas, NumPy, scikit-learn**, and other ML techniques.

## 🚀 Features
- 🎯 **Content-Based Filtering**: Recommends shows/movies similar to the user's choice.
- 🤝 **Collaborative Filtering**: Suggests based on user preferences.
- 🔀 **Hybrid Recommendation**: Combines multiple recommendation techniques.
- 🧹 **Data Preprocessing**: Cleans and transforms data for better accuracy.
- 🌐 **Web Interface**: Uses Flask/Streamlit for UI (if implemented).

## 🛠️ Technologies Used
| Technology | Purpose |
|------------|---------|
| **Python** | Core language |
| **pandas, NumPy** | Data manipulation |
| **scikit-learn** | Machine learning models |
| **matplotlib, seaborn** | Data visualization |
| **Flask/Streamlit** | Web application |
| **Jupyter Notebook** | Development & visualization |

## 📂 Dataset
The dataset includes Netflix TV shows and movies with features such as:
- 🎬 **Title**
- 🎭 **Genre**
- 🎥 **Director**
- 🌟 **Cast**
- 📝 **Description**
- ⭐ **Rating**
- 📅 **Release Year**
- ⏳ **Duration**

## 📌 Installation
To run the project, install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 How to Use
### Clone the Repository
```bash
git clone https://github.com/prajjukorban/Netflix-Tv-Shows-Movie-Recommendation-System.git
cd Netflix-Tv-Shows-Movie-Recommendation-System
```

### Run the Jupyter Notebook
```bash
jupyter notebook
```

### Run the Web App (if applicable)
```bash
python app.py  # Flask
streamlit run app.py  # Streamlit
```

## 📊 Recommendation Techniques
### Content-Based Filtering
- Uses **TF-IDF Vectorization** and **Cosine Similarity**.
- Finds similar movies based on descriptions and genres.

### Collaborative Filtering
- Uses **Singular Value Decomposition (SVD)** from the Surprise library.
- Recommends based on user preferences and behavior.

### Hybrid Model
- Combines both approaches for improved recommendations.

## 📈 Performance Metrics
- 📉 **RMSE (Root Mean Square Error)**
- 🎯 **Precision, Recall**
- ✅ **User Satisfaction Evaluation**

## 🎯 Future Enhancements
- 🚀 Add **Deep Learning-based recommendations**.
- 🔗 Integrate with **real-time Netflix APIs**.
- 🎨 Improve **UI/UX** for a better user experience.

## 👨‍💻 Author
**Prajwal K.**

## 🔗 Repository
[GitHub Repo](https://github.com/prajjukorban/Netflix-Tv-Shows-Movie-Recommendation-System)

## 📜 License
This project is open-source under the **MIT License**.
