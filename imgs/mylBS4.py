import requests, os
from io import open
from bs4 import BeautifulSoup

# 1. obtener html
URL_BASE = "https://api.myl.cl/static/cards/19/001.png"
response = requests.get(URL_BASE)
# html_contenido = response.text
# print(html_contenido)
# soup = BeautifulSoup(html_contenido, "html.parser")


# hago un contador para las ediciones partiendo desde el valor EEE
# hago un contador para las cartas partiendo desde el valor CCC
# hago un request sobre la API de TOR usando los endpoints "/EEE/CCC.png"
# si la respuesta es diferente a 404 entonces hasta obtener el 404 aumentare el contador de cartas CCC
# descargo por cada pasada las IMG de las cartas

def format_carta(contador):
    contador_carta = contador
    carta = str(contador_carta)
    if len(carta) < 10: 
        carta = carta.zfill(3)
    elif len(carta) < 100 and len(carta) > 9:
        carta = carta.zfill(3)

    return carta

def crear_carpeta():
    carpeta = input("Ingresa el nombre de la carpeta a crear >> ")
    carpeta = carpeta.title()
    carpeta = carpeta.replace(" ", "-")
    os.mkdir(carpeta)
    return carpeta

def descargar_imgs():
    edicion = input("Ingresa el numero de Edicion >> ")
    directorio = crear_carpeta()
    print(f"SE CREO EL DIRECTORIO '{directorio}'")
    i = 1
    print("DESCARGANDO ...")
    while(i < 400):
        carta_formateada = format_carta(i)
        URL_BASE = f"https://api.myl.cl/static/cards/{edicion}/{carta_formateada}.png"
        response = requests.get(URL_BASE)

        if response.status_code != 404:
            with open(f'{directorio}/{carta_formateada}.png', 'wb') as filePng:
                filePng.write(response.content)
        else:
            print(response.status_code)
            break
        print(f'{directorio}/{carta_formateada}.png')
        i += 1

    print(f"FINALIZADO\nSE DESCARGARON HASTA {i} CARTAS")

descargar_imgs()