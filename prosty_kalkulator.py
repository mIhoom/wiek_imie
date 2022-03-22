print (" WITAM W PROSTYM KALKULATORZE")
wybór = input ("Wybierz działanie: + dodawanie, - odejmowanie, * mnożenie, / dzielenie i zatrwierdź swój wybór Enterem ")
a = int (input("Podaj pierwszą liczbę :"))
b = int (input("Podaj drugą liczbę :"))
if wybór == '+':
    print ("Wynik dodawania to:")
    print (a + b)
elif wybór == '-':
    print ("Wynik odejmowania to:")
    print (a - b)
elif wybór == '*':
    print ("Wynik mnożenia to:")
    print (a * b)
elif wybór == '/':
    print ("Wynik dzielenia to:")
    if (b == 0):
        print ("Pamiętaj cholero, nie dziel przez zero!!!")
    else: print (a / b)
else:
    print ("Dokonałeś złego wyboru")