
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    def convert24(str1):
        # Checking if last two elements of time
        # is AM and first two elements are 12
        if str1[-2:] == "AM" and str1[:2] == "12":
            return "00" + str1[2:-2]

            # remove the AM
        elif str1[-2:] == "AM":
            return str1[:-2]

            # Checking if last two elements of time
        # is PM and first two elements are 12
        elif str1[-2:] == "PM" and str1[:2] == "12":
            return str1[:-2]

        else:

            # add 12 to hours and remove PM
            if str1[2] == ":":
                print("ma dwukropek ")
                return str(int(str1[:1]) + 12) + str1[2:8]
            else:
                print("niema dwukropek ")
                return str(int(str1[:2]) + 12) + str1[2:8]

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/


    f = open('csv/_as BP Report 012220.csv','r')
    dane =f.read()
    dane = dane.split("\n")

    print(dane[2].split(";"))

    d10 =dane[10]
    print("d10", d10, "\n")
    print("type d10", type(d10), "\n")
    d11 = d10.split(";")
    print(" d11 :", d11, "\n")
    data, godzina, wysokie, niskie, tetno = d11[:5]

    print(data, godzina, wysokie, niskie, tetno, sep="\n")

    print("godzina[1]" , godzina[1])
    print("type godzina", type(godzina))

    if godzina[1] == ":" :
        godzina = "0" + godzina
        print("godzina 0 :" + godzina)

    print("poifie")
    d12 = "1:12:15 PM"

    def timeconvert(str1):
        if str1[-2:] == "AM" and str1[:2] == "12":
            return "00" + str1[2:-2]
        elif str1[-2:] == "AM":
            return str1[:-2]
        elif str1[-2:] == "PM" and str1[:2] == "12":
            return str1[:-2]
        else:
            return str(int(str1[:2]) + 12) + str1[2:8]

    print("godzina po konwersji :", timeconvert(godzina))
