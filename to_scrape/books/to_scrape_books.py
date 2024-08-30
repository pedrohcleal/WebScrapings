from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from time import sleep


def iterar_pag(driver):
    table = driver.find_elements(
        By.CSS_SELECTOR,
        "#default > div > div > div > div > section > div:nth-child(2) > ol > *",
    )
    cont = 0
    for item in table:
        descricao = item.find_element(By.TAG_NAME, "h3")
        preco = item.find_element(By.CLASS_NAME, "price_color")
        driver.execute_script("arguments[0].scrollIntoView();", preco)
        print(f"Nome do livro{cont} = {descricao.text}")
        print(f"Preço = {preco.text}")
        print()
        sleep(0.4)
        cont += 1


def percorrer_pags(driver):
    iterar_pag(driver)
    try:
        next_element = driver.find_element(
            By.CSS_SELECTOR,
            "#default > div > div > div > div > section > div:nth-child(2) > div > ul > li.next > a",
        )
        next_element.click()
        sleep(1)
    except NoSuchElementException as err:
        print(f"elemento de click next não encontrado, erro = {err}")
        return print("fim")
    print(f"Indo para a próxima página")
    percorrer_pags(driver)


if __name__ == "__main__":
    URL = "https://books.toscrape.com/index.html"
    print("Iniciando Scraping, URL =", URL)

    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Configura o serviço do ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        driver.get(URL)
        sleep(2)
        percorrer_pags(driver)
    finally:
        driver.quit()
