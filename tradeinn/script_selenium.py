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
from googletrans import Translator
from to_pdf import PDF

translator = Translator()


def descricao(driver):
    try:
        seletor_tamanho = "#desc"
        select_tag = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, seletor_tamanho))
        )
        # translated = translator.translate(text= select_tag.text, src='en', dest='pt')
        print(f"Descrição = {select_tag.text}\n")
        # print(f'Descrição traduzida = {translated.text}')
        return str(select_tag.text)
    except Exception as e:
        print(f"Erro ao encontrar descrição: {e}")


def tamanhos(driver):
    try:
        seletor_tamanho = "#talla2"
        select_tag = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, seletor_tamanho))
        )
        driver.execute_script("arguments[0].scrollIntoView();", select_tag)
        select_tag.click()
        options = select_tag.find_elements(By.TAG_NAME, "option")
        # Itera sobre as opções e imprime o texto de cada uma
        for option in options:
            print(option.text)
        return [option.text for option in options]
    except Exception as e:
        print(f"Erro ao encontrar os tamanhos: {e}")


def preco(driver):
    try:
        seletor_preco = "#js-precio"
        preco_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, seletor_preco))
        )
        preco = preco_element.text
        print(f"Preço: {preco}")
        return preco
    except Exception as e:
        print(f"Erro ao encontrar o preço: {e}")


def titulo(driver):
    try:
        seletor_titulo = "#js-titulo_nombre_producto"
        titulo_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, seletor_titulo))
        )
        titulo = titulo_element.text
        print(f"Título: {titulo}")
        return titulo
    except Exception as e:
        print(f"Erro ao encontrar o título: {e}")


def get_imagem(driver, url):
    try:
        seletor_imagem = "img#zoom_01"
        img_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, seletor_imagem))
        )
        img_url = urljoin(url, img_element.get_attribute("src"))
        img_data: bytes = requests.get(img_url).content
        # with open('imagem.jpg', 'wb') as handler:
        #     handler.write(img_data)
        # print("Imagem baixada com sucesso!")
        return img_data
    except Exception as e:
        print(f"Erro ao baixar a imagem: {e}")


if __name__ == "__main__":
    URL = "https://www.tradeinn.com/goalinn/en/adidas-world-cup-football-boots/118593/p"

    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Configura o serviço do ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    produto = {}

    try:
        driver.get(URL)
        cookie = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#onetrust-accept-btn-handler")
            )
        )
        cookie.click()
        sleep(3)
        produto["imagem"] = get_imagem(driver, URL)
        print()
        produto["titulo"] = titulo(driver)
        print()
        produto["preco"] = preco(driver)
        print()
        produto["tamanho"] = tamanhos(driver)
        print()
        produto["descricao"] = descricao(driver)

        pdf = PDF()
        pdf.add_page()

        pdf.add_product_row(produto)

        # Salvar o PDF
        pdf.output("catalogo_produtos.pdf")
        print("\npdf concluído")
    finally:
        driver.quit()
