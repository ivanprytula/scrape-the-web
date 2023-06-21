"""
PEP 418 describes some of the rationale behind introducing these functions.
It includes the following short descriptions:

- time.monotonic(): timeout and scheduling, not affected by system clock updates
- time.perf_counter(): benchmarking, most precise clock for short period
- time.process_time(): profiling, CPU time of the process
As you can tell, perf_counter() is usually the best choice for your Python timer.

"""
import atexit
import os
import time
from contextlib import contextmanager

import requests
from bs4 import BeautifulSoup


@contextmanager
def file_manager(filename, mode):
    """Just a fancy wrapper for open() to see progress in terminal."""
    print("The file is opening...")
    file = open(filename, mode)
    yield file
    print("The file is closing...")
    file.close()


def main():
    URL = "https://realpython.github.io/fake-jobs/"

    tic = time.perf_counter()  # performance counter that’s well-suited for timing parts of your code

    page = requests.get(URL)

    # with file_manager("test.html", "w") as f:
    #     f.write(page.text)

    # .content attribute holds raw bytes, which can be decoded better than
    # the text representation using `.text` attribute
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")
    # print(results.prettify())

    # job_elements = results.find_all("div", class_="card-content")
    # python_jobs = results.find_all("h2", string="Python")  # looks for that string exactly
    # print(python_jobs)  # -> []

    python_jobs = results.find_all(name="h2", string=lambda text: "python" in text.lower())

    python_job_elements = [h2_element.parent.parent.parent for h2_element in python_jobs]

    # for job_element in job_elements:
    # for job_element in python_jobs:
    for job_element in python_job_elements:
        # print(job_element, end="\n" * 2)

        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")

        link_url = job_element.find_all("a")[1]["href"]  # or we can use -1 if desired link will become "last in row"
        print(f"Apply here: {link_url}\n")

        try:
            print(title_element.text.strip())
            print(company_element.text.strip())
            print(location_element.text.strip())
            print()
        except AttributeError:
            print("Check the way you search and parse elements on the page")
        except Exception:
            # very brutal exit w/o explanation;))
            # just to check that cleanup function upon_normal_script_execution() won't be executed
            os._exit(1)

    toc = time.perf_counter()
    print(f"Downloaded & parsed page in {toc - tic:0.4f} seconds")
    # Downloaded & parsed page in 8.4975 seconds
    # NB: almost the same as measured with Linux shell's CLI tool 'time':
    # real    0m8.756s


@atexit.register
def upon_normal_script_execution():
    print(
        """
          Scraping script finished without errors.
          Script itself is OK, but what about results?
          Check them!
        """
    )


if __name__ == "__main__":
    main()
