# README

## IDEJA:
Spletna stran apartmanija.hr pogosto nudi odlične apartmaje, vendar pogosto prikažejo samo najnižjo ceno, ki se običajno nanaša na zimsko sezono za najmanjše sobe. Da bi ugotovili točne cene, je potrebno vložiti čas in trud. Program, ki sem ga razvil, poišče vse enote apartmajev, jih grobo uredi po cenah in ustvari tabelo v csv in xlsx formatu. Nato vzame izbrano število teh enot, preuči vse ponujene sobe, preračuna cene glede na izbrana datuma, izloči tiste, ki v izbranem terminu niso v oddaji, zbere tocne naslove in razdalje do morja, trgovin, restavracij in več. Zadnji del kode ustvari še tabele in grafe in jih doda v enako datoteko kot prej, in sicer datoteko z imenom grafi_in_tabele.


## NAVODILA ZA ZAGON:
1. Namestite naslednje knjižnice:
   - `beautifulsoup4`
   - `pandas`
   - `selenium`
   - `seaborn`
   - `matplotlib`
   - `openpyxl`
   
2. Odprite datoteko z razširitvijo `.ipynb` (Jupyter Notebook).

3. Nastavite parametre glede na vrsto URL-ja, ki ga želite analizirati:

   **URL-ji so v dveh oblikah:**
   - _1_ : `https://www.apartmanija.hr/apartmani/{glavni_naslov}`
   - _2_ : `https://www.apartmanija.hr/pretraga/apartmani/r:{okolica}+c:{kraj}+osobe:{osebe}+start:{prihod}+end:{odhod}`

   **Nastavitve parametrov glede na vrsto URL-ja:**
   - Za URL oblike _1_ :
     - Nastavite `{prihod}`, `{odhod}`, `{glavni_naslov}`.
     - Vrednosti `{osebe}`, `{okolica}`, `{kraj}` pustite nespremenjene.
     - Nastavite `{i}` na `True`.
     
   - Za URL oblike _2_ :
     - Nastavite `{prihod}`, `{odhod}`, `{osebe}`, `{okolica}`, `{kraj}`.
     - Vrednost `{glavni_naslov}` pustite nespremenjeno.
     - Nastavite `{i}` na `False`.

   **Pozor:** Datumi naj bodo v formatu "01.08.2024".

4. V naslednji celici nastavite `{podrobna_analiza}` na številsko vrednost, ki predstavlja število apartmajev, ki jih želite podrobno pregledati. Prav tako nastavite `{brskalnik}` na ime brskalnika, ki ga uporabljate.

5. Ko so vsi parametri nastavljeni, lahko zaženete vse celice. Rezultati bodo shranjeni v mapo `grafi_in_tabele`. Upoštevajte, da je potreben čas za izvedbo zelo odvisen od vrednosti `{podrobna_analiza}` in hitrosti internetne povezave.

## PRIMER PRIDOBLJENIH PODATKOV:
V mapi primer_pridobljenih_podatkov se nahaja primer podatkov, ki jih je koda sposobna pridobiti. V mapi najdete tudi tekstovno datoteko, ki opisuje parametre, ki so bili uporabljeni.
