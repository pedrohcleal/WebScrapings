import asyncio
import os
from dotenv import load_dotenv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep


async def login(driver, email, password, url):
    driver.get(url)
    WebDriverWait(driver, 20).until(
        ec.presence_of_element_located((By.ID, "Email"))
    ).send_keys(email)
    driver.find_element(By.ID, "Passwd").send_keys(password)
    driver.find_element(By.ID, "logar").click()
    await asyncio.sleep(3)


async def get_total_documents(driver):
    elemt_quant = driver.find_element(
        By.CSS_SELECTOR,
        "div.pull-left > span[data-original-title='Total de documentos']",
    )
    docs_quant = elemt_quant.find_element(By.CSS_SELECTOR, "b").text
    return float(docs_quant.replace(",", ""))


async def scrape_documents(driver, pags_num):
    cont = 0
    list_names = []
    for page in range(pags_num):
        driver.get(
            f"https://secure.d4sign.com.br/...p={page}..."
        )  # substituir endereço pelo correto
        await asyncio.sleep(5)  # Espera a página carregar
        elementos_span = driver.find_elements(
            By.CSS_SELECTOR, "span[id^='nome_documento']"
        )
        for elemento_span in elementos_span:
            nome_documento = elemento_span.find_element(
                By.CSS_SELECTOR, "b"
            ).text  # Obter o texto dentro das tags <b>
            list_names.append(nome_documento)
            cont += 1
            print(nome_documento)
        print(f"Número de arquivos verificados até o momento = {cont}")
        print(f"Página: {page}")
    return list_names


def generate_file_from_list(items, filename):
    with open(filename, "w") as file:
        for item in items:
            file.write(str(item) + "\n")


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
    total_documents = await get_total_documents(driver)
    pags_num = round(total_documents / 20)
    print(f"Número total de páginas = {pags_num}")
    print(f"Quantidade total de documentos: {total_documents}")
    list_names = await scrape_documents(driver, pags_num + 1)
    generate_file_from_list(list_names, "nomes dos docs")
    driver.quit()


if __name__ == "__main__":
    asyncio.run(main())
