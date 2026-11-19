# Cvičení 2 – Seznamy
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se na jméno. Když je na seznamu hostů, vypiš "Vítej!".
#    Když není, vypiš "Na seznamu nejsi.".
#    Vstup uprav tak, aby prošlo i " anna " nebo "ANNA".

hoste = ["Anna", "Petra", "Jana", "Eva"]

jmeno = input("Jak se jmenuješ?").capitalize()
jmeno = jmeno.strip().capitalize()
if jmeno in hoste:
    print("Vítej, ", jmeno)
else:
    print("Na seznamu nejsi.")