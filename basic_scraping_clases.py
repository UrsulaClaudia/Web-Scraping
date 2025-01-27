import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'

encabezados = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

respuesta = requests.get(url,headers=encabezados)

class scraping:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    
    def list_scraping(self):
        pass
    

class scraping_books(scraping):
    def __init__(self,first,second):
        super().__init__(first,second)
        self.lista = []

    def list_scraping(self):
        if respuesta.status_code == 200:
            soup = BeautifulSoup(respuesta.text, 'html.parser')
            sections = soup.find_all(self.first)
            for section in sections:
                busqueda = section.find_all(self.second)
                for find in busqueda:
                    self.lista.append(find.get_text(strip=True))
        else:
            print(f"Error al acceder a la página: {respuesta.status_code}")

        return self.lista

class scraping_prices(scraping):
    def __init__(self,first,second):
        super().__init__(first,second)
        self.lista = []

    def list_scraping(self):
        if respuesta.status_code == 200:
            soup = BeautifulSoup(respuesta.text, 'html.parser')
            sections = soup.find_all(self.first)
            for section in sections:
                busqueda = section.find_all(self.second)
                for find in busqueda:
                    convert_word = str(find.get_text(strip=True))
                    if convert_word.startswith("Â£"):                
                        self.lista.append(convert_word)
                    else:
                        continue
        else:
            print(f"Error al acceder a la página: {respuesta.status_code}")

        return self.lista

lista_libros = scraping_books('h3','a')
lista_libros.list_scraping()
lista_precios = scraping_prices('article','p')
lista_precios.list_scraping()

tabla = list(zip(lista_libros.list_scraping(),lista_precios.list_scraping()))
print(f"Libro       |         Precio")
for items in tabla:
    libro, precio = items
    print(f"{libro}  |  {precio}")