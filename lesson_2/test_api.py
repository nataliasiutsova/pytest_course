import requests
import pytest
import json
import random
from faker import Faker
fake=Faker()


class TestCreateUser:
 
 def test_create_user(self):
  
  payload_data={
  "id": random.randint(1,10),
  "username": fake.user_name(),
  "firstName": fake.first_name(),
  "lastName": fake.last_name(),
  "email": fake.email(),
  "password": fake.password(),
  "phone": fake.phone_number(),
  "userStatus": 0
}
  global user_name
  user_name=payload_data["username"]
  global last_name
  last_name=payload_data["lastName"]


  
  r=requests.post("https://petstore.swagger.io/v2/user", json=payload_data)

  content=json.loads(r.content.decode("utf-8"))
  assert r.status_code==200
  assert len(content)>0

 def test_get_user_by_user_name(self):
  r=requests.get(f"https://petstore.swagger.io/v2/user/{user_name}")
  content=json.loads(r.content.decode("utf-8"))
  assert r.status_code==200
  assert content["lastName"]==last_name 

 def test_get_not_existing_user(self):
   r=requests.get(f"https://petstore.swagger.io/v2/user/{fake.user_name()}")
   assert r.status_code==404
   
   
 