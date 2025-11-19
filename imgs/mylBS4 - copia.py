import requests, os
from io import open
from bs4 import BeautifulSoup
import csv

#FUNCIONES PARA TRABAJAR EL CSV
def format_carta(s_num):
    carta = s_num
    if len(carta) < 10: 
        carta = carta.zfill(3)
    elif len(carta) < 100 and len(carta) > 9:
        carta = carta.zfill(3)

    return carta

def exportar_csv(cartas:list, edicion):
    with open("LISTADO-CARTAS.csv", "a", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(cartas + [f'{edicion}\{format_carta(cartas[0])}.png'])


#PETICION GET
def req_get(URL_BASE):
    respuesta = requests.get(URL_BASE)
    html = respuesta.text
    return html


#DESCARGA DE IMGS
def format_cartas(contador):
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

def descargar_imgs(inicia:int, edicion:int):
    # edicion = input("Ingresa el numero de Edicion >> ")
    directorio = crear_carpeta()
    print(f"SE CREO EL DIRECTORIO '{directorio}'")
    i = 1
    print("DESCARGANDO ...")
    while(i < 400):
        carta_formateada_url = format_carta(str(i))
        carta_formateada_png = format_cartas(int(inicia))
        URL_BASE = f"https://api.myl.cl/static/cards/{edicion}/{carta_formateada_url}.png"
        response = requests.get(URL_BASE)

        if response.status_code != 404:
            with open(f'{directorio}/{carta_formateada_png}.png', 'wb') as filePng:
                filePng.write(response.content)
        else:
            print(response.status_code)
            break
        print(f'{directorio}/{carta_formateada_png}.png')
        i += 1
        inicia += 1

    print(f"FINALIZADO\nSE DESCARGARON HASTA {i} CARTAS")



#REQUEST GET
# html = req_get("https://myl.fandom.com/es/wiki/Lista_de_cartas_de_Espada_Sagrada")
html = req_get("https://myl.fandom.com/es/wiki/Lista_de_cartas_de_Cruzadas")
# html = req_get("https://myl.fandom.com/es/wiki/Lista_de_cartas_de_Hel%C3%A9nica")
# html = req_get("https://myl.fandom.com/es/wiki/Lista_de_cartas_de_Imperio")

#OBTENCION DE DATOS POR BEAUTIFULSOUP
wscraper = BeautifulSoup(html, "html.parser")
td_tags = wscraper.findAll("tr")

#LIMPIO Y PREPARO LOS DATOS EN ARRAYS
td_tags.pop(0)
td_tags.pop(0)
lista = []
edicion = input("Ingresa el numero de Edicion >> ")
print("EXPORTANDO CSV ...")
for td in td_tags:
    carta = (list) (td.get_text().split("\n"))
    longitud = len(carta)
    for i in range(0, longitud): 
        try:
            carta.remove("")
        except:
            break
    
    # print(carta)
    lista.append(carta)
    #EXPORTO UN CSV
    exportar_csv(carta, edicion)

print("CSV EXPORTADO")
print("="*100)
#DESCARGA DE LAS IMAGENES
descargar_imgs(int(lista[0][0]), edicion)







