import requests
from bs4 import BeautifulSoup

# URL de la página que deseas scrapear
url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREYzY3pVU0JtVnpMVFF4T1NnQVAB?hl=es-419&gl=AR&ceid=AR%3Aes-419"
# Realiza la solicitud HTTP
response = requests.get(url)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    # Carga el contenido HTML en BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encuentra todas las etiquetas <a> con href que comienza con './read/'
    links = soup.find_all('a', href=lambda href: href and href.startswith('./read/'))

    contents = [link.get_text(strip=True) for link in links if link.get_text(strip=True)]
    # Imprime los valores de href
    for link in links:
        print(link.get_text(strip=True))
       

else:
    print('Error al hacer la solicitud:', response.status_code)

print(contents)
print(len(contents))