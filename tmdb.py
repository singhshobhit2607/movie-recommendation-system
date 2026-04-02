import requests
import os

TMDB_API_KEY = os.getenv("TMDB_API_KEY", "")
BASE_URL     = "https://api.themoviedb.org/3"
IMG_BASE     = "https://image.tmdb.org/t/p/w500"
PLACEHOLDER  = "https://placehold.co/200x300/1a1a2e/white?text=No+Poster"


def _safe_get(url: str, params: dict) -> dict:
    try:
        r = requests.get(url, params=params, timeout=5)
        r.raise_for_status()
        return r.json()
    except Exception:
        return {}


def get_movie_details(title: str) -> dict:
    """Search TMDB for a movie and return poster + meta."""
    if not TMDB_API_KEY:
        return {"poster_url": PLACEHOLDER}

    data = _safe_get(
        f"{BASE_URL}/search/movie",
        {"api_key": TMDB_API_KEY, "query": title, "language": "en-US"},
    )
    results = data.get("results", [])
    if not results:
        return {"poster_url": PLACEHOLDER}

    m = results[0]
    return {
        "tmdb_id":      m.get("id"),
        "poster_url":   (IMG_BASE + m["poster_path"]) if m.get("poster_path") else PLACEHOLDER,
        "release_year": (m.get("release_date") or "")[:4],
        "tmdb_rating":  round(m.get("vote_average", 0), 1),
    }