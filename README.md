# movie-recommendation-systyem
This project is a hybrid movie recommendation system🎯 that combines machine learning (TF-IDF) 🤖 with real-time API integration (TMDB) 🌐 to deliver accurate and visually rich movie suggestions.

The system follows a modular architecture 🏗️ where the backend is built using FastAPI ⚡ for handling heavy computations and API calls, while the frontend is developed using Streamlit 🎨 to provide an interactive and user-friendly interface.

At its core, the system uses a content-based filtering approach 📊. Movie data such as overview, genres, and tagline 🎭 are preprocessed using NLP techniques:

🧹 Text cleaning
🚫 Stopword removal
🔄 Lemmatization

This processed text is converted into numerical form using TF-IDF vectorization 📈, and cosine similarity 📐 is applied to find movies with similar content.

To enhance the experience, the system integrates with the TMDB API 🎥, which provides:

🖼️ Movie posters
📅 Release dates
⭐ Ratings
🎭 Genre-based recommendations
🚀 Features of the System:
🔍 Search for any movie
🎯 Get similar movie recommendations (TF-IDF based)
🎭 Discover movies by genre
🖼️ View posters and detailed movie information
