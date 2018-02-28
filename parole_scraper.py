from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import requests

dates = "06/08/2016"
URL = "http://ewsocis1.courts.state.va.us/CJISWeb/circuit.jsp"
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
# website = requests.get(URL, headers=headers)

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


# Scraping individual cases
source = browser.page_source
soup = BeautifulSoup(source, 'html.parser')

case_table = soup.findAll('table')[3]

loops_needed = len(case_table.find_all('tr'))
# csv_file = open("court.csv", "w")

for i in range(loops_needed-1):
    browser.find_element_by_xpath('(//*[@id="tdbold"])[' + str(i+1) + ']/a').click()

    # SCRAPING
    case_source = browser.page_source
    case_soup = BeautifulSoup(case_source, 'html.parser')

    # Checking if Guilty and has Probation Time
    final_disposition_table = case_soup.findAll('table')[8]
    disposition_code = final_disposition_table.findAll('td')[0].text
    results_table = case_soup.findAll('table')[9]
    probation_time = results_table.findAll('td')[11].text

    if disposition_code.split()[2] == "Guilty" and len(probation_time.split()) > 2:

        # Demographics
        main_table = case_soup.findAll('table')[4]

        case_number = main_table.findAll('td')[0].text
        case_number = case_number.split()[2]

        name = main_table.findAll('td')[4].text
        name = name.split()[1:]
        name = " ".join(name)

        sex = main_table.findAll('td')[5].text
        sex = sex.split()[1]

        race = main_table.findAll('td')[6].text
        race = race.split()[1:]
        race = " ".join(race)

        charge = main_table.findAll('td')[9].text
        charge = charge.split()[1:]
        charge = " ".join(charge)

        code_section = main_table.findAll('td')[10].text
        code_section = code_section.split()[2]

        charge_type = main_table.findAll('td')[11].text
        charge_type = charge_type.split()[2]

        # Final Disposition
        final_disposition_table = case_soup.findAll('table')[8]

        disposition_code = final_disposition_table.findAll('td')[0].text
        disposition_code = disposition_code.split()[2]

        disposition_date = final_disposition_table.findAll('td')[1].text
        disposition_date = disposition_date.split()[2]

        # Results
        results_table = case_soup.findAll('table')[9]

        sentence_time = results_table.findAll('td')[3].text
        sentence_time = sentence_time.split()[2:]
        sentence_time = " ".join(sentence_time)

        probation_time = results_table.findAll('td')[11].text
        probation_time = probation_time.split()[2:]
        probation_time = " ".join(probation_time)


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

        # csv_row = [case_number, name, sex, race, charge, code_section, charge_type, disposition_code, disposition_date, sentence_time, probation_time]
        # data = ",".join(csv_row)
        # csv_file.write(data + "\n")

    browser.find_element_by_id("hearList").click()

# csv_file.close()