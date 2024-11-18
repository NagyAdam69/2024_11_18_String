"""1.2 Feladat
Az előbbi programot módosítsd úgy, hogy újabb és újabb mondatot kérjen be a program 
(amig a felhasználó csak egy ENTER-t nem üt), majd állapítsa meg, és írja ki mineden egyes alkalommal a mondat fajtáját!"""

while True:
    megadott_mondat = input("Kérlek adj meg egy mondatot: ")
    if megadott_mondat == "":
        print("Program vége")
        break
    elif megadott_mondat[-1] == ".":
        print("Ez a mondat egy kijelentő mondat")
    elif megadott_mondat[-1] == "?":
        print("Ez a mondat egy kérdő mondat.")
    elif megadott_mondat[-1] == "!":
        print("Ez a mondat egy felkiáltó / felszólító / óhatjtó mondat")
    
    else:
        print("Nem írtál mondatvégi írásjelet.")