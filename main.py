
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

    f = open('csv/_as BP Report 012220.csv','r')
    dane = f.read()
    pobrane_dane = dane.split("\n")
    d10 = pobrane_dane[83]
    d10 = d10.split(";")
    pobrana_data, pobrana_godzina, wysokie, niskie, tetno = d10[:5]

    if pobrana_godzina[1] == ":" :
        godzina = "0" + pobrana_godzina

    data = pobrana_data.split(".")
    miesiac, dzien, rok = data

    if len(miesiac) < 2:
        miesiac = "0" + miesiac

    data = f"{dzien}.{miesiac}.{rok}"
    godzina = timeconvert(godzina)
    print("data do arkusza: ", data)
    print("godzina do arkusza:", godzina)
