from statistics import mode
import requests
from bs4 import BeautifulSoup

class Car:
     def __init__(self,id, model, name, price, mile):
          self.id = id
          self.model = model
          self.name = name
          self.price = price
          self.mile = mile

car_model = input()
car_name = input()
url = 'https://www.truecar.com/used-cars-for-sale/listings/{input1}/{input2}/location-new-york-ny/'.format(input1= car_model, input2= car_name)

response = requests.get(url)
all_data=BeautifulSoup(response.text , 'html.parser')
cars_data =all_data.find_all('div',attrs={'class':"card-content vehicle-card-body order-3"})

car_list=[]
counter = 1
for i in cars_data:
     if(counter > 20):
          break
     prices=i.find('div',attrs={'data-qa' : "Heading"})
     miles=i.find('div',attrs={'data-test' : 'vehicleMileage'})
     car=Car(counter, car_model,car_name,float(prices.text.split('$')[1].replace(',', '.')),float(miles.text.split(' ')[0].replace(',', '.')))
     car_list.append(car)
     counter = counter + 1


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="my-secret-pw",
  database="Test"
)
print(mydb)
mycursor = mydb.cursor()

for obj in car_list:
     sql = "INSERT INTO Car(Id, Name, Miles, Model, Price) VALUES (%s, %s, %s, %s, %s)"
     val = (obj.id, obj.name, obj.mile, obj.model, obj.price)
     mycursor.execute(sql, val)
     mydb.commit()



