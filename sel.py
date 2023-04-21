from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytesseract 
import PIL.Image

options = Options()
# options.add_argument('headless')
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.zefoy.com/")
driver.implicitly_wait(10)

def enterCode():
    def saveCode():
        capRead = driver.find_element('xpath',"/html/body/div[5]/div[2]/form/div/div/img")
        capRead.screenshot("code.png")

    def readCode():
        saveCode()
        myconfig = r"--psm 6 --oem 3"
        return pytesseract.image_to_string(PIL.Image.open("code.png"), config=myconfig)
    
    def writeCode():
        givenCode = readCode()
        capWrite = driver.find_element('xpath',"/html/body/div[5]/div[2]/form/div/div/div/input")
        capWrite.clear()
        capWrite.send_keys(givenCode)

    def clickCapBtn(): 
        writeCode()
        capBtn = driver.find_element('class name','submit-captcha')
        capBtn.click()

    clickCapBtn()

enterCode()