# Web scraping project

## High-level architecture

- **Web scraper**: You can use `Python` and `Beautifulsoup` to scrape data from websites that provide information. You can also use `Celery` to schedule periodic scraping tasks.
- **Database**: You can store the scraped data in a `PostgreSQL` database.
- **Data cleaning and adjustment**: You can use `Python` and `pandas` to clean and adjust the scraped data.
- **Map integration**: You can integrate an open-source map such as `Leaflet` into your web application.
- **Dashboard**: You can use `plotly` to create interactive visualizations of the scraped data.
- **Deployment**: You can deploy your web application on `AWS` using `Flask` and `Redis`.

#### Topics within "web scraping" epic

- static vs dynamic sites
- changing page structure
- authentication, hidden sites/pages

## Tutorials used for this project

- https://realpython.com/beautiful-soup-web-scraper-python/
  
### Project details: setup, run, troubleshooting

#### Local setup

- create virtual environment
- install `requests` library/package
- install `beautifulsoup4` library/package
- create `main.py`
- have fun `=)` 


#### Diff commands/helpers

```shell
time python fake_jobs_example.py

# real - time is the actual time elapsed during the execution of the script.
# user - time is the amount of CPU time spent in user-mode code (outside the kernel) within the process.
# sys  - time is the amount of CPU time spent in kernel-mode code (inside the kernel) within the process

real    0m8.756s
user    0m0.431s
sys     0m0.036s

python3 -m timeit '"-".join(str(n) for n in range(100))'



```

### Web tools

- [Web Formatter](https://webformatter.com)
- [JSON Formatter & Validator ](https://jsonformatter.curiousconcept.com/)
  
### Related Python packages

- [Pythonic HTML Parsing for Humans™](https://github.com/psf/requests-html)
- `Selenium`
