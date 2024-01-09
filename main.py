from bs4 import BeautifulSoup
import requests

root = 'https://subslikescript.com'
website = f'{root}/movies_letter-A'
resultado = requests.get(website)
contenido = resultado.text
soup = BeautifulSoup(contenido, 'lxml')
# print(soup.prettify())

# PAGINACION
# Agarro el elemento UL de las paginaciones
paginacion = soup.find('ul', class_='pagination')
# Agarro todos los elementos LI
paginas = paginacion.find_all('li', class_='page-item')
ultima_pagina = paginas[-2].text

# Empieza en 1 y termina en otro por ej: range(1, 1000 + 1)
for nPagina in range(1, int(ultima_pagina) + 1)[:2]:
    website = f'{website}?page={nPagina}'
    resultado = requests.get(website)
    contenido = resultado.text
    soup = BeautifulSoup(contenido, 'lxml')

    box = soup.find('article', class_='main-article')

    # Lista de todas las peliculas
    links = []
    for link in box.find_all('a', href=True):
        links.append(link['href'])

    for link in links:
        try:
            resultado = requests.get(f'{root}/{link}')
            contenido = resultado.text
            soup = BeautifulSoup(contenido, 'lxml')

            box = soup.find('article', class_='main-article')

            titulo = box.find('h1').get_text()
            transcripcion = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

            with open(f'{titulo}.txt', 'w', encoding='utf-8') as file:
                file.write(transcripcion)
        except:
            print('--------- El link no funciona ----------')
            print(link)
