# Facebook_Scraper



This is a web scraping service that extracts comments and likes from a Facebook public page. It uses the FastAPI framework and PostgreSQL database to store the scraped data.

## RUN Facebook_Scraper

```
To start the scraper, run the following command:
git clone https://gitlab.com/YafetBA/facebook_scraper
cd facebook-scraper
docker-compose build
docker-compose up
```
## Testing
```
To run the tests for the scraper, use the following command:

docker-compose run scraper pytest

or using Postman 

http://0.0.0.0:8000/scrape?page_name=facebook&db_name=FacebookData&db_user=postgres&db_password=admin&db_host=db
```
![Postman](/images/cp1.jpg)

## Extracted data

![data](/images/cp2.jpg)





