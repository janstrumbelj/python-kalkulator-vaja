def sestej(a, b):
    return f"\nVsota izračuna števil {a} + {b} = {a + b}"

def odstej(a, b):
    return f"\nRazlika izračuna števil {a} - {b} = {a - b}"

def pomnozi(a,b):
    return f"\nProdukt izračuna števil {a} * {b} = {a * b}"

def deli(a,b):
    try:
        a / b
    except ZeroDivisionError:
        return "\nDrugo število ne sme biti 0"    
    else:
        return f"\nKoličnik izračuna števil {a} : {b} = {a / b}"

while True:

    print("\nPozdrav! Mini kalkulator")
    print("1 = seštevanje")
    print("2 = odštevanje")
    print("3 = množenje")
    print("4 = deljenje")
    print("0 = izhod")

    izbira = input("Kaj želiš narediti? (0-4): ")

    if izbira == "1":
        x = float(input("Prvo število: "))
        y = float(input("Drugo število: "))
        print(sestej(x, y))
    elif izbira == "2":
        x = float(input("Prvo število: "))
        y = float(input("Drugo število: "))
        print(odstej(x, y))
    elif izbira == "3":
        x = float(input("Prvo število: "))
        y = float(input("Drugo število: "))
        print(pomnozi(x, y))
    elif izbira == "4":
        x = float(input("Prvo število: "))
        y = float(input("Drugo število: "))
        print(deli(x, y))
    elif izbira == "0":
        print("\nUspešno ste zapustili meni.\n")
        break
    else:
        print("\nNeveljavna izbira!")