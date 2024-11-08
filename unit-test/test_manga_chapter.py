import pytest
import requests

BASE_URL = "https://api.mangadex.org"

# From src.manga_chapters.py file
def TestGetMangaByName(name : str):
    full_url = f"{BASE_URL}/manga?title={name}"

    response = requests.get(full_url)

    assert response is not None