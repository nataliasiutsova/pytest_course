import pytest
from selenium import webdriver

driver=webdriver.Chrome()

class TestTitle:
  def test_page_title(self):
    driver.get("https://www.visitnorway.com/")
    expected_title="Visit Norway | Official travel guide to Norway"
    actual_title=driver.title
    assert expected_title==actual_title

     