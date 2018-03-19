'''
This scrapes the database by the names found in court_scraper.py.
Checks to see if people randomly chosen had been convicted after their first offense.
If they were, the county they were convicted in is added to the main list.
'''

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

def set_court_by_index(i):
    dropdown = Select(browser.find_element_by_name("whichsystem"))
    dropdown.select_by_index(i)
    browser.find_element_by_id("courtSubmit").click()

def set_name(name):
    namebox = browser.find_element_by_name("lastName")
    namebox.send_keys(name)
    browser.find_element_by_id("nameSubmit").click()

def get_last_first(case_line):
    last_name = case_line[1]
    first_name = case_line[2].split()[0]
    name_shortened = last_name + ", " + first_name

    return name_shortened

URL = "http://ewsocis1.courts.state.va.us/CJISWeb/circuit.jsp"
browser = webdriver.Chrome()
browser.get(URL)

# csv_file = open("repeat_names.csv", "w")
# headers = "jklafwjklafwjklawf, kjlafwjklafwjkl"
# csv_file.write(headers + "\n")

county = "Albemarle"

source = browser.page_source
soup = BeautifulSoup(source, 'html.parser')

courts_list = browser.find_elements_by_css_selector("option")

match_dict = {}

for court in range(len(courts_list)+1):
    court_name = soup.findAll("option")[court].text.strip()

    set_court_by_index(court)

    csv_file = open(county + ".csv", "r+")
    for line in csv_file:
        case_line = line.split(",")
        print("Supplied name: " + get_last_first(case_line))
        doc_name_shortened = get_last_first(case_line)

        # Search for the name in the system
        set_name(doc_name_shortened)

        case_list_soup = BeautifulSoup(browser.page_source, "html.parser")
        case_table = case_list_soup.findAll('table')[3]
        loops_needed = len(case_table.find_all('tr'))

        for i in range(loops_needed-1):
            # Gets names from case list
            case_id_cell = case_list_soup.find_all(id="tdbold")[i]
            case_defendant = case_id_cell.parent.findNext("td").text.lstrip()
            # Just declaring the clickable case number link
            case_id_cell_link = browser.find_element_by_xpath('(//*[@id="tdbold"])[' + str(i + 1) + ']/a')

            # Gets rid of middle names
            case_name_split = case_defendant.split(", ")
            if len(case_name_split) > 1:
                case_name_shortened = case_name_split[0] + ", " + case_name_split[1].split()[0]
            else:
                case_name_shortened = case_name_split[0]

            # Check if disposition date is after original
            # Hear date is new list
            hear_date = case_id_cell.parent.findNext("td").findNext("td").findNext("td").text
            if len(hear_date) > 0:
                hear_date_test = time.strptime(hear_date, "%m/%d/%Y")
            else:
                continue
            # Case date is from old list
            case_date = case_line[5]
            case_date_test = time.strptime(case_date, "%m/%d/%y")

            # If there's a match, proceed to make sure all other qualifiers match
            if case_name_shortened == doc_name_shortened and len(case_id_cell_link.text) > 0 and hear_date_test > case_date_test:
                print(case_id_cell_link.text)
                print("Name match found")
                case_id_cell_link.click()

                # Check if guilty and not probation violation
                case_source = browser.page_source
                case_soup = BeautifulSoup(case_source, 'html.parser')

                # Demographics Table
                main_table = case_soup.findAll('table')[4]
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

                if len(disposition_code.split()) > 2 and disposition_code.split()[2] == "Guilty":
                    match_value = court_name + "; " + hear_date
                    print(match_value)

                    # Add the county name and hearing date to dictionary
                    if doc_name_shortened not in match_dict:
                        match_dict[doc_name_shortened] = [match_value]
                    elif match_value not in match_dict[doc_name_shortened]:
                        match_dict[doc_name_shortened].append(match_value)

                    print(match_dict)
                else:
                    print("Not 'GUILTY'.")

                browser.find_element_by_xpath("//input[@value='  Name List ']").click()

        browser.find_element_by_xpath("//input[@value='Main Menu']").click()

    browser.find_element_by_xpath("//input[@value='Change Court']").click()

csv_file.close()

print("SAVING OUTPUT...")
output_file = open(county + "_output.csv", "w")
for item in match_dict:
    line = []
    line.append(item)
    for record in match_dict[item]:
        line.append(record)
    print(line)
    data = ",".join(line)
    output_file.write(data + "\n")
output_file.close()