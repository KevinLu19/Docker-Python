from src.mangadex_api import manga_id
from src.mangadex_api import manga_chapters


if __name__ == "__main__":
    manga_chapter = manga_chapters.MangaChapter()
    
    while True:
        userinput = input("Enter manga name to get information. (press q to exit): ")
        
        if userinput == "Q" or userinput == "q":
            break
        
        # Feeds user input into the manga title class.
        manga_chapter.GetMangaByName(userinput)