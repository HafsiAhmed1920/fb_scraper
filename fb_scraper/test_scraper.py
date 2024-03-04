import requests

def test_scrape_endpoint():
    url = "http://0.0.0.0:8000/scrape"
    data = {
        "page_name": "facebook",
        "db_name": "FacebookData",
        "db_user": "postgres",
        "db_password": "admin",
        "db_host": "0.0.0.0"
    }
    response = requests.post(url, json=data)
    assert response.status_code == 200
    assert response.json() == {"message": "Scraping complete."}