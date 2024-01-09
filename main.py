from bs4 import BeautifulSoup
import requests

root = 'https://subslikescript.com'
website = f'{root}/movies'
resultado = requests.get(website)
contenido = resultado.text
soup = BeautifulSoup(contenido, 'lxml')
# print(soup.prettify())
box = soup.find('article', class_='main-article')

# Lista de todas las peliculas
links = []
for link in box.find_all('a', href=True):
    links.append(link['href'])

for link in links:
    website = f'{root}/{link}'
    resultado = requests.get(website)
    contenido = resultado.text
    soup = BeautifulSoup(contenido, 'lxml')

    box = soup.find('article', class_='main-article')

    titulo = box.find('h1').get_text()
    transcripcion = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

    with open(f'{titulo}.txt', 'w', encoding='utf-8') as file:
        file.write(transcripcion)
