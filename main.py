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


# stare_niskie = 0
# stare_tetno = 0
stara_data = 1999
stare_wysokie = 0
def srednia(data_pomiaru, zpomiaru_wysokie, jakies_niskie, jakies_tetno, jakas_data, jakies_wysokie):
    if data_pomiaru == jakas_data:
        print("data się pokrywa", data_pomiaru, " <-- data_pomiaru | stara_data --> ", jakas_data)
        print("zgodna data ",zpomiaru_wysokie," <-- z pomiaru wysokie | stare wysokie --> ", jakies_wysokie)
        # wysokie = (stare_wysokie + jakies_wysokie) / 2
        # niskie = (stare_niskie + jakies_niskie) / 2
        # tetno = (stare_tetno + jakies_tetno) / 2
        # print("usredniony wynik", jakas_data, data_pomiaru, wysokie, niskie, tetno, sep="\t")
        # print("----")
    else:
        print("----- daty są różne", data_pomiaru, " <-- data_pomiaru | stara_data --> ", jakas_data)
        global stara_data
#        print("stara data", stara_data)
        stara_data = data_pomiaru

        global stare_wysokie
        stare_wysokie = zpomiaru_wysokie
        print("---- niezgodna data ",zpomiaru_wysokie," <-- z pomiaru wysokie | stare wysokie --> ", jakies_wysokie)
        # global stare_niskie
        stare_niskie = jakies_niskie
        #
        # global stare_tetno
        stare_tetno = jakies_tetno
        #
    #    print("dodane do stare_wynik", jakas_data, data_pomiaru, stare_wysokie, stare_niskie, stare_tetno, sep="\t")
    #    print("----")
    return


print("poza funkcją stare_wynik",stara_data) #, jakas_data, data_pomiaru, stare_wysokie, stare_niskie, stare_tetno, sep="\t")

f = open('csv/_as BP Report 012220.csv','r')
dane = f.read()
pobrane_dane = dane.split("\n")
    #
    # print(pobrane_dane)
    # d10 = pobrane_dane[3]
    # print("print d10: ",d10)

for dane in pobrane_dane:
#    print(dane)

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


    if pobrana_godzina[1] == ":" :
        godzina = "0" + pobrana_godzina

    data = pobrana_data.split(".")
    miesiac, dzien, rok = data

    if len(miesiac) < 2:
        miesiac = "0" + miesiac
    data_pomiaru = f"{dzien}.{miesiac}.{rok}"
    godzina = timeconvert(godzina)
#    print("data do arkusza: ", data_pomiaru)
#    print("godzina do arkusza:", godzina)

#    print("------------------- ",stara_data, " ================ stara_data")
    srednia(data_pomiaru, wysokie, niskie, tetno, stara_data, stare_wysokie)

