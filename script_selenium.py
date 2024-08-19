from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager   
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urljoin
from time import sleep
import requests

def tamanhos(driver):
    try:
        seletor_tamanho = '#talla2'
        select_tag = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, seletor_tamanho))
        )
        select_tag.click()
        element_present = EC.presence_of_element_located((By.ID, 'talla2'))
        WebDriverWait(driver, 10).until(element_present)
        print(element_present)
        tamanhos = [option.text for option in element_present]
        print(f'Tamanhos: {tamanhos}')
    except Exception as e:
        print(f'Erro ao encontrar os tamanhos: {e}')

def preco(driver):
    try:
        seletor_preco = '#js-precio'
        preco_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, seletor_preco))
        )
        preco = preco_element.text
        print(f'Preço: {preco}')
    except Exception as e:
        print(f'Erro ao encontrar o preço: {e}')

def titulo(driver):
    try:
        seletor_titulo = '#js-titulo_nombre_producto'
        titulo_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, seletor_titulo))
        )
        titulo = titulo_element.text
        print(f'Título: {titulo}')
    except Exception as e:
        print(f'Erro ao encontrar o título: {e}')

def baixar_imagem(driver, url):
    try:
        seletor_imagem = 'img#zoom_01'
        img_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, seletor_imagem))
        )
        img_url = urljoin(url, img_element.get_attribute('src'))
        img_data = requests.get(img_url).content
        with open('imagem.jpg', 'wb') as handler:
            handler.write(img_data)
        print("Imagem baixada com sucesso!")
    except Exception as e:
        print(f'Erro ao baixar a imagem: {e}')

if __name__ == '__main__':
    URL = 'https://www.tradeinn.com/goalinn/en/adidas-world-cup-football-boots/118593/p'
    
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Configura o serviço do ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(URL)

        baixar_imagem(driver, URL)
        titulo(driver)
        preco(driver)
        tamanhos(driver)
        sleep(5)

    finally:
        driver.quit()
