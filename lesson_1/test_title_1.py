import pytest
from selenium import webdriver

driver=webdriver.Chrome()

class TestTitle:
  def test_page_title(self):
    driver.get("https://www.volvo.com/en/")
    expected_title="Welcome to Volvo"
    actual_title=driver.title
    assert expected_title==actual_title, "Title is incorrect"
    

