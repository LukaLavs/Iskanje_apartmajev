import pandas as pd
import os



#Koda ustvari csv datoteko v mapi shranjevanje_strani
#vrne pa df, ki je oblike DataFrame
def create_csv(sez):
    df = pd.DataFrame(sez, columns=["Ime", "Cena", "Kapaciteta", "Povezava"])
    df = df.sort_values(by="Cena")
    
    podmapa = 'grafi_in_tabele'
    file_name = 'apartmaji_v_izbrani_okolici.csv'

    if not os.path.exists(podmapa):
        os.makedirs(podmapa)

    file_path = os.path.join(podmapa, file_name)
    df.to_csv(file_path, index=False, sep=',', encoding='utf-8-sig')

    return df



#Koda ustvari excel datoteko, saj so v njej podatki preglednejši kot v csv
def create_excel(sez):
    # Pretvorimo seznam v DataFrame
    df = pd.DataFrame(sez, columns=["Ime", "Cena", "Kapaciteta", "Povezava"])
    df = df.sort_values(by="Cena")
    df['Kapaciteta'] = df['Kapaciteta'].apply(lambda x: f"{x[0]} - {x[1]}" if isinstance(x, list) else x)
    
    podmapa = 'grafi_in_tabele'
    file_name = 'apartmaji_v_izbrani_okolici.xlsx'

    if not os.path.exists(podmapa):
        os.makedirs(podmapa)

    file_path = os.path.join(podmapa, file_name)

    #Ta del kode, prepreči ustvarjanje excel dokumenta, če openpyxl ni nameščen
    try:
        df.to_excel(file_path, index=False)
    except ModuleNotFoundError as e:
        if "openpyxl" in str(e):
            print("Module 'openpyxl' not found. Please install it to create Excel files.")
        else:
            raise e
    

    
#Koda razvrsti oglase od najcenejšega do najdražjega, in vrne n povezav do n najcenejših
def povezave_do_izbranih(df, n=3):
    if n < 1:
        print("Za podrobnejšo analizo potrebujemo vsaj 1 apartma")
        return None
    
    if n > df.shape[0]:
        print(f"Imamo le {df.shape[0]} kandidatov")
        return None
    
    #izberimo n najcenejših ponudb in [[imen], [povezav]] za njih
    return [[df.iloc[i, 0] for i in range(n)]] + [[df.iloc[i, 3] for i in range(n)]]



#Funkcija iz seznama ustvari DataFrame in podatke zapiše v csv
def ustvari_podrobnejsi_csv(sez):
    stolpci = ["Ime","Naslov", "Soba", "Skupna cena", "Cena na noč", "Morje", "Plaža", "Center", "Trgovina", "Restavracija", "Povezava"]
    df = pd.DataFrame(sez, columns=stolpci)
    df = df.sort_values(by=["Soba","Cena na noč", "Plaža"])
    
    podmapa = 'grafi_in_tabele'
    file_name = 'csv_podrobnejsi_podatki.csv'

    if not os.path.exists(podmapa):
        os.makedirs(podmapa)

    file_path = os.path.join(podmapa, file_name)
    df.to_csv(file_path, index=False)

    return df



def create_excel_podrobnejsi(sez):
    stolpci = ["Ime","Naslov", "Soba", "Skupna cena", "Cena na noč", "Morje", "Plaža", "Center", "Trgovina", "Restavracija", "Povezava"]
    df = pd.DataFrame(sez, columns=stolpci)
    df = df.sort_values(by=["Soba","Cena na noč", "Plaža"])
    
    podmapa = 'grafi_in_tabele'
    file_name = 'excel_apartmaji_v_izbrani_okolici.xlsx'

    if not os.path.exists(podmapa):
        os.makedirs(podmapa)

    file_path = os.path.join(podmapa, file_name)

    #Ta del kode, prepreči ustvarjanje excel dokumenta, če openpyxl ni nameščen
    try:
        df.to_excel(file_path, index=False)
    except ModuleNotFoundError as e:
        if "openpyxl" in str(e):
            print("Modul 'openpyxl' ni najden. Naloži z komando: pip install openpyxl")
        else:
            raise e
    
