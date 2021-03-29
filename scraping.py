from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pandas as pd
import mysql.connector as mysql
import csv
from app import main

# Connectivity to the database
connection = mysql.connect(host="localhost",
                     user="root",
                     passwd=" ",
                     db="inventory")
driver = webdriver.Chrome('/usr/local/bin/chromedriver')

# Scraping barcode scanner from the website, automating it using selenium
driver.get("https://www.barcodelookup.com/")
driver.implicitly_wait(4)
table= driver.find_element_by_xpath("//*[@id='body-container']/section[1]/div/div[1]/p")
text_area = driver.find_element_by_xpath("/html/body/div[1]/section[1]/div/div[2]/form/div/input")
text_area.send_keys(main())
product_id = main()
driver.find_element_by_xpath("//*[@id='body-container']/section[1]/div/div[2]/form/div/span/button").click()

driver.implicitly_wait(4)
driver.get("https://www.barcodelookup.com/{}".format(product_id))
product_details = driver.find_element_by_xpath("//*[@id='body-container']/section[2]/div/div/div[2]/h4")
product = product_details.text

mySql_insert_query = "INSERT INTO pantry (item_barcode,item_name) VALUES (%s, %s)"
values = (product_id, product)
# mySql_insert_query = "INSERT INTO pantry (item_barcode,item_name) VALUES ({}, {});".format(barcode_text, name)
cursor = connection.cursor()
print(mySql_insert_query)
## executing the query with values
cursor.execute(mySql_insert_query, values)
connection.commit()

print(cursor.rowcount, "record inserted")
