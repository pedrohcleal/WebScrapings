import asyncio
import os
import math
from dotenv import load_dotenv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import tracemalloc

tracemalloc.start()

load_dotenv()


async def login(driver, email, password, url):
    driver.get(url)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "Email"))
    ).send_keys(email)
    driver.find_element(By.ID, "Passwd").send_keys(password)
    driver.find_element(By.ID, "logar").click()
    sleep(3)


async def scrape_documents(driver, pags_num):
    cont = 0
    for page in range(pags_num):
        driver.get(
            "https://secure.d4sign.com.br/...p={page}..."
        )  # substituir endereço pelo correto
        sleep(2)

        # Encontra todos os blocos de botões de download
        rows = driver.find_elements(By.CSS_SELECTOR, "#contratos > tbody > tr")
        for i, row in enumerate(rows, start=1):
            try:
                # Seletor específico para o botão em cada linha da tabela
                button = row.find_element(By.CSS_SELECTOR, "td:nth-child(6) > div > i")

                # Scroll até o botão
                driver.execute_script("arguments[0].scrollIntoView(true);", button)
                sleep(0.2)

                # Clica no botão de dropdown usando JavaScript para evitar interferências
                driver.execute_script("arguments[0].click();", button)
                print(f"Botão clicado na linha {i}")
                sleep(0.2)

                # Localiza a lista de opções
                options_list = row.find_element(
                    By.CSS_SELECTOR, "td:nth-child(6) > div > ul"
                )

                # Encontra a opção desejada e clica nela
                download_option = options_list.find_element(
                    By.CSS_SELECTOR, "li:nth-child(1) > a > b"
                )
                driver.execute_script("arguments[0].click();", download_option)
                print(f"Download iniciado na linha {i}")

                sleep(0.5)
                # Espera até que a janela de download seja fechada
                WebDriverWait(driver, 35).until(
                    EC.invisibility_of_element_located(
                        (By.CSS_SELECTOR, "div.modal-content")
                    )
                )
                print(f"Janela de download fechada na linha {i}")

                # Espera um tempo adicional para o download terminar
                sleep(0.5)

                cont += 1

            except Exception as e:
                print(f"\nERRO ERRO - Ocorreu um erro na linha {i}: {e}\n")
                print(f"Pagína em que ocorreu o erro: {page}")
                raise e

        print(f"Número de arquivos verificados até o momento = {cont}")
        print(f"Página: {page}")

    return print("Todas as páginas verificadas com sucesso")


async def main():
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.headless = True  # Executar em modo headless (sem interface gráfica)
    driver = webdriver.Chrome(service=service, options=options)

    # Definindo as credenciais e URL
    email = os.environ.get("email")
    password = os.environ.get("senha")
    url = "url_dos_seus_cofres_d4sign"

    await login(driver, email, password, url)

    total_documents = 354  # inserir qtd
    pags_num = math.ceil(total_documents / 20)
    print(f"Número total de páginas = {pags_num}")
    print(f"Quantidade total de documentos: {total_documents}")
    await scrape_documents(driver, pags_num)
    driver.quit()


if __name__ == "__main__":
    asyncio.run(main())
