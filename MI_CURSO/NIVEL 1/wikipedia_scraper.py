import requests
from lxml import html

##### Primera parte en la que solicitamos la pagina por medio de la librería request ####
##### Necesitamos definir los user-agent y lo que tenemos que imprimir debe ser el texto, no el reponse  ####
encabezados = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
}

url = "https://www.wikipedia.org"

respuesta = requests.get(url, headers=encabezados)
#print(respuesta.text)


#### Ahora vamos a parsear por medio de la libreria lxml => html. Vamos a parsear de dos formas
## La primera por medio de las funciones de lxml
parser = html.fromstring(respuesta.text)
ingles = parser.get_element_by_id("js-link-box-en")  ## Este elemento lo he inspeccionado en la pagina y buscado su ID. Esta funcion viene con lxml
print(ingles. text_content())
## La segunda por medio de xpath
espanol = parser.xpath("//a[@id='js-link-box-es']/strong/text()")
print(espanol)

#### Vamos a recorrer todos los idiomas #####
## Si vemos, todos los idiomas estan en un <a> dentro de un <div> cuya "class = central-featured-lang " y algo más
## Todos ellos guardan la misma estructura  <div class = central-featured-lang xxxx>, dentro <a> y dentro <strong>
idiomas = parser.xpath("//div[contains(@class, 'central-featured-lang')]//strong/text()")
print(idiomas)  #idiomas es una lista, puesto que encuentra todos los divs que conienen esa clase. Para imprimir uno por uno: for idioma in idimas ...


#### Lo mismo, vamos a recoger todos los idiomas pero con lxml
idiomas = parser.find_class('central-featured-lang')
print(idiomas)
for idioma in idiomas:
    print(idioma.text_content())