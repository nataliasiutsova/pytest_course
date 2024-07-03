import pytest
from selenium import webdriver
from dotenv import load_dotenv
import os
import time


load_dotenv()

class TestLogin:

  def setup_method(self):
   self.driver=webdriver.Chrome()
   self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
   time.sleep(4)

  
  def test_page_elements_exist(self):
    
    assert self.driver.find_element('xpath',"//input[@name='username']").is_displayed()
    assert self.driver.find_element('xpath',"//input[@name='password']").is_displayed()
    assert self.driver.find_element('xpath',"//button[@type='submit']").is_displayed()


  @pytest.mark.parametrize("login,password,expected_result",[

    (os.getenv("LOGIN"),os.getenv("PASSWORD"),True),
    (os.getenv("LOGIN"),os.getenv("PASSWORD")[:7],False),

  ])

  def test_login(self,login,password,expected_result):
    
    self.driver.find_element('xpath',"//input[@name='username']").send_keys(login)
    self.driver.find_element('xpath',"//input[@name='password']").send_keys(password)
    self.driver.find_element('xpath',"//button[@type='submit']").click()
    
    if expected_result:
     assert "/dashboard/index" in self.driver.current_url 
    else:
      assert "/dashboard/index" not in self.driver.current_url 


  @pytest.mark.parametrize("link, url",[
    ("//a[contains(@href,'admin')]", "admin/viewSystemUsers"),
    ("//a[contains(@href,'pim')]", "pim/viewEmployeeList"),
    ("//a[contains(@href,'time')]", "time/viewEmployeeTimesheet"),
  
  ])
  def test_link_navigation(self,link,url):
  
    self.driver.find_element('xpath',"//input[@name='username']").send_keys(os.getenv("LOGIN"))
    self.driver.find_element('xpath',"//input[@name='password']").send_keys(os.getenv("PASSWORD"))
    self.driver.find_element('xpath',"//button[@type='submit']").click()
    time.sleep(3)
    self.driver.find_element('xpath',link).click()
    
    assert url in self.driver.current_url
    

  def teardown_method(self):
   self.driver.quit()


    
