from datetime import datetime
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.action_chains import ActionChains

actions = ActionChains(ActionChains)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.invokergame.com/")
driver.maximize_window()
# driver.implicitly_wait(1)
time.sleep(0.5)
# click on clasic
driver.find_element(By.XPATH, "//*[@id=\"GameMenu\"]/div/table/tbody/tr[3]/td[1]/input").click()
# click on without steam
time.sleep(0.5)
driver.find_element(By.XPATH, "//*[@id=\"LoginNotification\"]/div/table/tbody/tr/td[3]/a/span[1]/sub").click()
# start game
time.sleep(1)

driver.find_element(By.XPATH, "//*[@id=\"GameInterface\"]/div[1]/nobr/table/tbody/tr/td/input").click()


def is_element_present(xpath):
    try:
        driver.find_element(By.XPATH, value=xpath)
        return True
    except NoSuchElementException:
        return False


count = 0
for i in range(0, 10):
    if is_element_present('//nobr/table/tbody/tr/td[@id="Spell_0"]/img'):
        ActionChains(driver).send_keys('qqqr').perform()
    elif is_element_present('//nobr/table/tbody/tr/td[@id="Spell_1"]/img'):
        ActionChains(driver).send_keys('qqwr').perform()
    elif is_element_present('//nobr/table/tbody/tr/td[@id="Spell_2"]/img'):
        ActionChains(driver).send_keys('qqer').perform()
    elif is_element_present('//nobr/table/tbody/tr/td[@id="Spell_3"]/img'):
        ActionChains(driver).send_keys('wwwr').perform()
    elif is_element_present('//nobr/table/tbody/tr/td[@id="Spell_4"]/img'):
        ActionChains(driver).send_keys('wwqr').perform()
    elif is_element_present('//nobr/table/tbody/tr/td[@id="Spell_5"]/img'):
        ActionChains(driver).send_keys('wwer').perform()
    elif is_element_present('//nobr/table/tbody/tr/td[@id="Spell_6"]/img'):
        ActionChains(driver).send_keys('eeer').perform()
    elif is_element_present('//nobr/table/tbody/tr/td[@id="Spell_7"]/img'):
        ActionChains(driver).send_keys('eeqr').perform()
    elif is_element_present('//nobr/table/tbody/tr/td[@id="Spell_8"]/img'):
        ActionChains(driver).send_keys('eewr').perform()
    elif is_element_present('//nobr/table/tbody/tr/td[@id="Spell_9"]/img'):
        ActionChains(driver).send_keys('qwer').perform()

x = driver.find_element(By.CLASS_NAME, "StatsMainStatResult")
# xpath //*[@id=\"StatsScreen\"]/div/div[1]

print("Your time was", x.text)
datum = datetime.now()

records = [str(datum) + "  With time: " + str(x.text) + "\n"]
with open('InvogameRecords.txt', 'a') as f:
    f.write('\n'.join(records))

print(records)

time.sleep(1)
driver.quit()

