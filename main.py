import sys
import time
import requests
from colorama import *
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# Open a New Chrome Window
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome()

welcome = "Your Personal Wikipedia Navigator: Wiki Compass Activated>>>"
for char in welcome:
    sys.stdout.write(f"{Fore.GREEN}{char}{Style.RESET_ALL}")
    sys.stdout.flush()
    time.sleep(0.1)
print()

username = input("Enter the Username")
exit = "The username you enter is very important because if you want to exit then just enter the username."
print(f"{Fore.RED}NOTE:{Style.RESET_ALL}")
for char in exit:
    sys.stdout.write(f"{Fore.RED}{char}{Style.RESET_ALL}")
    sys.stdout.flush()
    time.sleep(0.1)
print()

try:
    # Navigate to Wikipedia page
    driver.get("https://www.wikipedia.org/")

    loop_value=0
    while loop_value<=5000000:
        if loop_value==0:
            time.sleep(2)
            # Find the search bar element
            search_bar = driver.find_element(By.ID, "searchInput")

            # Enter any data You want to search on Wikipedia and Submit the search form
            print("Want to Search Something>>")
            search_input = input()
            if search_input == username:
                print("?")
                break
            else:
                pass
            search_bar.send_keys(search_input)
            search_bar.submit()

            loading = '-(Loading)-'
            for e in range(5):
                for char in loading:
                    if char in 'Loading':
                        sys.stdout.write(f"{Fore.BLUE}{char}{Style.RESET_ALL}{Fore.RED}_{Style.RESET_ALL}")
                        sys.stdout.flush()
                        time.sleep(0.1)

                    else:
                        sys.stdout.write(f"{Fore.GREEN}{char}{Style.RESET_ALL}{Fore.RED}_{Style.RESET_ALL}")
                        sys.stdout.flush()
                        time.sleep(0.1)

            # Current Url for Scraping DATA from this page
            current_url = driver.current_url


            # Using Soup for scraping data frome current url
            curl = requests.get(current_url)
            soup = BeautifulSoup(curl.text, "lxml")
            div = soup.find('div', class_ = "mw-content-ltr mw-parser-output")
            h2 = div.find_all('h2')
            h3 = div.find_all('h3')
            h4 = div.find_all('h4')
            p = div.find_all('p')

            all_tags = []
            for i in h2:
                all_tags.append(i.text)
            for i in h3:
                all_tags.append(i.text)
            for i in h4:
                all_tags.append(i.text)
            for i in p:
                all_tags.append(i.text)

            for i in div:
                if i.text in all_tags:
                    print(i.text)

            for hl in range(127):
                print(f"{Fore.RED}_{Style.RESET_ALL}", end="")

        elif loop_value>0:
            driver.back()
            driver.refresh()
            # Find the search bar element
            search_bar = driver.find_element(By.ID, "searchInput")

            # Enter any data You want to search on Wikipedia and Submit the search form
            print("Want to Search More>>")
            search_again = input()
            if search_again == username:
                print("?")
                break
            else:
                pass
            search_bar.send_keys(search_again)
            search_bar.submit()

            loading = '-(Loading)-'
            for e in range(5):
                for char in loading:
                    if char in 'Loading':
                        sys.stdout.write(f"{Fore.BLUE}{char}{Style.RESET_ALL}{Fore.RED}_{Style.RESET_ALL}")
                        sys.stdout.flush()
                        time.sleep(0.1)

                    else:
                        sys.stdout.write(f"{Fore.GREEN}{char}{Style.RESET_ALL}{Fore.RED}_{Style.RESET_ALL}")
                        sys.stdout.flush()
                        time.sleep(0.1)

            # Current Url for Scraping DATA from this page
            current_url = driver.current_url


            # Using Soup for scraping data frome current url
            curl = requests.get(current_url)
            soup = BeautifulSoup(curl.text, "lxml")
            div = soup.find('div', class_ = "mw-content-ltr mw-parser-output")
            h2 = div.find_all('h2')
            h3 = div.find_all('h3')
            h4 = div.find_all('h4')
            p = div.find_all('p')

            all_tags = []
            for i in h2:
                all_tags.append(i.text)
            for i in h3:
                all_tags.append(i.text)
            for i in h4:
                all_tags.append(i.text)
            for i in p:
                all_tags.append(i.text)

            for i in div:
                if i.text in all_tags:
                    print(i.text)

            for hl in range(127):
                print(f"{Fore.RED}_{Style.RESET_ALL}", end="")

        loop_value=loop_value+1
    
except:  
    # Closing New opend window
    driver.quit()