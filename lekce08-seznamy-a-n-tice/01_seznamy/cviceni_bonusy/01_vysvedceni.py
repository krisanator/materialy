# Bonus 1 – Seznamy
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci vyhodnot_vysvedceni, která má na vstupu seznam známek
#    a vrátí text:
#
#      "bez známek"             když je seznam prázdný
#      "neprospěl/a"            když je mezi známkami pětka
#      "s vyznamenáním"         když je průměr nejvýš 1.5 a žádná známka
#                               není horší než 2
#      "prospěl/a"              jinak
#
#    Vyzkoušej ji na seznamech [1, 2, 1], [1, 3, 2], [1, 5, 1] a [].

znamky = input("Zadej známky").split(", ")

def vyhodnot_vysvedceni(znamky):
    if len(znamky) == 0:
        return "bez známek"
    elif 5 in znamky:
        return "neprospěl/a"
    elif sum(znamky) / len(znamky) <= 1.5 and max(znamky) <= 2:
        return "s vyznamenáním"
    else:
        return "prospěl/a"

print(vyhodnot_vysvedceni)