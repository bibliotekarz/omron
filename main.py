import re


def timeconvert(str1):
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]
    elif str1[-2:] == "AM":
        return str1[:-2]
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]
    else:
        return str(int(str1[:2]) + 12) + str1[2:8]


stare_niskie = 0
stare_tetno = 0
stara_data = 0
stare_wysokie = 0

def robi_stare(data_pomiaru, wysokie, niskie, tetno):
    stara_data = data_pomiaru
    stare_wysokie = wysokie
    stare_niskie = niskie
    stare_tetno = tetno
    return stara_data, stare_wysokie, stare_niskie, stare_tetno

def popraw_date(dane, pobrana_data):

    data = pobrana_data.split(".")
    miesiac, dzien, rok = data

    if len(miesiac) < 2:
        miesiac = "0" + miesiac
    data_pomiaru = f"{dzien}.{miesiac}.{rok}"
    return data_pomiaru


def popraw_godzine(pobrana_godzina):
    if pobrana_godzina[1] == ":":
        godzina0 = "0" + pobrana_godzina
        godzina = timeconvert(godzina0)
    else:
        godzina = timeconvert(pobrana_godzina)
    return godzina

def wylicz_srednia(stara_data, nowa_data, stary_parametr, nowy_parametr):
    if stara_data == nowa_data:
        parametr = (int(stary_parametr) + int(nowy_parametr)) / 2
    else:
        parametr = int(nowy_parametr)
    return parametr

# :TODO: zrobić średnią niezależna od liczby pomiarów
# f = open('csv/as.csv','r')
f = open('csv/_as BP Report 012220.csv','r')
wszystkie_dane = f.read()
pobrane_dane = wszystkie_dane.split("\n")
poprawiona_data = 0
wysokie = 0
niskie = 0
tetno = 0

for dane in pobrane_dane:

    stare = robi_stare(poprawiona_data, wysokie, niskie, tetno)

    if dane == "":
        print("awaria puste")
        continue

    re0 = "\d"
    test_na_cyfre = re.match(re0, dane[0])
    if test_na_cyfre == None :
        print("to nie cyfra")
        continue

    dane = dane.split(";")
    pobrana_data, pobrana_godzina, wysokie, niskie, tetno = dane[:5]
    print("wadliwa data", pobrana_data, "wadliwa godzina ", "w"+pobrana_godzina+"w", type(pobrana_godzina))
    poprawiona_data = popraw_date(dane[0], pobrana_data)
    poprawiona_godzina = popraw_godzine(pobrana_godzina)
    print("poprawiona godzina", poprawiona_godzina)

    nowe = (poprawiona_data, wysokie, niskie, tetno)
    print("-----")

    print(nowe[0], "wysokie ", wylicz_srednia(stare[0], nowe[0], stare[1], nowe[1]), "s"+str(stare[1]), "n"+str(nowe[1]))
    print(nowe[0], "niskie ", wylicz_srednia(stare[0], nowe[0], stare[2], nowe[2]), "s"+str(stare[2]), "n"+str(nowe[2]))
    print(nowe[0], "tetno ", wylicz_srednia(stare[0], nowe[0], stare[3], nowe[3]), "s"+str(stare[3]), "n"+str(nowe[3]))
