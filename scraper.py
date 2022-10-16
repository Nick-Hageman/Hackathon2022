import sqlite3
from selenium import webdriver
from selenium.webdriver.common.by import By #Need this to select elements
from selenium.webdriver.chrome.service import Service
import time
import datetime 

url = 'https://dining.uiowa.edu/burge-market-place'

#Connect to SQLite Database
conn = sqlite3.connect("./database/burge.db") # Establish connection to Database
conn = sqlite3.connect("./database/catlett.db")
conn = sqlite3.connect("./database/hillcrest.db")
c = conn.cursor()

#---Drop Database Table---
#c.execute('''DROP TABLE burge''')

#---Create Table---
#c.execute('''CREATE TABLE videos(title TEXT, views TEXT, likes TEXT)''')
#c.execute('''CREATE TABLE burge(breakfast TEXT, lunch TEXT, dinner TEXT)''')
#Store data in arrays
breakfast = []
lunch = []
dinner = []

#Start chromedriver
ser = Service(r"C:\Users\gabri\Downloads\chromedriver_win32\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get(url)

#Find all menu elements
menu = driver.find_elements(By.CLASS_NAME, "menu-course")

date = driver.find_elements(By.CLASS_NAME, "dining-hours-date")[0].text
#date = driver.find_element(By.CLASS_NAME, "datepicker form-control form-text menuDatePicker-processed picker__input")
#print(date)

def getFoodList(element, menu, started, diningHall):
    for item in menu:   #parse through dining hall food sections
        food = item.find_elements(By.CLASS_NAME, 'menu-item-title') #parse through to get food item name
        for x in food:  #goes through list of food
            if (started == True and len(x.text) == 0):  #checks for empty lists and checks if tab is activated
                break
            if (len(x.text) != 0):  #once thorugh empty foods, enables the production of forming food list
                started = True
            if (started == True):   #starts building food list and add it to data
                if element == driver.find_element(By.XPATH, './/*[@id="location-menu"]/div/ul/li[1]/a'):    #checks if on breakfast tab
                    c.execute('''INSERT INTO {} (breakfast) VALUES (?)'''.format(diningHall), (x.text,))    #adds foods into breakfast table
                elif element == driver.find_element(By.XPATH, './/*[@id="location-menu"]/div/ul/li[2]/a'):  #checks if on lunch tab
                    c.execute('''INSERT INTO {} (lunch) VALUES (?)'''.format(diningHall), (x.text,))        #adds foods into lunch table
                elif element == driver.find_element(By.XPATH, './/*[@id="location-menu"]/div/ul/li[3]/a'):  #checks if on dinner tab
                    c.execute('''INSERT INTO {} (dinner) VALUES (?)'''.format(diningHall), (x.text,))       #adds foods into dinner table
                print(x.text)
    
def getAllFood(url):      #url is defined at the top, gets all food on the current day
    diningHall = url[25: url.index('-')]   #gets dining hall from url
    #gets breakfast list
    getFoodList(driver.find_element(By.XPATH, './/*[@id="location-menu"]/div/ul/li[1]/a').click(),driver.find_elements(By.CLASS_NAME, "menu-course"), True, diningHall)
    time.sleep(3)
    #gets lunch list
    getFoodList(driver.find_element(By.XPATH, './/*[@id="location-menu"]/div/ul/li[2]/a').click(),driver.find_elements(By.CLASS_NAME, "menu-course"), False, diningHall)
    time.sleep(3)
    #gets dinner list
    getFoodList(driver.find_element(By.XPATH, './/*[@id="location-menu"]/div/ul/li[3]/a').click(),driver.find_elements(By.CLASS_NAME, "menu-course"), False, diningHall)

def goThroughWeeks():
    access = True
    getAllFood(url)     #gets all food from page
    for x in (range(1,(int(datetime.datetime.now().strftime("%U"))+1)%7)):      #Iterates 1 week at a time---->weeks in callender
        for y in (range(1,(int(datetime.datetime.now().strftime("%w"))+1)%8)):     #iterates for 1 day at a time---->days in week
            if(access):     #if active get change date and get all food
                driver.find_element(By.XPATH, './html/body/div[3]/div/div[2]/div/div/article/div/div[1]/div/div[1]/div[2]/div/div[1]/div/input').click()      #clicks onto the calender prompt
                driver.find_element(By.XPATH, './html/body/div[3]/div/div[2]/div/div/article/div/div[1]/div/div[1]/div[2]/div/div/div[1]/div/div/div/div/div/div/table/tbody/tr['+str(x)+']/td['+str(y)+']/div').click()
                getAllFood(url)

def getAllDining():    #gets all food on the current day at all the dining halls
    getAllFood('https://dining.uiowa.edu/burge-market-place')
    driver.get('https://dining.uiowa.edu/hillcrest-market-place')
    getAllFood('https://dining.uiowa.edu/hillcrest-market-place')   
    driver.get('https://dining.uiowa.edu/catlett-market-place')
    getAllFood('https://dining.uiowa.edu/catlett-market-place')

getAllDining()


#insert Date into database
#c.execute('''INSERT INTO videos VALUES(?, ?, ?)''', (food, date))
conn.commit()

#---INSERTING DATA---
#c.execute('''INSERT INTO videos VALUES(?,?,?)''', (title, views, likes))
#---Commit INSERTIONS---
#conn.commit()

#c.execute('''SELECT * FROM burge''') # could select "title" to just get title
#c.execute('''SELECT * FROM catlett''')
#c.execute('''SELECT * FROM hillcrest''')
results = c.fetchall()
#print(results)

print("-----------------------------------")