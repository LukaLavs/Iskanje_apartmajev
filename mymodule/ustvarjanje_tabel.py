import pandas as pd
import os



def nastavi_directory():
    """Funkcija ustvari grafi_in_tabele in vrne njeno lokacijo"""
    pot_do_skripte = os.path.abspath(__file__)
    pot_do_nadmape = os.path.dirname(os.path.dirname(pot_do_skripte))
    tarca = os.path.join(pot_do_nadmape, 'grafi_in_tabele')
    
    if not os.path.exists(tarca):
        os.makedirs(tarca)
  
    return tarca


def create_csv(sez):
    """Koda ustvari csv datoteko v mapi grafi_in_tabele in vrne df."""
    df = pd.DataFrame(sez, columns=["Ime", "Cena", "Kapaciteta", "Povezava"])
    df = df.sort_values(by="Cena")
    
    nastavi_directory()
    file_name = 'apartmaji_v_izbrani_okolici.csv'
    directory = nastavi_directory()
    tarca = os.path.join(directory, file_name)

    df.to_csv(tarca, index=False, sep=',', encoding='utf-8-sig')
    return df


def create_excel(sez):
    """Koda ustvari excel datoteko, saj so v njej podatki preglednejši kot v csv."""
    df = pd.DataFrame(sez, columns=["Ime", "Cena", "Kapaciteta", "Povezava"])
    df = df.sort_values(by="Cena")
    df['Kapaciteta'] = df['Kapaciteta'].apply(lambda x: f"{x[0]} - {x[1]}" if isinstance(x, list) else x)
    
    file_name = 'apartmaji_v_izbrani_okolici.xlsx'
    directory = nastavi_directory()
    tarca = os.path.join(directory, file_name)

    #Ta del kode, prepreči ustvarjanje excel dokumenta, če openpyxl ni nameščen
    try:
        df.to_excel(tarca, index=False)
    except ModuleNotFoundError as e:
        if "openpyxl" in str(e):
            print("Module 'openpyxl' not found. Please install it to create Excel files.")
        else:
            raise e
    

def povezave_do_izbranih(df, n=3):
    """Funkcija razvrsti oglase od najcenejšega do najdražjega, in vrne n povezav do n najcenejših."""
    if n < 1:
        print("Za podrobnejšo analizo potrebujemo vsaj 1 apartma")
        return None
    if n > df.shape[0]:
        print(f"Imamo le {df.shape[0]} kandidatov")
        return None
    
    #izberimo n najcenejših ponudb in [[imen], [povezav]] za njih
    return [[df.iloc[i, 0] for i in range(n)]] + [[df.iloc[i, 3] for i in range(n)]]


def ustvari_podrobnejsi_csv(sez):
    """Funkcija ustvari csv datoteko z podatki o sobah."""
    stolpci = ["Ime","Naslov", "Soba", "Skupna cena", "Cena na noč", "Morje", "Plaža", "Center", "Trgovina", "Restavracija", "Povezava"]
    df = pd.DataFrame(sez, columns=stolpci)
    df = df.sort_values(by=["Soba","Cena na noč", "Plaža"])
    
    file_name = 'csv_podrobnejsi_podatki.csv'
    directory = nastavi_directory()
    file_path = os.path.join(directory, file_name)

    df.to_csv(file_path, index=False)
    return df


def create_excel_podrobnejsi(sez):
    """Funkcija ustvari excel datoteko z podatki o sobah."""
    stolpci = ["Ime","Naslov", "Soba", "Skupna cena", "Cena na noč", "Morje", "Plaža", "Center", "Trgovina", "Restavracija", "Povezava"]
    df = pd.DataFrame(sez, columns=stolpci)
    df = df.sort_values(by=["Soba","Cena na noč", "Plaža"])

    file_name = 'excel_podrobnejsi_podatki.xlsx'
    directory = nastavi_directory()
    file_path = os.path.join(directory, file_name)
    
    try:
        df.to_excel(file_path, index=False)
    except ModuleNotFoundError as e:
        if "openpyxl" in str(e):
            print("Modul 'openpyxl' ni najden. Naloži z komando: pip install openpyxl")
        else:
            raise e
    
