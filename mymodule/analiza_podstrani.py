from bs4 import BeautifulSoup
import re



#Funkcija pretvori nize oblike "10 km" v stevilo metrov
def pretvori_razdalje(niz):
    pattern = r'(\d+)\s?(m|km)\b'

    matches = re.search(pattern, niz)
    stevilo, enota = matches.groups()
    stevilo = int(stevilo)
        
    if enota == 'km':
        return stevilo * 1000
    else:
        return stevilo
    
    
    
#Koda vrne seznam oblike ["Točen naslov", "Morje", "Plaža", "Center", "Trgovina", "Restavracija"]
def luscenje_fino(soups):
    info = []
    naslovi = []
    for soup in soups:
    
        naslov = soup.find("span", {'id': 'property_address', 'itemprop': 'address'})
        if naslov:
            t = naslov.text
            naslovi.append(t.replace(",", "|"))

        #info_blok = soup.find("div", class_="property_more_info")
        info_blok = soup.find('ul', {'id': 'property_dist_list', 'class': 'property_dist_mob'})
        
        info_blok = info_blok.find_all("span")
        x = len(info_blok)
        
        if x < 5:
            dodatek = ["Ni podatka"] * (5 - x)
            info.append([pretvori_razdalje(informacija.text) for informacija in info_blok[:5]] + dodatek)
        else:
            info.append([pretvori_razdalje(informacija.text) for informacija in info_blok[:5]])
        #info je v obliki ["Morje", "Plaža", "Center", "Trgovina", "Restavracija"]
        
    return [naslovi] + [info]



#Funkcija poišče številke, ki nas vodijo do podrobnih cenikov, za določeno stran
#vrne tudi tip stanovanja, naprimer "Studio"
def poisci_pricelist_id(datoteka_soup_stevilka):

    datoteka_path = f'shranjevanje_strani/soup{datoteka_soup_stevilka}.txt'
    vzorec2 = r'<div class="pull-left property_unit_xs">\s*<span>(.*?)</span>\s*</div>\s*<div class="pull-left property_unit_xs">\s*<strong>ID:(\d+)'

    with open(datoteka_path, 'r', encoding="utf-8") as file:
        file_vsebina = file.read()
    
    ujemanja = re.findall(vzorec2, file_vsebina, re.DOTALL)
    tip_stanovanja = [x for (x, y) in ujemanja]
    id = [int(y) for (x, y) in ujemanja]

    return [tip_stanovanja, id]



#Funkcija poišče številke, za vse izbrane strani do len(dobri)-te
def seznam_price_id(n):
    return [poisci_pricelist_id(i) for i in range(1, n+1)]



