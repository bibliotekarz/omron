import re
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    def timeconvert(str1):
        if str1[-2:] == "AM" and str1[:2] == "12":
            return "00" + str1[2:-2]
        elif str1[-2:] == "AM":
            return str1[:-2]
        elif str1[-2:] == "PM" and str1[:2] == "12":
            return str1[:-2]
        else:
            return str(int(str1[:2]) + 12) + str1[2:8]


    stara_data = 1999
    def srednia(data_pomiaru, wysokie, niskie, tetno, stara_data):

     #   stara_data = 1999
        stare_wysokie = 0
        stare_niskie = 0
        stare_tetno = 0
        if data_pomiaru == stara_data:
            wysokie = (stare_wysokie + wysokie) / 2
            niskie = (stare_niskie + niskie) / 2
            tetno = (stare_tetno + tetno) / 2
            print("usredniony wynik", stara_data, data_pomiaru, wysokie, niskie, tetno, sep="\t")
            print("----")
        else:
            stara_data = data_pomiaru
            stare_wysokie = wysokie
            stare_niskie = niskie
            stare_tetno = tetno
            print("dodane do stare_wynik", stara_data, data_pomiaru, stare_wysokie, stare_niskie, stare_tetno, sep="\t")
            print("----")
        return stara_data

    f = open('csv/_as BP Report 012220.csv','r')
    dane = f.read()
    pobrane_dane = dane.split("\n")
    #
    # print(pobrane_dane)
    # d10 = pobrane_dane[3]
    # print("print d10: ",d10)

    for dane in pobrane_dane:
        print(dane)

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
        print("data do arkusza: ", data_pomiaru)
        print("godzina do arkusza:", godzina)
        srednia(data_pomiaru, int(wysokie), int(niskie),int(tetno), stara_data)

