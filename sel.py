from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytesseract 
import PIL.Image
import time

opt = Options()
# opt.add_argument('headless')
opt.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)

driver.get("https://www.zefoy.com/")
driver.implicitly_wait(10)

def viewIncreaser():
    
    def enterUrl():
        userUrl = input("Enter the URL here: ")
        
        addViews(userUrl)
        
    def enterCode():
        def saveCode():
            capRead = driver.find_element('xpath',"/html/body/div[5]/div[2]/form/div/div/img")
            capRead.screenshot("code.png")
            writeCode()

        def readCode():
            return pytesseract.image_to_string(PIL.Image.open("code.png"))
        
        def writeCode():
            givenCode = readCode()
            capWrite = driver.find_element('xpath',"/html/body/div[5]/div[2]/form/div/div/div/input")
            capWrite.clear()
            capWrite.send_keys(givenCode)
            clickCapBtn()

        def clickCapBtn():
            capBtns = driver.find_elements('xpath','/html/body/div[5]/div[2]/form/div/div/div/div/button')
            for capBtn in capBtns:
                if bool(capBtns):
                    capBtn.click()
                    break
        saveCode()

    def addViews(userUrl):
        def enterViews():
            enterCode()
            viewsBtns = driver.find_elements('xpath', '/html/body/div[6]/div/div[2]/div/div/div[5]/div/button')
            if (bool(viewsBtns)):
                for viewsBtn in viewsBtns:
                    if bool(viewsBtns):
                        viewsBtn.click()
                        addUrl()
                        break
            else:
                driver.refresh()
                print("Captcha Error")
                enterViews()

        def addUrl():
            tiktokUrl = userUrl
            urlWrite = driver.find_element('xpath',"/html/body/div[10]/div/form/div/input")
            urlWrite.clear()
            urlWrite.send_keys(tiktokUrl)            
            submitUrl()

        def submitUrl():
            submitUrlBtns = driver.find_elements('xpath', '/html/body/div[10]/div/form/div/div/button')
            for submitUrlBtn in submitUrlBtns:
                if bool(submitUrlBtns):
                    submitUrlBtn.click()
                    counterReady()
                    break

        def counterReady():
            getReadyBtns = driver.find_elements('xpath', '/html/body/div[10]/div/div/div[1]/div/form/button')
            if bool(getReadyBtns):

                for getReadyBtn in getReadyBtns:
                    if bool(getReadyBtns):
                        getReadyBtn.click()
                        time.sleep(120)
                        print("again")
                        submitUrl()
                        break
            else:
                time.sleep(120)
                submitUrl()

        enterViews()
    
    enterUrl()

viewIncreaser()