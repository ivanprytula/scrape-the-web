import requests
from bs4 import BeautifulSoup


def show_page(url: str):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    
    # page_body = soup.body
    # print(page_body)
    
    results = soup.find(name="h2", class_="header-h2 color-dark")
    print(results)


if __name__ == "__main__":
    show_page("https://dataforest.ai/")
