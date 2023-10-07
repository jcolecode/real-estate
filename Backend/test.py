from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

lara_url = "https://cofs.lara.state.mi.us/SearchApi/Search/Search"
owner1 = "G.M.K., L.L.C."

# LARA
def startLara(url, owner):
    # find chromedriver on machine
    s = Service('../chromedriver/chromedriver')
    driver = webdriver.Chrome(service = s)

    #open url in Chrome
    driver.get(url)

    time.sleep(3)

    driver.find_element(By.ID, "txtEntityName").send_keys(owner)

    time.sleep(3)

    driver.find_element(By.ID, "SearchSubmit").click()

    time.sleep(3)

    # TODO IF THERE ARE MULPITPLE OPTIONS FOR LLC CHECK THE ADDRESS FROM LANDVISON
    driver.find_element(By.XPATH, '//a[@href="' + "https://cofs.lara.state.mi.us/CorpWeb/CorpSearch/CorpSummary.aspx?token=nBxILn58HwVtv4JMRDwTm1cWblopjmzIgq3FCQzRMH7Z0mRAdeXC1B5BhZoRn0rX3c+Fp+Gbnx2wRL9zMGX1/sqhAMEqWytza0G4dL88Kii9r8OTSljKNqvdnbvImpekDgIM4oOuLyKYNJ5StGnZPZoKheK8QThGI0ug80NLPCzCtiv7EGbX4jSx3ouV2Zjy5Qm+v6OzxOMA/HplVdLzxkw3cZwjP27lAx5LCRGE2ZFSc0ygP37CQCJ5pQFzVU7uCL9rpuRfy5+xp3WO0wsgZTfDSJRqmg+Ff1cDuBTDo/tWBmbGZ5EtFbd7cBsUl4qwkAVNmUcdtgRQ7xoNebsN5AeSWszabZBf" + '"]').click()
    time.sleep(3)

    resident_element = driver.find_element(By.ID, "MainContent_lblResidentAgentName")
    resident = resident_element.text
    return resident

    # TODO GET FIRST NAME FROM THIS RESIDENT
    
    # TODO GET LAST NAME FROM THIS RESIDENT

startLara(lara_url, owner1)


# Jacob's Notes 10-6-23
# Download selenium, chromedriver, and openpyxl to setup my environment
# Put a chrome driver in the project file so it is not dependent on system-specific paths 
#   May have an issue because everyone using this program could possibly not have the same version of chrome, for now we are using "chromedriver mac-arm64 Version: 117.0.5938.149"
#   Only idea I have of getting around this issue is to run a Virtual Machine when we start selling this so the chromedriver is consistent