import openpyxl
# Used to import the webdriver from selenium
from selenium import webdriver
import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime

# Get the path of chromedriver which you have install

# LANDVISION
def startBot(username, password, url, location):
    s = Service('/Users/christophertrippel/PycharmProjects/pythonProject/chromedriver')
    driver = webdriver.Chrome(service=s)
    list = []

    # opening the website  in chrome.
    driver.get(url)

    # find the id or name or class of
    # username by inspecting on username input
    driver.find_element(By.ID,
        "ctl00_ctl00_MainContentPlaceHolder_MainContent_LoginUser_UserName").send_keys(username)

    # find the password by inspecting on password input
    driver.find_element(By.ID,
        "ctl00_ctl00_MainContentPlaceHolder_MainContent_LoginUser_Password").send_keys(password)

    # click on submit
    driver.find_element(By.ID,
        "ctl00_ctl00_MainContentPlaceHolder_MainContent_LoginUser_LoginButton").click()

    time.sleep(2)

    driver.find_element(By.PARTIAL_LINK_TEXT,
                        "LandVision™").click()
    time.sleep(5)

    driver.find_element(By.ID,
                        "searchInputBox").send_keys(location)

    time.sleep(3)

    driver.find_element(By.ID,
                        "searchButton").click()

    time.sleep(10)

    # TODO IF NO RESULT HERE FILL OUT EXCEL AS N/A HAVE TRUE OR FALSE FLAG FOR FOUND VS NOT FOUND
    parcel_element = driver.find_element(By.ID,"APN14764712871601230024743169")
    parcelNum = parcel_element.text
    parcelNum = parcelNum.split()

    parcelNum = parcelNum[3]

    list.append(parcelNum)

    last_sale_AND_price_element = driver.find_element(By.ID, "DATE_TRANSFER14764741062561454744183232")
    # split string for ^ (m/dd/yyyy) $<amount>

    tempString = last_sale_AND_price_element.text
    tempString = tempString.split()

    list.append(tempString[3])
    list.append(tempString[5])

    lot_size_element = driver.find_element(By.ID, "CUSTOM_SCRIPT14764713063173742496117214764713063181309428583173")
    lotSize = lot_size_element.text
    lotSize = lotSize.split()
    lotSize = lotSize[2]

    list.append(lotSize)

    zoning_element = driver.find_element(By.ID, "ZONING147647540102912649719131076")
    zoning = zoning_element.text
    zoning = zoning.split()
    zoning = zoning[2]

    list.append(zoning)

    owner_element = driver.find_element(By.ID, "OWNER_NAME_11476471882809240282258281")
    owner = owner_element.text
    # IF THIS IS AN LLC
    owner = owner[8:]

    # TODO is this is a person

    list.append(owner)

    return list

# LARA
def startLara(url, owner):
    s = Service('/Users/christophertrippel/PycharmProjects/pythonProject/chromedriver')
    driver = webdriver.Chrome(service=s)

    # opening the website  in chrome.
    driver.get(url)

    time.sleep(3)

    driver.find_element(By.ID,
                        "txtEntityName").send_keys(owner)

    time.sleep(3)

    driver.find_element(By.ID,
                        "SearchSubmit").click()

    time.sleep(3)

    # TODO IF THERE ARE MULPITPLE OPTIONS FOR LLC CHECK THE ADDRESS FROM LANDVISON
    driver.find_element(By.XPATH, '//a[@href="' + "https://cofs.lara.state.mi.us/CorpWeb/CorpSearch/CorpSummary.aspx?token=nBxILn58HwVtv4JMRDwTm1cWblopjmzIgq3FCQzRMH7Z0mRAdeXC1B5BhZoRn0rX3c+Fp+Gbnx2wRL9zMGX1/sqhAMEqWytza0G4dL88Kii9r8OTSljKNqvdnbvImpekDgIM4oOuLyKYNJ5StGnZPZoKheK8QThGI0ug80NLPCzCtiv7EGbX4jSx3ouV2Zjy5Qm+v6OzxOMA/HplVdLzxkw3cZwjP27lAx5LCRGE2ZFSc0ygP37CQCJ5pQFzVU7uCL9rpuRfy5+xp3WO0wsgZTfDSJRqmg+Ff1cDuBTDo/tWBmbGZ5EtFbd7cBsUl4qwkAVNmUcdtgRQ7xoNebsN5AeSWszabZBf" + '"]').click()
    time.sleep(3)

    resident_element = driver.find_element(By.ID, "MainContent_lblResidentAgentName")
    resident = resident_element.text
    return resident

    # TODO GET FIRST NAME FROM THIS RESIDENT
    
    # TODO GET LAST NAME FROM THIS RESIDENT


    

# LEXIS NEXIS
def startLexisNexis(username, password, url, first, last):
    s = Service('/Users/christophertrippel/PycharmProjects/pythonProject/chromedriver')
    driver = webdriver.Chrome(service=s)

    # time.sleep(5)
    # opening the website  in chrome.
    driver.get(url)

    # find the id or name or class of
    # username by inspecting on username input
    driver.find_element(By.ID,
                        "userNameInput").send_keys(username)

    # find the password by inspecting on password input
    driver.find_element(By.ID,
                        "passwordInput").send_keys(password)

    # click on submit
    driver.find_element(By.ID,
                        "submitButton").click()



    time.sleep(4)

    driver.find_element(By.PARTIAL_LINK_TEXT,
                        "Comprehensive People").click()
    time.sleep(5)
    iframe = driver.find_elements(By.TAG_NAME, "iframe")[0]
    driver.switch_to.frame(iframe)
    driver.find_element(By.NAME,
                        "ctl00$MainContent$Name$FirstName").send_keys(first)
    driver.find_element(By.NAME,
                        "ctl00$MainContent$Name$LastName").send_keys(last)
    time.sleep(2)

    button = driver.find_element(By.NAME,
                        "ctl00$MainContent$formSubmit$searchButton")

    driver.execute_script("arguments[0].click();", button)

    # driver.find_element(By.NAME,
    #                     "ctl00$MainContent$formSubmit$searchButton").click()

    time.sleep(5)

    driver.find_element(By.ID,
                        "spanNames1_0").click()

    time.sleep(5)

    # newframe = driver.find_elements(By.TAG_NAME, "iframe")[0]
    # driver.switch_to.frame(newframe)
    #
    # time.sleep(2)

    address = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div[2]/div/div[2]/div[2]/table[1]/tbody/tr[2]/td[2]")
    phone = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div[2]/div/div[2]/div[2]/table[1]/tbody/tr[2]/td[4]")
    email = driver.find_element(By.XPATH,"/html/body/form/div[3]/div[2]/div/div/div[2]/div/div[2]/div[2]/table[2]/tbody/tr[3]/td[5]")
    print(address.text)
    print(phone.text)
    print(email.text)







# Driver Code
# Enter below your login credentials
username = "YMouflouzelis"
password = "YMMM2022!"

nexisUser = "Yianni.mouflouzelis@marcusmillichap.com"
nexisPass = "Susan1970!"


# location = "3349 North Clark Street"
location = "54 Springview Dr, MI"
# URL of the login page of site
# which you want to automate login.


url = "https://login-spatialstream.prod.lightboxre.com/MemberPages/Login.aspx?ReturnUrl=%2fmemberpages%2fdefault.aspx%3fma%3dmarcusmillichap&ma=marcusmillichap"
lara_url = "https://cofs.lara.state.mi.us/SearchApi/Search/Search"
nexis_url = "https://advance.lexis.com/container?federationidp=2PQ9S259274&config=00JAAwNzNkMWZlYy0yZGE3LTQ2ZTYtYWYzMC1hNzc3YTFhYzZiY2IKAFBvZENhdGFsb2cdj7jL73YBZAngd4dP1brS&crid=356171ea-f80b-44f5-bc02-25fff019b5a4"


# Call the function
# mylist = startBot(username, password, url, location)
# print(mylist)
# resident = startLara(lara_url, mylist[5])
#
# resList = resident.split()
# print(resList)
# firstName = resList[0]
# lastName = resList[1]

startLexisNexis(nexisUser, nexisPass, nexis_url, "DAVID", "KAMARA")

# TODO EXCEL ENTRY
# excelPath = "/Users/christophertrippel/PycharmProjects/pythonProject/test.xlsx"
# workbook = openpyxl.load_workbook(excelPath)
# sheet = workbook.active
#
# sheet['A2'] = "54 Springview Dr"
# sheet['C2'] = "MI"
# sheet['F2'] = list[0]
# sheet['H2'] = list[1]
# sheet['I2'] = list[2]
# sheet['J2'] = list[3]
# sheet['M2'] = list[4]
# sheet['N2'] = list[5]
# sheet['O2'] = resident
# sheet['P2'] = firstName
# sheet['Q2'] = lastName
#
# now = datetime.now() # current date and time
#
# date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
#
# workbook.save(filename="/Users/christophertrippel/PycharmProjects/pythonProject/output.xlsx")
