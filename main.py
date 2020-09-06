import csv
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

def robi_stare(data_pomiaru, wysokie, niskie, tetno):
    stara_data = data_pomiaru
    stare_wysokie = wysokie
    stare_niskie = niskie
    stare_tetno = tetno
    return stara_data, stare_wysokie, stare_niskie, stare_tetno

def robi_bardzo_stare(stara_data, stare_wysokie, stare_niskie, stare_tetno):
    bardzo_stara_data = stara_data
    bardzo_stare_wysokie = stare_wysokie
    bardzo_stare_niskie = stare_niskie
    bardzo_stare_tetno = stare_tetno
    return bardzo_stara_data, bardzo_stare_wysokie, bardzo_stare_niskie, bardzo_stare_tetno

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

licznik = 1
bardzo_stary_parametr = 0
def wylicz_srednia(bardzo_stary_parametr, stara_data, nowa_data, stary_parametr, nowy_parametr, licznik):
    licznik0 = licznik
    if stara_data == nowa_data:
        licznik0 += 1
        if licznik0 < 3:
            parametr = (int(stary_parametr) + int(nowy_parametr)) / licznik0
        elif licznik0 > 2:
            parametr = (int(bardzo_stary_parametr) + int(stary_parametr) + int(nowy_parametr)) / licznik0

        licznik = licznik0
    else:
        parametr = int(nowy_parametr)
        licznik = 1

    return parametr, licznik

pomiar_wszystkie = [['01.01.2000', 0, 0, 0, 0]]
def wybierz_pomiar():

     pomiar_stary = pomiar_wszystkie[-1]
     pomiar_aktualny = [poprawiona_data, int(wys), int(nis), int(tet), licznik]
     pomiar_jeden = ['01.01.1010', 0, 0, 0, 0]

     while pomiar_stary[0] == pomiar_aktualny[0]:
        if pomiar_aktualny[-1] == 3:
            pomiar_jeden = pomiar_aktualny
            pomiar_wszystkie[-1] = pomiar_jeden[0:-1]
            break
        else:
            if pomiar_aktualny[-1] == 2:
                pomiar_jeden = pomiar_aktualny
                pomiar_wszystkie[-1] = pomiar_jeden[0:-1]
                break
            else:
                if pomiar_aktualny[-1] == 1:
                    pomiar_jeden = pomiar_aktualny
                    pomiar_wszystkie[-1] = pomiar_jeden[0:-1]
                    break
                else:
                    break

        pomiar_wszystkie.append(pomiar_jeden[0:-1])
        continue

     else:
        pomiar_wszystkie.append(pomiar_aktualny[0:-1])

f = open('csv/sample.csv','r')
wszystkie_dane = f.read()
pobrane_dane = wszystkie_dane.split("\n")
poprawiona_data = 0
wysokie = 0
niskie = 0
tetno = 0
bardzo_stare = (123, 123, 123, 123)

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
    poprawiona_data = popraw_date(dane[0], pobrana_data)
    poprawiona_godzina = popraw_godzine(pobrana_godzina)

    nowe = (poprawiona_data, wysokie, niskie, tetno)

    wys = wylicz_srednia(bardzo_stare[1], stare[0], nowe[0], stare[1], nowe[1], licznik)[0]
    nis = wylicz_srednia(bardzo_stare[2], stare[0], nowe[0], stare[2], nowe[2], licznik)[0]
    tet = wylicz_srednia(bardzo_stare[3], stare[0], nowe[0], stare[3], nowe[3], licznik)[0]
    licznik = wylicz_srednia(bardzo_stare[1], stare[0], nowe[0], stare[1], nowe[1], licznik)[1]

    bardzo_stare = robi_bardzo_stare(stare[0], stare[1], stare[2], stare[3])
    wybierz_pomiar()

pomiar_wszystkie.pop(0)

with open("csv/wynik.csv", 'w', newline='') as f:
    wri = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC, delimiter=';', lineterminator=';\n')
    wri.writerows(pomiar_wszystkie)
