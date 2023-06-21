from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"

page = urlopen(url)

print(page)  # <http.client.HTTPResponse object at 0x7fd8441d9030>
