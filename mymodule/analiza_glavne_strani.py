from bs4 import BeautifulSoup
import requests, traceback
import re
import os



def create_url(zacetek, konec, osebe, okolica, kraj, glavni_naslov, i):
    """Funkcija ustvari željen url"""
    
    if i == 2:
        for x in [zacetek, konec]:
            if not  re.match(r"\d{2}.\d{2}.\d{4}", x):
                print("Datume piši v obliki kot 01.01.2001")
                return None
        url = f"https://www.apartmanija.hr/apartmani/{glavni_naslov}"
        return url
    else:    
        zacetek, konec = str(zacetek), str(konec)
        if osebe != int(osebe):
            print("Napišite osebe kot število")
            return None
        if osebe > 12:
            osebe = 13
        for x in [zacetek, konec]:
            if not  re.match(r"\d{2}.\d{2}.\d{4}", x):
                print("Datume piši v obliki kot 01.01.2001")
                return None
            
        url = (f"https://www.apartmanija.hr/pretraga/apartmani/r:" 
        f"{okolica}+c:{kraj}+osobe:{osebe}+start:{zacetek}+end:{konec}")
        return url


def url_to_soup(url):
    """Funkcija pridobi html željene strani"""
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return BeautifulSoup(response.content, "html.parser")
        else:
            print("URL ni bil najden")
            return None
        
    except Exception:
        print(f"Napaka pri nalaganju {url}:\n {traceback.format_exc()} ")
        return None
    
    
def nastavi_directory():
    """Funkcija ustvari shranjevanje_strani in vrne njeno lokacijo"""
    
    pot_do_skripte = os.path.abspath(__file__)
    pot_do_nadmape = os.path.dirname(os.path.dirname(pot_do_skripte))
    tarca = os.path.join(pot_do_nadmape, 'shranjevanje_strani')
    
    if not os.path.exists(tarca):
        os.makedirs(tarca)
  
    return tarca

    
def izbrisi_vse_datoteke_v_mapi():
    """Funkcija izprazni mapo shranjevanje_strani."""
    
    #nastavi_directory()
    mapa = nastavi_directory()
    try:
        seznam_datotek = os.listdir(mapa)
        
        for datoteka in seznam_datotek:
            pot_do_datoteke = os.path.join(mapa, datoteka)
            if os.path.isfile(pot_do_datoteke):
                os.remove(pot_do_datoteke)
    
    except Exception as e:
        print(f"Napaka pri brisanju datotek v mapi '{mapa}': {e}")    
    

def save_soup_to_file(soup, filename):
    """Funkcija shrani stran v datoteko."""
    
    directory = nastavi_directory()
    text = str(soup)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as izhod:
        izhod.write(text)
    return None


def kapaciteta_uredi(sez):
    """
    Funkcija izlušči podatke iz seznama ki ima nize oblike "od 1 do 11 osoba u 2 apartmana"
    vrne pa seznam seznamov oblike [od,do]. """
    
    kapaciteta = []
    for stvar in sez:
        stevila = re.findall(r'\d+', stvar)
        stevila = list(map(int, stevila))
        if stevila == []:
            kapaciteta.append("?")
        if len(stevila) == 1:
            kapaciteta.append(stevila*2)
        else:
            kapaciteta.append(stevila[:2])
    return kapaciteta


def luscenje_grobo(soup):
    """Funkcija izlušči glavne podatke in vrne sezname oblik: [ime, cena, kapaciteta, povezava]."""
    
    imena = soup.find_all("p", class_="prop_name")
    imena = [geslo.text.strip() for geslo in imena]
    
    kapaciteta = soup.find_all("div", class_="prop_body")
    kapaciteta = [geslo.text.strip()[11:] for geslo in kapaciteta]
    kapaciteta = kapaciteta_uredi(kapaciteta)
    
    cena_blok = soup.find_all("div", class_="prop_footer_prc")
    cena = [blok.find_all("span")[1] for blok in cena_blok]
    cena = [float(geslo.text.strip()[2:]) for geslo in cena]

    povezava_blok = soup.find_all("div", class_="prop_header")
    povezava = [blok.find("a", class_="ff1").get("href") for blok in povezava_blok]
    
    return [[a, b, c, d] for (a, b, c, d) in zip(imena, cena, kapaciteta, povezava)]


def pridobi_soups(dobri):
    """Funkcija vrne seznam Soup vsebin, iz podstrani."""
    
    soups = []
    for (povezava, i) in zip(dobri, range(1, len(dobri) + 1)):
        soup_n = url_to_soup(povezava)
        save_soup_to_file(soup_n, f"soup{i}.txt")
        soups.append(soup_n)
        
    return soups