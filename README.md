![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-brightgreen)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.10%2B-blue)
![Requests](https://img.shields.io/badge/Requests-2.28%2B-blue)

# Web Scrapings

Este repositório contém diferentes automações de web scraping utilizando **Selenium** e **BeautifulSoup** (via requests). Cada pasta refere-se a um site específico ou projeto de scraping, organizando scripts que realizam a extração de dados de forma automatizada.

## Estrutura do Repositório

```bash
web_scrapings/
├── __init__.py               # Inicializador do pacote
├── commands.txt              # Comandos úteis e instruções para rodar os scripts
├── d4sign/                   # Scripts relacionados ao D4Sign
│   ├── __init__.py
│   ├── downloads_automation.py      # Automação de downloads de documentos
│   └── scrapping_name_documents.py  # Extração de nomes de documentos
├── kabum/                    # Scripts relacionados ao site da Kabum
│   ├── __init__.py
│   ├── beautifulsoup_main.py       # Web scraping usando BeautifulSoup
│   └── selenium_main.py            # Web scraping usando Selenium
├── requirements.txt          # Dependências do projeto
├── timeanddate/              # Scripts relacionados ao Time and Date
│   ├── __init__.py
│   └── handler.py                  # Manipulação de dados de temperatura e data
├── to_scrape/                # Scripts relacionados ao site To Scrape
│   └── books/
│       ├── __init__.py
│       └── to_scrape_books.py      # Web scraping de livros
├── tradeinn/                 # Scripts relacionados ao site Tradeinn
│   ├── __init__.py
│   ├── catalogo_produtos.pdf       # Catálogo de produtos (gerado via scraping)
│   ├── logo.png                    # Logotipo do Tradeinn
│   ├── script_selenium.py          # Web scraping usando Selenium
│   └── to_pdf.py                   # Conversão de dados em PDF
```

## Tecnologias Utilizadas

- **Selenium**: Automação de navegação e interação com páginas web.
- **BeautifulSoup**: Extração e análise de dados HTML.
- **Requests**: Para fazer requisições HTTP de forma simples.
  
## Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/pedrohcleal/WebScrapings
   cd WebScrapings
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute os scripts conforme necessário. Por exemplo:
   ```bash
   python kabum/selenium_main.py
   ```

## Contribuição

Contribuições são bem-vindas! Fique à vontade para abrir issues e enviar pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
