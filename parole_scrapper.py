from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import requests

dates = "06/08/2016"
URL = "http://ewsocis1.courts.state.va.us/CJISWeb/circuit.jsp"
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
# website = requests.get(URL, headers=headers)
#
# soup = BeautifulSoup(website.text, "html.parser")
#
# print(soup.prettify())
browser = webdriver.Chrome()
browser.get(URL)

# Picking Albemarle Country Court
dropdown = Select(browser.find_element_by_name("whichsystem"))
dropdown.select_by_index(1)
browser.find_element_by_id("courtSubmit").click()

# Picking date and "Search by Hearing Date"
datebox = browser.find_element_by_name("selectDate")
datebox.send_keys(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE)
datebox.send_keys(dates)
browser.find_element_by_name("hearDate").click()

# For loop
source = browser.page_source
soup = BeautifulSoup(source, 'html.parser')

case_table = soup.findAll('table')[3]

loops_needed = len(case_table.find_all('tr'))

for i in range(loops_needed-1):
    browser.find_element_by_xpath('(//*[@id="tdbold"])[' + str(i+1) + ']/a').click()

    # SCRAPING
    case_source = browser.page_source
    case_soup = BeautifulSoup(case_source, 'html.parser')

    # Demographics
    main_table = case_soup.findAll('table')[4]

    case_number = main_table.findAll('td')[0].text
    name = main_table.findAll('td')[4].text
    sex = main_table.findAll('td')[5].text
    race = main_table.findAll('td')[6].text
    charge = main_table.findAll('td')[9].text
    code_section = main_table.findAll('td')[10].text
    charge_type = main_table.findAll('td')[11].text

    # Final Disposition
    final_disposition_table = case_soup.findAll('table')[8]

    disposition_code = final_disposition_table.findAll('td')[0].text
    disposition_date = final_disposition_table.findAll('td')[1].text

    # Results
    results_table = case_soup.findAll('table')[9]
    sentence_time = results_table.findAll('td')[4].text
    probation_time = results_table.findAll('td')[11].text

    if disposition_code.split()[2] == "Guilty" and len(probation_time.split()) > 2:
        print(case_number)
        print(name)
        print(sex)
        print(race)
        print(charge)
        print(code_section)
        print(charge_type)

        print(disposition_code)
        print(disposition_date)

        print(sentence_time)
        print(probation_time)

    browser.find_element_by_id("hearList").click()