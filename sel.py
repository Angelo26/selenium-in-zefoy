from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.zefoy.com/")
driver.implicitly_wait(10)


capRead = driver.find_element('xpath',"/html/body/div[5]/div[2]/form/div/div/img")
# capWrite = driver.find_element('xpath',"/html/body/div[5]/div[2]/form/div/div/div/input")
# capWrite.clear()
# capWrite.send_keys("Angel") 
# capBtn = driver.find_element('class name','submit-captcha')
# capBtn.click()