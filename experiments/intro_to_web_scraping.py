# from urllib.request import urlopen
from urllib.request import urlopen
from browser import document, ajax

output = document["scraped-result"]


def extract_html(url: str):
    page = urlopen(url)

    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    print(html)
    return html


def show(req):
    print(req.text)


# @bind("#scrape-url", "click")
def scrape_url(event):
    input_url = document["exampleInputURL"].value
    # print(input_url)

    # with urlopen(input_url) as f:
    #     content = f.read()

    # input_selector = document["exampleInputSelector"].value

    req = ajax.Ajax()
    req.bind("complete", show)
    req.open("GET", input_url)
    req.send()
    output.html <= req.read()

    # raw_html = extract_html(input_url)

    # document["scraped-result"] <= raw_html


document["scrape-url"].bind("click", scrape_url)


url = "http://olympus.realpython.org/profiles/aphrodite"


# print(page)  # <http.client.HTTPResponse object at 0x7fd8441d9030>
