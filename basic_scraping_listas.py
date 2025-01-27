import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://books.toscrape.com/'

encabezados = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

respuesta = requests.get(url,headers=encabezados)

def scraping_data(first,second):
    lista = []

    if respuesta.status_code == 200:
        soup = BeautifulSoup(respuesta.text, 'html.parser')
        sections = soup.find_all(first)
        for section in sections:
            busqueda = section.find_all(second)
            for find in busqueda:
                lista.append(find.get_text(strip=True))
    else:
        print(f"Error al acceder a la página: {respuesta.status_code}")

    return lista

def scraping_price(first,second):
    lista = []

    if respuesta.status_code == 200:
        soup = BeautifulSoup(respuesta.text, 'html.parser')
        sections = soup.find_all(first)
        for section in sections:
            busqueda = section.find_all(second)
            for find in busqueda:
                convert_word = str(find.get_text(strip=True))
                if convert_word.startswith("Â£"):                
                    lista.append(convert_word)
                else:
                    continue
    else:
        print(f"Error al acceder a la página: {respuesta.status_code}")

    return lista

lista_libros = scraping_data('h3','a')
lista_precios = scraping_price('article','p')

df = pd.DataFrame({
    'Libros': lista_libros,
    'Precios': lista_precios
})

print(df)

