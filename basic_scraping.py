import requests
from bs4 import BeautifulSoup

url = 'https://www.cafeteria.com/ecommerce/section'

respuesta = requests.get(url)

if respuesta.status_code == 200:
    soup = BeautifulSoup(respuesta.text, 'html.parser')

    sections = soup.find_all('section')

    busqueda = ('a','h4')

    for section in sections:
         a_tags = section.find_all(busqueda)
         for a_tag in a_tags:
             convert_word = str(a_tag.get_text(strip=True))

             if convert_word.isupper():
                 print(f'\033[32m{convert_word}\033[0m')
             else:
                 print(convert_word)
else:
    print("Hubo un error al obtener las maquina")