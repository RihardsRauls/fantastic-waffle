"""
Kalkulators ar 4 darbībām
"""

def saskaitisana(a, b):
    return a+b

def atnemsana(a, b):
    return a-b

def reizinasana(a,b):
    return a*b

def kapinasana(a, b):
    return a**b

def dalisana(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "NEVAR DALĪT AR 0 TU AMBĀLI!!!!!!"

def main():
    skaitlis1 = float(input("Skaitlis 1 : "))
    skaitlis2 = float(input("Skaitlis 2 : "))

    print("""
    1 - Samesties
    2 - Atsavināt mantu
    3 - Vairoties
    4 - Mana sieva mani pameta
    """)

    darbs = int(input("Darbība : "))

    print("")

    if darbs == 1:
        print(saskaitisana(skaitlis1, skaitlis2))
    elif darbs == 2:
        print(atnemsana(skaitlis1, skaitlis2))
    elif darbs == 3:
        print(reizinasana(skaitlis1, skaitlis2))
    elif darbs == 4:
        print(dalisana(skaitlis1, skaitlis2))
    else:
        print("Mazāk dzert vajag!")

if __name__ =="__main__":
    main()