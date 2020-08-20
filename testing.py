# you need to fix the SSL issue,
# found that the page is run by react, react scambles the code everytime, however,
# there is something interesting, always in the source of the page, there is a json object that has all the items
# it is a script tag at the end of the page that has attribute called data-js-react-on-rails-store
# it makes it too much easier to scroll through. see below.

import json
from colorama import Fore, Back, Style
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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

firstpage = 9
lastpage = json_response["items"]["catalogItems"]["totalPages"]
itemCounter = 1

# start the things
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
                if sub_item_counter < 5:
                    print(itemCounter, ": Price is: ",value["price"], ", Username is:", value["user"]["login"],", Color is: ", value["color1_id"],", Favorites are: ",value["favourite_count"])
                itemCounter = itemCounter + 1
                sub_item_counter = sub_item_counter + 1
            break
        except:
            print("Oops!  we have a problem")
            if  error_counter >= 5:
                exit()
            error_counter = error_counter + 1

exit()
