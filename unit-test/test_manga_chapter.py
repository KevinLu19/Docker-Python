import requests

BASE_URL = "https://api.mangadex.org"

def test_success():
    print("Starting Testing")


# From src.manga_chapters.py file
def test_get_manga_by_name():
    anime_title = "bleach"
    request = requests.get(f"{BASE_URL}/manga", params={"title": anime_title, "limit": 5})
    response = request.json()

    if request:
        for manga in response["data"]:
            attributes = manga["attributes"]["title"]

            print (attributes["en"])

        for status in response["data"]:
            manga_status = status["attributes"]["status"]
            print("Status:", manga_status)
        
        for chpt in response["data"]:
            last_chpt =  chpt["attributes"]["lastChapter"]
            print("Last Chapter:", last_chpt)
        
    assert request.json()["data"] is not None