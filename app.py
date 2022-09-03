# import required modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os

myId='divyansh.anand.19c@iitram.ac.in'
myPassword='Hardik@0908'	
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_extension('IDM-Integration-Module.crx')
driver = webdriver.Chrome(executable_path='chromedriver.exe', options=opt)
driver.get('https://sleepdata.org/datasets/mros/files/polysomnography/edfs/visit1?page=8')

def checkLoginState():   # Check if user is logged in
    try:
        driver.find_element(By.XPATH,"//a[@href='/login']")
        
        isPresent = True;
    except:
        isPresent = False;
    return isPresent;

def Login():                # Login to sleepdata.org
    driver.find_element(By.XPATH,"//input[@id='user_email']").send_keys(myId)
    driver.find_element(By.XPATH,"//input[@id='user_password']").send_keys(myPassword)
    driver.find_element(By.XPATH,"//input[@type='submit']").click()
print(checkLoginState())
#calling Login function if user is not logged in to sleepdata.org
if(checkLoginState()==False):
    print("Already logged in")
else:
    driver.find_element(By.XPATH,"//a[@href='/login']").click()
    try:
        myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="sign-up-form-title"]')))
        Login()
        print("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")
    print("Logged in")
#function to check if file is already downloaded
def checkFile():
    pathOfVisit1="C:\\Users\\singh\\OneDrive\\Desktop\\dev\\NSRR-Dataset-Download\\download"
    fileList=os.listdir(pathOfVisit1)
    return fileList
#function to download file
def logLinks():
    for i in range(1,31):
        driver.get('https://sleepdata.org/datasets/mros/files/polysomnography/annotations-events-profusion/visit1?page='+str(i))
        time.sleep(1)
        links = driver.find_elements(By.XPATH,"//a[@data-turbolinks='false']")
        listFile=checkFile()
        for link in links:
            fileName=link.get_attribute('innerHTML')
            if(fileName in listFile):
                print("File already downloaded")
                pass
            else:
                print("Downloading file: "+fileName)
                try:
                    link.click()   
                except:
                    try:
                        link.click()
                        time.sleep(1)
                    except:
                        pass

logLinks()