import requests
from bs4 import BeautifulSoup
from time import sleep


def iterar_pag(soup: BeautifulSoup):
    selector = "#listing > div.sc-gsTEea.sc-202cc1e9-2.ezCvIu.SzkqH > div > div > div.sc-hKgJUU.hzqTWi > div > main"
    table = soup.find("div", class_="sc-ccc9eb50-13 cWkplc")

    cont = 0
    print(table)
    # print(f"LEN TABLE = {len(table)}")
    for item in table:
        descricao = item.find("h3")
        preco = item.find(class_="priceCard")
        link = item.find(class_="productLink")
        if descricao and preco and link:
            href_value = link["href"]
            print(f"Placa {cont} = {descricao.text.strip()}")
            print(f"Preço = {preco.text.strip()}")
            print(f"Link = {href_value}")
            print()
        sleep(0.2)
        cont += 1


def percorrer_pags(url):
    for num_page in range(1, 20):
        URL = f"https://www.kabum.com.br/hardware/placa-de-video-vga?page_number={num_page}&page_size=100&facet_filters=&sort=most_searched"
        response = requests.get(URL)
        if response.status_code != 200:
            return print(f"erro no request = {response.status_code}")
        soup = BeautifulSoup(response.text, "html.parser")
        print(soup.title)
        iterar_pag(soup)
        break


if __name__ == "__main__":
    URL = "https://www.kabum.com.br/hardware/placa-de-video-vga?page_number=1&page_size=100&facet_filters=&sort=most_searched"
    print("Iniciando Scraping, URL =", URL)

    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    # Simulação de clique em botões de cookies e seleção de itens por página
    # (em BeautifulSoup, não há interação como no Selenium, então precisa ser tratado de outra forma)

    percorrer_pags(URL)
