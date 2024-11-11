import requests

BASE_URL = "https://api.mangadex.org"

def test_success():
    print("Starting Testing")

# From src.manga_chapters.py file
def test_get_manga_by_name():
    anime_title = "bleach"
    request = requests.get(f"{BASE_URL}/manga", params={"title": anime_title})
    
    if request:
        print ([manga["id"] for manga in request.json()["data"]])
        
    assert request.json()["data"] is not None