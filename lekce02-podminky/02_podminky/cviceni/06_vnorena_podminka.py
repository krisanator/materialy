# Cvičení 6 – Podmínky
# Doplň kód pod zadání a soubor spusť (Run).

# Vnořená podmínka s otázkami na uživatele.
#    Zeptej se: "Máš hlad? (ano/ne)" a ulož odpověď do proměnné hlad.
#    Když má hlad, zeptej se ještě "Máš doma jídlo? (ano/ne)":
#      - když má jídlo, vypiš "Uvař si."
#      - když nemá, vypiš "Objednej si."
#    Když nemá hlad, vypiš "Tak nic, uvidíme později.".

hlad = (input("Máš hlad? ano/ne"))
if hlad == "ano":
    co_ted = (input("Máš doma jídlo? ano/ne"))
    if co_ted == "ano":
        print("Uvař si.")
    elif co_ted == "ne":
        print("Objednej si.")
elif hlad == "ne":
    print("Tak nic, uvidíme se později.")

