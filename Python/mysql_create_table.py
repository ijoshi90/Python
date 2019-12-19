"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 19-12-2019 at 18:31
"""

import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.179.137",
  user="akshay",
  passwd="password",
  database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")