import re
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

# URL para a primeira requisição
url1 = f"https://www.car.gov.br/publico/imoveis/getImovel?lat=-15.531894&lng=-47.367931"

# Inicializar o navegador usando o Firefox com as opções configuradas
driver = webdriver.Firefox()

try:
    # Faz a primeira requisição
    driver.get(url1)  # in seconds

    # Faz a segunda requisição (mesma URL)
    driver.get(url1)
    driver.implicitly_wait(1)  # in seconds

    # Obter o conteúdo da segunda requisição usando o Selenium
    content2 = driver.page_source

    # Encontrar a string JSON usando expressões regulares (regex)
    json_match = re.search(r'{"type":"FeatureCollection".*}', content2, re.DOTALL)

    if json_match:
        json_text = json_match.group()

        # Analisar o JSON
        data = json.loads(json_text)

        codigo = data['features'][0]['properties']['codigo']

        # Imprimir o código no console
        print("Código do JSON:")
        print(codigo)
    else:
        print("Nenhum JSON encontrado na página.")

finally:
    # Fechar o navegador após as requisições
    driver.quit()