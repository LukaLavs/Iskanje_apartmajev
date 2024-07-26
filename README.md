##IDEJA:
Spletna stran apartmanija.hr ima mnogokrat na voljo dobre apartmaje. Kar me zmoti je to, da imajo kot ceno, ki predstavlja apartma, napisano najnižjo ceno, ki jo postavljajo, na primer neko ceno za zimsko sezono za njihovo najmanjšo sobo. Točne cene si lahko ogledamo le tako, da zapravimo svoj čas. Program, ki sem ga napisal, poišče in izračuna cene, poišče različne razdalje, izloči tiste, ki na želen termin niso v najem in še več



##NAVODILA ZA ZAGON:
1. namestite naslednje knjižnice: beautifulsoup4, pandas, selenium, seaborn, matplotlib, openpyxl.
2. Odprite .ipynb datoteko.
3. Nastavite parametre na željeno vrednost po naslednjih navodilih:
 
Stran apartmanija.hr ima url-je oblik:

(1):  https://www.apartmanija.hr/apartmani/{glavni_naslov}

(2):  https://www.apartmanija.hr/pretraga/apartmani/r:{okolica}+c:{kraj}+osobe:{osebe}+start:{prihod}+end:{odhod}

Nastavite parametre glede na tip želenega url-ja:
 
(1):  Nastavite {prihod, odhod, glavni_naslov}, vrednosti {osebe, okolica, kraj} ne spreminjajte, za {i} pa nastavite vrednost True.

(2):  Nastavite {prihod, odhod, osebe, okolica, kraj}, vrednosti {glavni_naslov} ne spreminjajte, za {i} pa nastavite vrednost False.

Pozor: datuma naj bosta oblike kot "01.08.2024"


V naslednji celici nastavite še {podrobna_analiza} na stevilsko vrednost, ki predstavlja število apartmajev, ki jih želimo pogledati podrobneje.
Prav tako nastavite {brskalnik} na ime brskalnika, ki ga uporabljate.


4.
Zdaj lahko mirno zaženete vse celice, rezultati pa se bodo shranili v mapo grafi_in_tabele. Opomba: potreben čas je močno odvisen od spremenljivke {podrobna_analiza} in internetne povezave. Za vrednost {podrobna_analiza=132} mi je vzelo nekaj manj kot 6 minut, našlo pa mi je 396 sob.

