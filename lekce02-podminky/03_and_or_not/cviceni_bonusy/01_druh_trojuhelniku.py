# Bonus 1 – And, or a not
# Doplň kód pod zadání a soubor spusť (Run).

# Druh trojúhelníku. Máš tři strany. Urči a vypiš, jaký to je
#     trojúhelník:
#       - "rovnostranný", když jsou všechny tři strany stejné,
#       - "rovnoramenný", když jsou aspoň dvě strany stejné,
#       - "různostranný", když jsou všechny strany různé.
a = 2
b = 5
c = 8

if(a == b):
    if((a + b) > c):
        print("yes")
    else:   print("no")

# zapomněla jsem elif, nahoře jsou intrukce, které je potřeba si přečíst, není vůbec důležitý, jestli vím, jak vypadá rovnostranný, rovnoramenný apod., zároveň tohle není excel
#  a není potřeba stavět složité if funkce

# python funguje lineárně, takže musím začít nejstriktnější podmínkou, jestliže chci ubírat kritéria