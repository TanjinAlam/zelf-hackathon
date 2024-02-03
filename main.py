
from helper import get_user_story_screenshot
import undetected_chromedriver as UC
from fastapi import FastAPI
from fastapi import Response
from helper.get_each_user_story import get_each_user_stories
from helper.get_user_stories import get_user_stories
app = FastAPI()
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

import os

userName = os.getenv("USERNAME")
password = os.getenv("PASSWORD")



@app.get("/user_all_story")
async def read_root():
    driver = UC.Chrome()
    data = get_user_stories(driver,'https://www.instagram.com/',userName,password)
    return Response(content=data, media_type='application/json')


@app.get("/get_each_user_story")
async def read_root():
    driver = UC.Chrome()
    data = get_each_user_stories(driver,'https://www.instagram.com/',userName,password)
    return Response(content=data, media_type='application/json')


@app.get("/get_user_story_screenshots")
async def read_root():
    driver = UC.Chrome()
    data = get_user_story_screenshot(driver,'https://www.instagram.com/',userName,password)
    return Response(content=data, media_type='application/json')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)