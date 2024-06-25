import pytest
from selenium import webdriver

driver=webdriver.Chrome()

class TestTitle:
  def test_page_title(self):
    driver.get("https://stackoverflow.com/")
    expected_title="Stack Overflow - Where Developers Learn, Share, & Build Careers"
    actual_title=driver.title
    assert expected_title==actual_title