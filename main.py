import time
import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
xpath_input = '/html/body/div[3]/div[4]/div[3]/div/div[3]/div[2]/div[8]/div/div[2]/div[1]/div/form/input[1]'
xpath_change = '//*[@id="visa_plan_ahead_rwd"]/div[2]/div[2]/div/span'
list_of_city = ["Abidjan", "Abu Dhabi", "Abuja", "Accra", "Adana", "Addis Ababa", "Algiers","Almaty","Amman",
                "Amsterdam","Ankara","Antananarivo","Apia","Ashgabat","Asmara","Asuncion","Athens","Auckland",'Baghdad',
                'Baku','Bamako','Bandar Seri Begawan','Bangkok','Banjul','Barcelona','Beijing',
                'Beirut','Belfast','Belgrade','Belmopan','Berlin','Bern','Bishkek','Bogota','Brasilia',
                'Bratislava','Brazzaville','Bridgetown','Brussels','Bucharest','Budapest','Buenos Aires','Bujumbura',
                ]


browser = webdriver.Chrome()
browser.get('https://travel.state.gov/content/travel/en/us-visas.html')

path = 'visa_usa.csv'
input = browser.find_element_by_xpath(xpath_input)
visa = []
i = 0
for el in list_of_city:
    input.send_keys(el)
    input.send_keys(Keys.ENTER)
    time.sleep(2)
    value = browser.find_element_by_class_name('num_days_visitor').text
    visa.append({
        'el': value,
    })
    change = browser.find_element_by_xpath(xpath_change)
    change.click()


# print(visa)

with open(path, 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['City', 'Wait time'])
    for item in visa:
        writer.writerow([list_of_city[i], item['el']])
        i += 1




