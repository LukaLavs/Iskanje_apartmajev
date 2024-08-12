from bs4 import BeautifulSoup
import requests, traceback
import re
import os







#Funkcija sprejme datuma začetka in konca potovanja, ter število oseb.
#Nato pa ustvari url do povezave.
#Vedno lahko link do željene podstrani, na strani apartmanija.hr, prilepite tudi sami.
#i predstavlja tip url-ja
def create_url(zacetek, konec, osebe, okolica, kraj, glavni_naslov, i):
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



#Funkcija pridobi html obliko strani
def url_to_soup(url):
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
    
    
    
#Funkcija nastavi ustrezen directory
def nastavi_directory():
    base_dir = os.getcwd()  # To je mapa, kjer se nahaja trenutna skripta
    # Zgradite pot do podmape
    desired_directory = os.path.join(base_dir, 'shranjevanje_strani')
    # Preverite, ali pot obstaja
    if not os.path.exists(desired_directory):
        os.makedirs(desired_directory)
        
    return desired_directory
    
    
#Funkcija izprazni mapo shranjevanje_strani, da preprečimo, da v njej ostanejo neželeni soupi    
def izbrisi_vse_datoteke_v_mapi():
    mapa = nastavi_directory()
    try:
        seznam_datotek = os.listdir(mapa)
        
        for datoteka in seznam_datotek:
            pot_do_datoteke = os.path.join(mapa, datoteka)
            if os.path.isfile(pot_do_datoteke):
                os.remove(pot_do_datoteke)
    
    except Exception as e:
        print(f"Napaka pri brisanju datotek v mapi '{mapa}': {e}")    

    
#Funkcija shrani stran v datoteko.
def save_soup_to_file(soup, filename):
    directory = nastavi_directory()
    text = str(soup)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as izhod:
        izhod.write(text)
    return None



#Funkcija izlušči podatke iz seznama ki ima nize oblike "od 1 do 11 osoba u 2 apartmana"
#vrne pa seznam seznamov oblike [od,do]
def kapaciteta_uredi(sez):
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



#izluščimo glavne podatke, in vrnimo seznam seznamov,
#kjer je posamezen seznam oblike [ime, cena, kapaciteta, povezava]
def luscenje_grobo(soup):
    
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


#Funkcija vrne seznam Soup vsebin, iz podstrani
def pridobi_soups(dobri):
    soups = []
    for (povezava, i) in zip(dobri, range(1, len(dobri) + 1)):
        soup_n = url_to_soup(povezava)
        save_soup_to_file(soup_n, f"soup{i}.txt")
        soups.append(soup_n)
    return soups