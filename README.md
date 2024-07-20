IDEJA:
Spletna stran apartmanija.hr ima mnogokrat na voljo dobre apartmaje. Kar me zmoti je to, da imajo kot ceno, ki predstavlja apartma, napisano najnižjo ceno, ki jo postavljajo, na primer neko ceno za zimsko sezono za njihovo najmanjšo sobo. Točne cene si lahko ogledamo le tako, da zapravimo svoj čas. Program, ki sem ga napisal, poišče in izračuna cene, poišče različne razdalje, izloči tiste, ki na želen termin niso v najem in še več



POTREBUJETE NASLEDNJE KNJIŽNICE:
(1.)
beautifulsoup4
pandas
(2.)
selenium
(3.)
seaborn
matplotlib
(4.)
openpyxl
Za delne rezultate potrebujete vsaj (1.), če imate še (2.) dobite podrobnejšo analizo v csv obliki, (3.) je potrebna za izris grafov, (4.) pa ustvari excel tabelo. Podrobnejše podatke o paketih dobite na datoteki requirements.txt.




NAVODILA ZA UPORABO:
Odprite .ipynb datoteko. 

1. DEL:

Stran apartmanija.hr ima url-je oblik:

(1):  https://www.apartmanija.hr/apartmani/{glavni_naslov}
(2):  https://www.apartmanija.hr/pretraga/apartmani/r:{okolica}+c:{kraj}+osobe:{osebe}+start:{prihod}+end:{odhod}

Nastavite parametre glede na tip želenega url-ja:
 
(1):  Nastavite {prihod, odhod, glavni_naslov}, vrednosti {osebe, okolica, kraj} ne spreminjajte, za {i} pa nastavite vrednost True.
(2):  Nastavite {prihod, odhod, osebe, okolica, kraj}, vrednosti {glavni_naslov} ne spreminjajte, za {i} pa nastavite vrednost False.

Pozor: datuma naj bosta oblike kot "01.08.2024"


2.DEL:	

V naslednji celici nastavite še {podrobna_analiza} na stevilsko vrednost, ki predstavlja število apartmajev, ki jih želimo pogledati podrobneje.
Prav tako nastavite {brskalnik} na ime brskalnika, ki ga uporabljate.


3.DEL:

Zdaj lahko mirno zaženete vse celice, rezultati pa se bodo shranili v mapo grafi_in_tabele. Opomba: potreben čas je močno odvisen od spremenljivke {podrobna_analiza} in internetne povezave. Za vrednost {podrobna_analiza=132} mi je vzelo nekaj manj kot 6 minut, našlo pa mi je 396 sob.

