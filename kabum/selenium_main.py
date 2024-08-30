from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from time import sleep


def iterar_pag(driver):
    table_selector = "#listing > div.sc-gsTEea.sc-202cc1e9-2.ezCvIu.SzkqH > div > div > div.sc-hKgJUU.hzqTWi > div > main > *"
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, table_selector))
    )
    table = driver.find_elements(By.CSS_SELECTOR, table_selector)
    cont = 0
    print(f"LEN TABLE ={len(table)}")
    for item in table:
        descricao = item.find_element(By.TAG_NAME, "h3")
        preco = item.find_element(By.CLASS_NAME, "priceCard")
        link = item.find_element(By.CLASS_NAME, "productLink")
        href_value = link.get_attribute("href")
        driver.execute_script("arguments[0].scrollIntoView();", preco)  # scrollar
        print(f"Placa {cont} = {descricao.text}")
        print(f"Preço = {preco.text}")
        print(f"Link = {href_value}")
        print()
        sleep(0.2)
        cont += 1


def percorrer_pags(driver):
    iterar_pag(driver)
    try:
        next_element = driver.find_element(
            By.CSS_SELECTOR,
            "#listingPagination > ul > li.next > a",
        )
        next_element.click()
        sleep(2)
    except NoSuchElementException as err:
        print(f"elemento de click next não encontrado, erro = {err}")
        return print("fim")
    print(f"Indo para a próxima página")
    percorrer_pags(driver)


if __name__ == "__main__":
    URL = "https://www.kabum.com.br/hardware/placa-de-video-vga"
    print("Iniciando Scraping, URL =", URL)

    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-notifications")

    # Configura o serviço do ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        driver.get(URL)
        sleep(3)
        driver.maximize_window()
        cookie_button = driver.find_element(
            By.CSS_SELECTOR, "#onetrust-accept-btn-handler"
        )
        cookie_button.click()
        itens_por_pag = driver.find_element(By.CSS_SELECTOR, "#Filter > label > select")
        itens_por_pag.click()
        selecionar_itens_por_pag = driver.find_element(
            By.CSS_SELECTOR, "#Filter > label > select > option:nth-child(5)"
        )
        selecionar_itens_por_pag.click()
        itens_por_pag.click()
        percorrer_pags(driver)
    finally:
        driver.quit()
