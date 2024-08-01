import pytest
from selenium import webdriver
from dotenv import load_dotenv
import os

load_dotenv()
@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()

    name=os.getenv("name")
    password=os.getenv("password")
    url=os.getenv("url")
    # driver.get(url)


    request.cls.driver=driver
    request.cls.name=name
    request.cls.password=password
    request.cls.url=url

    yield driver
    driver.quit()


