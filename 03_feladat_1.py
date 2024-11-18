"""1.1 Feladat
Készíts egy programot, amely a felhasználó által megadott mondatról a mondatvégi 
jel alapján eldönti milyen fajtájú! (kijelentő, kérdő, felkiáltó / felszólító / óhatjtó)
"""
megadott_mondat = input("Kérlek adj meg egy mondatot: ")

if megadott_mondat[-1] == ".":
    print("Ez a mondat egy kijelentő mondat")
elif megadott_mondat[-1] == "?":
    print("Ez a mondat egy kérdő mondat.")
elif megadott_mondat[-1] == "!":
    print("Ez a mondat egy felkiáltó / felszólító / óhatjtó mondat")
else:
    print("Nem írtál mondatvégi írásjelet.")