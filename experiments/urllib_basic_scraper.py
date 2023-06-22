from urllib.request import urlopen
import re
from bs4 import BeautifulSoup


def get_aphrodite():
    url = "http://olympus.realpython.org/profiles/aphrodite"

    page = urlopen(url)

    # print(page)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    print(html)

    title_index = html.find("<title>")
    start_index = title_index + len("<title>")

    end_index = html.find("</title>")
    title = html[start_index:end_index]
    print(title)

    # ==================
    re.findall("ab*c", "ac")
    re.findall("ab*c", "ABC", re.IGNORECASE)
    re.findall("a.c", "acc")
    re.findall("a.*c", "abbc")
    match_results = re.search(pattern="ab*c", string="ABC", flags=re.IGNORECASE)
    match_results.group()  # 'ABC'

    string = "Everything is <replaced> if it's in <tags>."
    string = re.sub(pattern="<.*>", repl="ELEPHANTS", string=string)
    # this is "greedy" example, meaning regex try to find the longest possible match when characters like * are used:
    # from the beginning of <replaced> to the end of <tags>
    # * matches the previous token between zero and unlimited times, as many times as possible, giving back as needed (greedy)
    print(string)  # 'Everything is ELEPHANTS.'

    # "non-greedy" example
    string = re.sub("<.*?>", "ELEPHANTS", string, 2)
    # *? matches the previous token between zero and unlimited times, as few times as possible, expanding as needed (lazy)
    # >>> "Everything is ELEPHANTS if it's in ELEPHANTS."


# def get_dionysus():
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title)  # Remove HTML tags

    # print(title)


# get_dionysus()
