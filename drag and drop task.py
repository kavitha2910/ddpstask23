from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
source_element=driver.find_element(By.XPATH,"//div[@id='draggable']")
target_element=driver.find_element(By.XPATH,"//div[@id='droppable']")
actions=ActionChains(driver)
actions.drag_and_drop(source_element,target_element).perform()
time.sleep(50)
driver.quit() 
