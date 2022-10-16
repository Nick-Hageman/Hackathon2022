import sqlite3
from selenium import webdriver
from selenium.webdriver.common.by import By #Need this to select elements
from selenium.webdriver.chrome.service import Service

url = 'https://dining.uiowa.edu/burge-market-place'

#Connect to SQLite Database
conn = sqlite3.connect("./database/burge.db") # Establish connection to Database
c = conn.cursor()

#---Drop Database Table---
c.execute('''DROP TABLE burge''')

#---Create Table---
#c.execute('''CREATE TABLE videos(title TEXT, views TEXT, likes TEXT)''')
c.execute('''CREATE TABLE burge(breakfast TEXT, lunch TEXT, dinner TEXT)''')
#Store data in arrays
breakfast = []
lunch = []
dinner = []

#Start chromedriver
ser = Service(r"C:\Users\nickh\AppData\Local\Programs\Python\Python310\Scripts\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get(url)

#Find all menu elements
menu = driver.find_elements(By.CLASS_NAME, "menu-course")

date = driver.find_elements(By.CLASS_NAME, "dining-hours-date")[0].text
#date = driver.find_element(By.CLASS_NAME, "datepicker form-control form-text menuDatePicker-processed picker__input")
#print(date)

for item in menu: #Parse through burge
    #date = item.find_element(By.XPATH,'//*[@id="P578505111"]').text #Remeber to include '.' in front
    #food = item.find_elements(By.XPATH, '//*[@id="Breakfast"]/div/div[2]/div[2]/div[1]/div[1]') #Remeber to include '.' in front
    food = item.find_elements(By.CLASS_NAME, 'menu-item-title') #Remeber to include '.' in front
    # Check if end of menu items
    if (len(item.text) == 0):
        break
    for i in food:
         #c.execute('''INSERT INTO burge VALUES(?, ?)''', (date, i.text))
         breakfast.append(i.text)
         print(i.text)
         if (len(i.text) == 0):
            break

element = driver.find_element(By.XPATH, './/*[@id="location-menu"]/div/ul/li[2]/a').click() # Switches to Lunch Menu
started = False
#New menu elements (lunch)
menu2 = driver.find_elements(By.CLASS_NAME, "menu-course")
for item2 in menu2:
    food2 = item2.find_elements(By.CLASS_NAME, 'menu-item-title') #Remeber to include '.' in front
    for x in food2:
        if (started == True and len(x.text) == 0):
            break
        if (len(x.text) != 0):
            started = True
        if (started == True):
            #c.execute('''INSERT INTO videos VALUES(?, ?)''', (date, i.text))
            lunch.append(x.text)
            print(x.text)

element = driver.find_element(By.XPATH, './/*[@id="location-menu"]/div/ul/li[3]/a').click() # Switches to Lunch Menu
menu3 = driver.find_elements(By.CLASS_NAME, "menu-course") #Switches to Dinner Menu
started = False

for item3 in menu3:
    food3 = item3.find_elements(By.CLASS_NAME, 'menu-item-title') #Remeber to include '.' in front
    for x in food3:
        if (started == True and len(x.text) == 0):
            break
        if (len(x.text) != 0):
            started = True
        if (started == True):
            #c.execute('''INSERT INTO videos VALUES(?, ?)''', (date, i.text))
            dinner.append(x.text)
            print(x.text)



    #title = video.find_element(By.XPATH,'.//*[@id="video-title"]').text #Remeber to include '.' in front
    #views = video.find_element(By.XPATH,'.//*[@id="metadata-line"]/span[1]').text #Remeber to include '.' in front
    #date = video.find_element(By.XPATH,'.//*[@id="metadata-line"]/span[2]').text #Remeber to include '.' in front
    #c.execute('''INSERT INTO videos VALUES(?, ?)''', (food, date))

#insert Date into database
#c.execute('''INSERT INTO videos VALUES(?, ?, ?)''', (food, date))

#---INSERTING DATA---
#c.execute('''INSERT INTO videos VALUES(?,?,?)''', (title, views, likes))
#---Commit INSERTIONS---
#conn.commit()

c.execute('''SELECT * FROM burge''') # could select "title" to just get title
results = c.fetchall()
#print(results)


print("-----------------------------------------------------------------")
def getFoodList(element, menu, started):
    for item in menu:
        food = item.find_elements(By.CLASS_NAME, 'menu-item-title') #Remeber to include '.' in front
        for x in food:
            if (started == True and len(x.text) == 0):
                    break
            if (len(x.text) != 0):
                    started = True
            if (started == True):
                #c.execute('''INSERT INTO videos VALUES(?, ?)''', (date, i.text))
                print(x.text)
    
def getAllFood(url, diningHall):
    conn = sqlite3.connect("./database/" + diningHall + ".db")
    driver.get(url)
    c = conn.cursor()
    c.execute('''DROP TABLE {}'''.format(diningHall))
    getFoodList(driver.find_element(By.XPATH, './/*[@id="location-menu"]/div/ul/li[1]/a').click(),driver.find_elements(By.CLASS_NAME, "menu-course"), True)
    getFoodList(driver.find_element(By.XPATH, './/*[@id="location-menu"]/div/ul/li[2]/a').click(),driver.find_elements(By.CLASS_NAME, "menu-course"), False)
    getFoodList(driver.find_element(By.XPATH, './/*[@id="location-menu"]/div/ul/li[3]/a').click(),driver.find_elements(By.CLASS_NAME, "menu-course"), False)


#Insert data into DB
#for i in breakfast:
#    c.execute('''INSERT INTO burge (breakfast) VALUES(?)''', (i,))
#for j in lunch:
#    c.execute('''INSERT INTO burge (lunch) VALUES(?)''', (j,))
#for k in dinner:
#    c.execute('''INSERT INTO burge (dinner) VALUES(?)''', (k,))

for i in range(min(len(breakfast), len(lunch), len(dinner))):
    c.execute('''INSERT INTO burge VALUES(?, ?, ?)''', (breakfast[i], lunch[i], dinner[i]))


conn.commit()
#getAllFood()