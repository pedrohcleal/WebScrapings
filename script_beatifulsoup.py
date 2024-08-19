import requests
from bs4 import BeautifulSoup as bs4
from urllib.parse import urljoin

def tamanhos(response):
    seletor_tamanho = '#talla2'
    soup = bs4(response.text, 'html.parser')
    print(soup)
    select_element = soup.find('select', id='talla2')
    options = select_element.find_all('option')
    #print(options)
    for option in options:
        value = option['value']
        text = option.get_text(strip=True)
        #print(f'Value: {value}, Text: {text}')
    #print(table.text) 
    pass
    
def preco(response):
    seletor_preco = '#js-precio'
    
    soup = bs4(response.text, 'html.parser')
    table = soup.select_one(seletor_preco)
    print(f' Preço = {table.text}') 
    

def titulo(response):
    seletor_titulo = '#js-titulo_nombre_producto'
    soup = bs4(response.text, 'html.parser')
    table = soup.select_one(seletor_titulo)
    print(f' Título = {table.text}') 
    pass

def baixar_imagem(response, url):
    seletor_imagem = 'img#zoom_01'
    soup = bs4(response.text, 'html.parser')
    img_tag = soup.select_one(seletor_imagem)
    if img_tag and img_tag.has_attr('src'):
        img_url = urljoin(url, img_tag['src'])
        img_data = requests.get(img_url).content
        with open('imagem.jpg', 'wb') as handler:
            handler.write(img_data)
        print("Imagem baixada com sucesso!")
    else:
        print("Tag <img> não encontrada ou sem atributo 'src'.")
    
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    URL = 'https://www.tradeinn.com/goalinn/en/adidas-world-cup-football-boots/118593/p'
    response = requests.get(URL, headers=headers)
    if response.status_code == 200:
        baixar_imagem(response, URL)
        titulo(response)
        preco(response)
        tamanhos(response)
    else:
        print("Não foi possível acessar a página.")
