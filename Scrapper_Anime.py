from typing import Counter
from bs4 import BeautifulSoup
import requests
from Modulos import Numero_Random_Rango

class Objetos_:
    def __init__( self, name, puntaje, info, link ):
        self.name = str(name)
        self.puntaje = str(puntaje)
        self.info = str(info)
        self.link = str(link)

def Anime_Scrapper():
    Numero_Random = str(Numero_Random_Rango(21350))
    Texto_HTML = requests.get('https://myanimelist.net/topanime.php?limit=' + Numero_Random).text
    soup = BeautifulSoup(Texto_HTML, 'lxml')

    animes = soup.find_all('tr', class_= 'ranking-list')
    
    lista_De_Animes = []
    
    for anime in animes:
        anime_Nombre = anime.find('h3',class_="hoverinfo_trigger fl-l fs14 fw-b anime_ranking_h3").text
        anime_Puntaje = anime.find('td', class_="score ac fs14").text
        anime_Info = anime.find('div', class_="information di-ib mt4").text
        anime_Link = anime.div.h3.a['href']

        puntaje_Fixed = anime_Puntaje.replace('\n', '')
        linkText = "<a href='{}'>{}</a>".format(anime_Link, anime_Nombre)
        link_Fixed = linkText
        info_Fixed = 'Info: \n' + anime_Info.replace( 'members', 'Vistas' ).replace( 'eps', 'Episodios' ).replace( '\n', '', 1 )[:-7]
        
        try:
            push_Ultimo_Anime = Objetos_( anime_Nombre, puntaje_Fixed, info_Fixed, link_Fixed )
            lista_De_Animes.append(push_Ultimo_Anime)            
        except:
            continue

    Numero_Random_2 = Numero_Random_Rango(len(lista_De_Animes))
    return lista_De_Animes[Numero_Random_2].puntaje, lista_De_Animes[Numero_Random_2].info, lista_De_Animes[Numero_Random_2].link

print(Anime_Scrapper())