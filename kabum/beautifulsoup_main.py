# TO DO
# TO DO

import requests
from bs4 import BeautifulSoup
from time import sleep

# Função para processar cada página
def iterar_pag(soup):
    # Localiza os itens da tabela
    table_selector = "#listing > div.sc-gsTEea.sc-202cc1e9-2.ezCvIu.SzkqH > div > div > div.sc-hKgJUU.hzqTWi > div > main > *"
    table = soup(table_selector)

    cont = 0
    print(f"LEN TABLE = {len(table)}")

    for item in table:
        descricao = item.find("h3")
        preco = item.find(class_="priceCard")

        if descricao and preco:
            print(f"Placa {cont} = {descricao.text}")
            print(f"Preço = {preco.text}")
            print()
        cont += 1
        sleep(0.2)


# Função para percorrer as páginas
def percorrer_pags(url):
    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        iterar_pag(soup)

        # Verifica se existe o botão para próxima página
        next_button = soup.select_one("#listingPagination > ul > li.next > a")
        if next_button:
            url = next_button["href"]
            print(f"Indo para a próxima página: {url}")
            sleep(2)
        else:
            print("Fim das páginas")
            break


if __name__ == "__main__":
    URL = "https://www.kabum.com.br/hardware/placa-de-video-vga"
    print("Iniciando Scraping, URL =", URL)

    percorrer_pags(URL)
