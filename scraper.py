import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys

# Verificar si se proporcionó una URL como argumento
if len(sys.argv) < 2:
    print("Uso: python scraper.py <URL>")
    sys.exit(1)

# URL proporcionada por el usuario
base_url = sys.argv[1]

# Obtener la página inicial
try:
    response = requests.get(base_url)
    response.raise_for_status()  # Lanza un error si la respuesta no es 200
except requests.exceptions.RequestException as e:
    print(f"Error al acceder a la URL: {e}")
    sys.exit(1)

# Analizar el HTML
soup = BeautifulSoup(response.text, "html.parser")

# Extraer enlaces internos
links = set()
for link in soup.find_all("a", href=True):
    full_url = urljoin(base_url, link["href"])
    if full_url.startswith(base_url):  # Solo enlaces internos
        links.add(full_url)

# Imprimir todas las URLs encontradas
print("\nEnlaces internos encontrados:")
for url in links:
    print(url)
