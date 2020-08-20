import json, csv
from colorama import Fore, Back, Style
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

file = open('vinted.csv', 'w')
options = Options()
options.add_argument("--ignore-certificate-errors")
browser = webdriver.Chrome(options=options)

#initial request, then we make the code scroll through all the pages, it gets the total number of pages from the website, not manual.
browser.get('https://www.vinted.es/vetements?catalog[]=1&page=1/')
elem = browser.find_element_by_xpath('//*[@data-js-react-on-rails-store]').get_attribute('textContent')  # Find the search box
json_response = json.loads(elem)
timeout=5

element_present0 = EC.presence_of_element_located((By.XPATH,'//*[@data-js-react-on-rails-store]'))
WebDriverWait(browser, timeout).until(element_present0)

firstpage = 1
lastpage = json_response["items"]["catalogItems"]["totalPages"]
itemCounter = 1

# start the things
with file:
        writer = csv.writer(file)
        writer.writerow(['Usuario','City','User items','Item title',
        'Item description', 'Item views','Size','Brand','Status','Price','Color','Likes'])
        for page_counter in range(firstpage, lastpage):
            #make the requets everytime
            print(Fore.RED + 'Page #: ' + Style.RESET_ALL + str(page_counter))
            url = 'https://www.vinted.es/vetements?catalog[]=1&page=' + str(page_counter)
            error_counter = 0
            # OK, so the code below will try to find the element, if exception, it will reload the page, and it will find it and continue.
            # good luck

            while True:
                try:
                    browser.get(url)
                    elem = browser.find_element_by_xpath('//*[@data-js-react-on-rails-store]').get_attribute('textContent')  # Find the search box
                    json_response = json.loads(elem)
                    # loop through the items
                    sub_item_counter = 0
                    
                    for key, value in json_response["items"]["byId"].items():
                        if sub_item_counter < 24:
                            writer.writerow(
                            [value["user"]["login"],
                            value["user"]["city"],
                            value["user"]["item_count"],
                            value["title"],
                            value["description"],
                            value["view_count"],
                            value["size"],
                            value["brand"],
                            value["status"],
                            value["price"], 
                            value["color1_id"],
                            value["favourite_count"]
                            ])
                            print(
                            itemCounter,
                            ", Username is: ", value["user"]["login"], 
                            ", User items: ", value["user"]["item_count"],
                            ", City: ", value["user"]["city"],
                            "|| Item title: ", value["title"],
                            ", Item description: ", value["description"],
                            ", Item views: ", value["view_count"],
                            ", Size: ", value["size"],
                            ", Brand: ", value["brand"],
                            ", Status: ", value["status"],
                            ", Price is: ", value["price"], 
                            ", Color is: ", value["color1_id"],
                            ", Favorites are: ", value["favourite_count"]
                            )
                        itemCounter = itemCounter + 1
                        sub_item_counter = sub_item_counter + 1
                    break
                except:
                    print("Oops!  we have a problem")
                    if  error_counter >= 5:
                        exit()
                    error_counter = error_counter + 1

        exit()