print("""
1) dodawanie
2) odejmowanie
3) mnożenie
4) dzielenie
5) potęgowanie
""")
C=int(input("wybierz numer operacji: "))
try:
    a=float(input("podaj a "))
except:
    print("zostala podana wartosc ktora nie jest liczba")
    exit()
try:
    b=float(input("podaj b "))
except:
    print("zostala podana wartosc ktora nie jest liczba")
    exit()
if C==1:
    print("wynik wynosi", a+b)
elif C==2:
    print("wynik wynosi", a-b)
elif C==3:
    print("wynik wynosi", a * b)
elif C==4:
    if b==0:
        print("nie mozna dzielic przez 0")
        exit()
    print("wynik wynosi", a / b)
elif C==5:
    print("wynik wynosi", a ** b)
else:
    print("brak operacji")

