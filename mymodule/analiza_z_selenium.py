from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

#Stran vsebuje gumbe z podrobnejšimi cenami, koda vrne njihove podatke, v html obliki
#Če funkcija javi težavo, je možna rešitev to da povečaš time.sleep()
def tocni_ceniki(seznam_urljev, pricelist_id, brskalnik='firefox'):
    
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
                
                #Ta delček kode počaka, da se vsebina znotraj div_elementa naloži. Nadomesti time.sleep()
                WebDriverWait(driver, 10).until(
                    lambda driver: driver.find_element(By.ID, f'mod-unit-prc-content{id}').text.strip() != ""
                )
                
                #time.sleep(1)
                cenik = div_element.find_element(By.CLASS_NAME, 'property_pricelist')
                cenik_apartmaja.append(cenik.get_attribute('outerHTML'))
                
            except Exception as e:
                print(f"Napaka pri iskanju cenika za ID {id}: {e}")
                cenik_apartmaja.append(f"Napaka pri iskanju cenika")
            
        cenik_apartmajev.append(cenik_apartmaja)
        
    driver.quit()
    
    return cenik_apartmajev










#prejme seznam seznamov, vrne seznam ponudnikov, kjer ima ponudnik podsezname: stanovanja, 
#ta pa imajo koncno za podsezname cenik

def izlusci_cenik(cenik_apartmajev):
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







from datetime import datetime, timedelta


def parse_date(date_str):
    """Pretvori niz datuma v objekt datetime."""
    day, month = map(int, date_str.split('.'))
    return datetime(datetime.now().year, month, day)

#Če datum ni mogoč, vrne [100000, 100000]
def calculate_cost(cenik, datum):
    """Izračuna strošek za določen datum glede na cenik."""
    
    # Pretvori datum v format datetime
    datum_start, datum_end = datum.split('-')
    datum_start = parse_date(datum_start)
    datum_end = parse_date(datum_end)

    # Inicializiraj strošek
    total_cost = 0
    covered_dates = []

    # Poglej vsak interval v ceniku
    for interval in cenik:
        interval_start, interval_end = interval[0].split('-')
        interval_start = parse_date(interval_start)
        interval_end = parse_date(interval_end)
        daily_cost = float(interval[1])

        # Izračunaj prekrivni interval
        overlap_start = max(datum_start, interval_start)
        overlap_end = min(datum_end, interval_end)

        # Preveri, ali obstaja prekrivni interval
        if overlap_start <= overlap_end:
            # Število dni v prekrivnem intervalu
            days_in_overlap = (overlap_end - overlap_start).days + 1
            total_cost += days_in_overlap * daily_cost
            covered_dates.append((overlap_start, overlap_end))

    # Preveri, ali so vsi dnevi v izbranem datumu pokriti
    current_date = datum_start
    while current_date <= datum_end:
        if not any(start <= current_date <= end for start, end in covered_dates):
            return ["nemogoče, nemogoče"]
        current_date += timedelta(days=1)
    
    return total_cost



def count_days(datum):
    """Izračuna število dni v danem obdobju."""
    datum_start, datum_end = datum.split('-')
    datum_start = parse_date(datum_start)
    datum_end = parse_date(datum_end)

    # Izračunaj število dni v obdobju
    days_count = (datum_end - datum_start).days + 1  # +1 vključuje zadnji dan

    return days_count


def cena_skupaj_in_na_noc(cenik, datum):
    a = calculate_cost(cenik, datum)
    if a == ["nemogoče, nemogoče"]:
        return a
    return [round(a, 2), round(a/count_days(datum), 2)]







