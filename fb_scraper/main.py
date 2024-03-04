
from scraper import scrape_page

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
app = FastAPI()

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

@app.exception_handler(Exception)
async def exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"},
    )

@app.post("/scrape")
async def scrape(page_name: str, db_name: str, db_user: str, db_password: str, db_host: str):
    try:
        scrape_page(page_name, db_name, db_user, db_password, db_host)
        return {"message": "Scraping complete."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

