from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movies'
ROOT = 'https://subslikescript.com/'

resultado = requests.get(website)

contenido = resultado.text

soup = BeautifulSoup(contenido, 'lxml')
# print(soup.prettify())

# Lista de todas las peliculas
allMoviesBox = soup.find('article', class_='main-article')

links = []
for link in allMoviesBox.find_all('a', href=True):
    links.append(ROOT + link['href'])

print(links)

# box = soup.find('article', class_='main-article')
# titulo = box.find('h1').get_text()
# transcripcion = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

# with open(f'{titulo}.txt', 'w', encoding='utf-8') as file:
#     file.write(transcripcion)
