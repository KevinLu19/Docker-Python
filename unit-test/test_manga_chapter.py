import pytest
import requests

BASE_URL = "https://api.mangadex.org"

def test_success():
    print("Starting Testing")

# From src.manga_chapters.py file
def test_get_manga_by_name():
    full_url = f"{BASE_URL}/manga?title=bleach"
    print (f"Full URL is: {full_url}")

    response = requests.get(full_url)

    result = response.json()

    # Parsing Results
    if result["data"]:
        manga_id = result["data"][0]["id"]

        manga_info_url = f"https://api.mangadex.org/manga/{manga_id}"
        manga_info_response = requests.get(manga_info_url)
        manga_info = manga_info_response.json()
        print (manga_info)
        
        assert result["data"] is not None
    else:
        raise None