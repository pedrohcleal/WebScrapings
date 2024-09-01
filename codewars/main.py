from chrome_config import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium import webdriver
from time import sleep


def perfom(driver: webdriver.Chrome):
    # Iterar sobre todas as soluções, precisa estar com a pagina inteira aberta na aba
    # Solutions
    class_name = "list-item-solutions"
    table = driver.find_elements(By.CLASS_NAME, class_name)
    # print(table)
    for index, item in enumerate(table):
        driver.execute_script("arguments[0].scrollIntoView();", item)
        sleep(0.4)


if __name__ == "__main__":
    url = "https://www.codewars.com/users/sign_in"
    try:
        driver.get(url)
        sleep(120)
        perfom(driver)
        # sleep(15)
    finally:
        driver.quit()
