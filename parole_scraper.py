from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import requests

# Typing date and "Search by Hearing Date"
def set_date(dates):
    datebox = browser.find_element_by_name("selectDate")
    datebox.send_keys(
        Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE)
    datebox.send_keys(dates)
    browser.find_element_by_name("hearDate").click()

# Picking proper court
def set_court(name):
    dropdown = Select(browser.find_element_by_name("whichsystem"))
    dropdown.select_by_visible_text(name)
    browser.find_element_by_id("courtSubmit").click()

def scrape_info():
    name = main_table.findAll('td')[4].text
    name = name.split()[1:]
    name = " ".join(name)

    sex = main_table.findAll('td')[5].text
    sex = sex.split()[1]

    race = main_table.findAll('td')[6].text
    race = race.split()[1:]
    race = " ".join(race)

    # Checking if case has AKA
    aka_shift = 0
    if "AKA:" in main_table.findAll('td')[8].text:
        aka_shift = 1

    charge = main_table.findAll('td')[9 + aka_shift].text
    charge = charge.split()[1:]
    charge = " ".join(charge)

    code_section = main_table.findAll('td')[10 + aka_shift].text
    code_section = code_section.split()[2]

    charge_type = main_table.findAll('td')[11 + aka_shift].text
    charge_type = charge_type.split()[2]

    # Final Disposition
    final_disposition_table = case_soup.findAll('table')[8]

    disposition_code = final_disposition_table.findAll('td')[0].text
    disposition_code = disposition_code.split()[2]

    disposition_date = final_disposition_table.findAll('td')[1].text
    disposition_date = disposition_date.split()[2]

    # Makes sure amended charges exist before adding

    amended_charge = final_disposition_table.findAll('td')[3].text
    if len(amended_charge.split()) > 2:
        amended_charge = amended_charge.split()[2:]
        amended_charge = " ".join(amended_charge)

        amended_code_section = final_disposition_table.findAll('td')[4].text
        amended_code_section = amended_code_section.split()[3]

        amended_charge_type = final_disposition_table.findAll('td')[5].text
        amended_charge_type = amended_charge_type.split()[3]
    else:
        amended_charge = ""
        amended_code_section = ""
        amended_charge_type = ""

    # Results
    results_table = case_soup.findAll('table')[9]

    sentence_time = results_table.findAll('td')[3].text
    sentence_time = sentence_time.split()[2:]
    sentence_time = " ".join(sentence_time)

    sentence_suspended = results_table.findAll('td')[4].text
    sentence_suspended = sentence_suspended.split()[2:]
    sentence_suspended = " ".join(sentence_suspended)

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

    csv_row = [case_number, name, sex, race, date, charge, code_section, charge_type, amended_charge,
               amended_code_section, amended_charge_type, disposition_code, disposition_date, sentence_time,
               sentence_suspended, probation_time]
    data = ",".join(csv_row)
    csv_file.write(data + "\n")

dates_generated = ['09/18/2013', '12/16/2014', '12/13/2015', '01/03/2015', '06/24/2013', '02/15/2016', '03/15/2015', '02/22/2012', '11/04/2013', '10/20/2012', '04/18/2016', '12/30/2012', '09/20/2013', '09/22/2015', '12/31/2013', '04/29/2012', '03/23/2014', '01/04/2015', '08/06/2015', '01/07/2016', '01/19/2014', '09/27/2013', '08/14/2015', '06/16/2012', '02/10/2016', '09/19/2012', '09/09/2016', '04/26/2016', '05/03/2013', '11/23/2015', '01/04/2012', '01/11/2013', '09/08/2014', '03/18/2016', '11/07/2012', '02/01/2012', '06/06/2015', '07/24/2015', '08/29/2015', '06/22/2014', '11/02/2015', '02/04/2013', '10/19/2016', '09/30/2014', '10/27/2012', '01/24/2012', '07/19/2014', '09/25/2015', '08/16/2013', '11/23/2012']
# Date with 4 known cases: "06/08/2016"
# "02/28/2018", "05/26/2014", "05/27/2014"
# 05/02/2014', '04/21/2014', '07/01/2011', '12/31/2014', '10/26/2014', "02/28/2018", "05/26/2014", "05/27/2014


URL = "http://ewsocis1.courts.state.va.us/CJISWeb/circuit.jsp"
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
# website = requests.get(URL, headers=headers)

browser = webdriver.Chrome()
browser.get(URL)

csv_file = open("court.csv", "w")
headers = "Case Number, Last Name, First Name, Sex, Race, Date, Charge, Code Section, Charge Type, Amended Charge, Amended Code Section, Amended Charge Type, Disposition Code, Disposition Date, Sentence Time, Sentence Suspended, Probation Time"
csv_file.write(headers + "\n")

set_court("Goochland Circuit Court")

for date in dates_generated:

    set_date(date)

    # Loop through all pages until we find a duplicate entry (no more pages)
    num_duplicates = 0
    case_list = []
    while num_duplicates == 0:
        print(num_duplicates)
        print(case_list)

        source = browser.page_source
        soup = BeautifulSoup(source, 'html.parser')

        case_table = soup.findAll('table')[3]

        # Keep track of the cases per day seen so far to keep track of duplicates
        loops_needed = len(case_table.find_all('tr'))
        if loops_needed == 1:
            num_duplicates = 1
            break
        # Loop through everything in the table
        for i in range(loops_needed-1):

            # Check if Case ID element exists
            case_id_cell = browser.find_element_by_xpath('(//*[@id="tdbold"])[' + str(i+1) + ']/a')
            if len(case_id_cell.text) > 0:
                case_id_cell.click()
            else:
                continue

            case_source = browser.page_source
            case_soup = BeautifulSoup(case_source, 'html.parser')

            # Demographics Table
            main_table = case_soup.findAll('table')[4]

            # Checking to make sure case number isn't repeated
            case_number = main_table.findAll('td')[0].text
            case_number = case_number.split()[2]

            if case_number in case_list:
                num_duplicates = 1
                browser.find_element_by_id("hearList").click()
                break
            else:
                case_list.append(case_number)

            # Check if Guilty, has Probation Time, and not Probation Violation
            final_disposition_table = case_soup.findAll('table')[8]
            disposition_code = final_disposition_table.findAll('td')[0].text
            results_table = case_soup.findAll('table')[9]
            probation_time = results_table.findAll('td')[11].text

            aka_shift = 0
            if "AKA:" in main_table.findAll('td')[8].text:
                aka_shift = 1
            charge = main_table.findAll('td')[9 + aka_shift].text
            charge = charge.split()[1:]
            charge = " ".join(charge)

            if len(disposition_code.split()) > 2 and disposition_code.split()[2] == "Guilty" and len(
                    probation_time.split()) > 2 and charge != "PROBATION VIOLATION":

                scrape_info()


            browser.find_element_by_id("hearList").click()

        browser.find_element_by_xpath("//input[@value='Scroll Forward']").click()

    browser.find_element_by_xpath("//input[@value='Main Menu']").click()

print("Scraping done for dates" + str(dates_generated))
csv_file.close()