import pytest
import requests

BASE_URL = "https://api.mangadex.org"

def test_success():
    print("Starting Testing")

# From src.manga_chapters.py file
def test_get_manga_by_name():
    full_url = f"{BASE_URL}/manga?title=bleach"

    response = requests.get(full_url)

    assert response is not None