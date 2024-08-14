from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import re



def tocni_ceniki(seznam_urljev, pricelist_id, brskalnik='firefox'):
    """Funkcija vrne seznam cenikov, ki so še v surovi (besedilni) obliki."""
    
    brskalniki = {
        'firefox': webdriver.Firefox,
        'edge': webdriver.Edge,
        'chrome': webdriver.Chrome
    }
    pricelist_id = [x[1] for x in pricelist_id]
    if brskalnik.lower() not in brskalniki:
        raise ValueError(f"Brskalnik {brskalnik} ni podprt. Podprti brskalniki so {', '.join(brskalniki.keys())}.")

    driver_class = brskalniki[brskalnik.lower()]
    driver = driver_class()
    cenik_apartmajev = []
    
    for (url, sez_id) in zip(seznam_urljev, pricelist_id):
        driver.get(url)
        cenik_apartmaja = []
        
        for id in sez_id:
            funkcija_klic = f"showPricelist({id}, 'reg', 'apartments', null);"
            driver.execute_script(funkcija_klic)
            try:
                WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.ID, f'mod-unit-prc-content{id}'))
                )
                div_element = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.ID, f'mod-unit-prc-content{id}'))
                )
                WebDriverWait(driver, 10).until(
                    lambda driver: driver.find_element(By.ID, f'mod-unit-prc-content{id}').text.strip() != ""
                )
                cenik = div_element.find_element(By.CLASS_NAME, 'property_pricelist')
                cenik_apartmaja.append(cenik.get_attribute('outerHTML'))    
            except Exception as e:
                print(f"Napaka pri iskanju cenika za ID {id}: {e}")
                cenik_apartmaja.append(f"Napaka pri iskanju cenika")
            
        cenik_apartmajev.append(cenik_apartmaja)
        
    driver.quit()
    return cenik_apartmajev


def izlusci_cenik(cenik_apartmajev):
    """ Funkcija prejme seznam seznamov, vrne seznam ponudnikov, kjer ima ponudnik podsezname: 
        stanovanja, ta pa imajo za podsezname cenik. """
        
    vzorec = r'<span>(\d{2}\.\d{2}-\d{2}\.\d{2})</span><span>(\d+|-)</span><span>€(\d+)</span>'
    izluscen_apartmajev = []
    
    for cenik_apartmaja in cenik_apartmajev:
        izluscen_apartmaja = []
        for cenik in cenik_apartmaja:
            ujemanja = re.findall(vzorec, "".join(cenik.split()))
            izluscen_cenik = [[datum, cena] for datum, nic, cena in ujemanja]
            izluscen_apartmaja.append(izluscen_cenik)
        izluscen_apartmajev.append(izluscen_apartmaja)    
        
    return izluscen_apartmajev


def nastavi_datum(date_str):
    """Pretvori niz datuma v objekt datetime."""
    
    day, month = map(int, date_str.split('.'))
    return datetime(datetime.now().year, month, day)


def izracuna_ceno(cenik, datum):
    """Izračuna strošek za določen datum glede na cenik."""
    
    # Pretvori datum v format datetime
    datum_zacetek, datum_konec = datum.split('-')
    datum_zacetek = nastavi_datum(datum_zacetek)
    datum_konec = nastavi_datum(datum_konec)
    
    skupna_cena = 0
    pokriti_datumi = []

    for interval in cenik:
        interval_zacetek, interval_konec = interval[0].split('-')
        interval_zacetek = nastavi_datum(interval_zacetek)
        interval_konec = nastavi_datum(interval_konec)
        dnevna_cena = float(interval[1])

        # Prekrivni interval
        overlap_start = max(datum_zacetek, interval_zacetek)
        overlap_end = min(datum_konec, interval_konec)

        #ali obstaja prekrivni interval
        if overlap_start <= overlap_end:
            days_in_overlap = (overlap_end - overlap_start).days + 1
            skupna_cena += days_in_overlap * dnevna_cena
            pokriti_datumi.append((overlap_start, overlap_end))

    # Preveri, ali so vsi dnevi v izbranem datumu pokriti
    trenutni_datum = datum_zacetek
    while trenutni_datum <= datum_konec:
        if not any(zacetek <= trenutni_datum <= konec for zacetek, konec in pokriti_datumi):
            return ["nemogoče, nemogoče"]
        trenutni_datum += timedelta(days=1)
    
    return skupna_cena


def prestej_dni(datum):
    """Izračuna število dni v danem obdobju."""
    
    datum_zacetek, datum_konec = datum.split('-')
    datum_zacetek = nastavi_datum(datum_zacetek)
    datum_konec = nastavi_datum(datum_konec)
    dnevi = (datum_konec - datum_zacetek).days + 1
    return dnevi


def cena_skupaj_in_na_noc(cenik, datum):
    """Funkcija glede na cenik in datum izračuna skupno ceno in ceno na noč."""
    
    a = izracuna_ceno(cenik, datum)
    if a == ["nemogoče, nemogoče"]:
        return a
    return [round(a, 2), round(a/prestej_dni(datum), 2)]
