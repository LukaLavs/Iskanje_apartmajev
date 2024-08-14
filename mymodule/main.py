import analiza_glavne_strani 
import analiza_podstrani   
import analiza_z_selenium
import graficni_prikaz
import ustvarjanje_tabel



def izlusci_podatke(zacetek, konec, osebe, okolica, kraj, glavni_naslov, i):
    """Funkcija izlušči podatke iz glavne strani."""
    analiza_glavne_strani.izbrisi_vse_datoteke_v_mapi()
    url = analiza_glavne_strani.create_url(zacetek, konec, osebe, okolica, kraj, glavni_naslov, i)
    soup = analiza_glavne_strani.url_to_soup(url)
    analiza_glavne_strani.save_soup_to_file(soup, "soup.txt")
    return analiza_glavne_strani.luscenje_grobo(soup)


def ustvari_df_glavne_strani(zacetek, konec, osebe, okolica, kraj, glavni_naslov, i):
    """Funkcija izlušči podatke iz glavne strani, jih shrani v tabele, in vrne df."""
    a = izlusci_podatke(zacetek, konec, osebe, okolica, kraj, glavni_naslov, i)
    ustvarjanje_tabel.create_excel(a)
    return ustvarjanje_tabel.create_csv(a)


def datum_od_do(zacetek, konec):
    """Funkcija ustvari zapis DD.MM-DD.MM"""
    return zacetek[:5] + "-" + konec[:5]
     
     
def prave_cene(n, seznam_urljev, datum, brskalnik='firefox'):
    """Funkcija vrne seznam velikosti sob in seznam izračunanih cen."""
    a = analiza_podstrani.seznam_price_id(n)
    velikost = [x[0] for x in a]
    b = analiza_z_selenium.tocni_ceniki(seznam_urljev, a, brskalnik)
    c = analiza_z_selenium.izlusci_cenik(b)
    e = []
    for blok in c:
        d = []
        for soba in blok:  
            d.append(analiza_z_selenium.cena_skupaj_in_na_noc(soba, datum))           
        e.append(d)
    return [velikost, e]


def natancne_informacije(df, stevilo_izbranih, zacetek, konec, brskalnik):
    """Funkcija vzame nekaj sob in zbere natančne podatke o sobah."""
    stevilo_izbranih = min(stevilo_izbranih, df.shape[0])
    imena_povezave = ustvarjanje_tabel.povezave_do_izbranih(df, stevilo_izbranih)
    dobri = imena_povezave[1]
    imena = imena_povezave[0]
    soups = analiza_glavne_strani.pridobi_soups(dobri)
    informacije = analiza_podstrani.luscenje_fino(soups)
    
    izracunane_cene = prave_cene(stevilo_izbranih, dobri, datum_od_do(zacetek, konec), brskalnik)
    naslovi = informacije[0]
    razdalje = informacije[1]
    objekti = izracunane_cene[0]
    cenee = izracunane_cene[1]

    info_za_tabelo = []
    for i in range(len(dobri)):
        for j in range(len(objekti[i])):
            if cenee[i][j] != ["nemogoče, nemogoče"]:
                info_za_tabelo.append( [imena[i]] + [naslovi[i]] + [objekti[i][j]] + cenee[i][j] + razdalje[i] + [dobri[i]] )
            
    return info_za_tabelo


def ustvari_podroben_csv(df, stevilo_izbranih, zacetek, konec, brskalnik):
    """Funkcija ustvari tabelo v kateri se nahajaja željeno število sob, ki smo jih imeli na strani."""
    a = natancne_informacije(df, stevilo_izbranih, zacetek, konec, brskalnik)
    ustvarjanje_tabel.create_excel_podrobnejsi(a)
    return ustvarjanje_tabel.ustvari_podrobnejsi_csv(a)


def graf(df):
    """Funkcija ustvari, prikaže in shrani grafe."""
    graficni_prikaz.izrisi_grafe(df)
    