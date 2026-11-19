# SEZNAMY

hoste = ["Marta", "Shrek", "Petr Pavel"]
print(hoste)

organizator = "Karel"
organizator = organizator + " Gott"
hoste = hoste + ["Karkulka"]
# sčítat můžeme pouze listy/seznamy
print(organizator, "zve", hoste, "na vánoční večírek.")
print(organizator)
print("Na večírek je pozváno", len(hoste), "hostů.")

pozvanka = "Zvu tě na svůj vánoční večírek. " + organizator[0] +  organizator[6]

print(pozvanka)

for host in hoste:
    print("Zvu tě na vánoční večírek", host)



# https://docs.python.org/2/library/functions.html

blacklist = ["Hegerová", "Vlk"]

prichozi = input("Jak se jmenuješ?")

def kontrola(prichozi, hoste, blacklist):
    if prichozi in hoste:
        print("Pojď dál", prichozi)
    elif prichozi in blacklist:
        print("Kšá", prichozi)
    else:
        print("Nejsi zván,",prichozi)

def pozvi(jmeno, hoste):
    hoste.append(jmeno)

pocet_hostu = len(hoste)

# prepiste jako for cyklus s funkci range
for i in range(pocet_hostu):
    print("Zvu tě na Vánoční večírek", hoste[i])

print("První byl/a pozván/a", hoste[0])

hoste[0] = "Martina"

print(hoste)

print(organizator.split())

# pop, remove, split, join

inicialy = ""
for slovo in organizator.split():
    inicialy = inicialy + slovo[0]
print(inicialy)

# lepsi je
for slovo in organizator.split():
    inicialy.append(slovo[0])
print(inicialy)

# join se musí dávat nad stringem

def odeber_hosta(jmeno, hoste):
    hoste.remove(jmeno)

odeber_hosta("Vojta", hoste)
print(hoste)

fronta = ["Vojta", "Petra", "Oslík", "Shrek"]

fronta.pop()