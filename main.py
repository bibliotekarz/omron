# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


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
            return str(int(str1[:2]) + 12) + str1[2:8]
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
    f = open('csv/_as BP Report 012220.csv','r')
    dane =f.read()
    dane = dane.split("\n")

    print(dane[2].split(";"))
    print(dane[10].split(";"))

    adane = dane[10].split(",")
    adane = str(adane)
    print("adane ", adane)
    print(type(adane))
    print(adane.split(";"))
    print("godzina : ",dane[10][3])

    print(convert24(dane[10][3]))