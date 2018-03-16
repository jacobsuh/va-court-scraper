from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

def set_court_by_index(i):
    dropdown = Select(browser.find_element_by_name("whichsystem"))
    dropdown.select_by_index(i)
    browser.find_element_by_id("courtSubmit").click()

def set_name(name):
    namebox = browser.find_element_by_name("lastName")
    namebox.send_keys(name)
    browser.find_element_by_id("nameSubmit").click()

def get_last_first(line):
    case_line = line.split(",")
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

county = "Fluvanna"

source = browser.page_source
soup = BeautifulSoup(source, 'html.parser')

courts_list = browser.find_elements_by_css_selector("option")

for court in range(len(courts_list)+1):
    court_name = soup.findAll("option")[court].text.lstrip()

    set_court_by_index(1)

    csv_file = open(county + ".csv", "r")
    for line in csv_file:
        print("Supplied name: " + get_last_first(line))
        doc_name_shortened = get_last_first(line)


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
            case_name_shortened = case_name_split[0] + ", " + case_name_split[1].split()[0]

            if case_name_shortened == doc_name_shortened and len(case_id_cell_link.text) > 0:
                print("Match found")
                case_id_cell_link.click()

                # Need to check DOB is same
                # Check if disposition date is after original
                # Check if guilty and not probation violation

                # Append the county name
                quit()
            else:
                continue

        browser.find_element_by_xpath("//input[@value='Main Menu']").click()

    browser.find_element_by_xpath("//input[@value='Change Court']").click()