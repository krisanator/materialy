# #opakovani je matka moudrosti:

# print("ahoj")
#       # print = tohle je funkce
#       # ("ahoj") = tohle je vstup
#       # některé funkce nepotřebují argument, aby měly výstup
#       # argumenty se oddělují čárkou:
# print("Ahoj", "Kris", "!")

# print(1, 2, 3, sep="-", end="!!!")

# input("kolik ti je")
# # můžou mít vstup/argument, a bude mít výstup


# vek = input("kolik ti je")
# print(vek)

# vek = input("kolik ti je?")
# print(vek + 1)
# # u funkci, ktere vraci hodnoty, je potreba zohlednit, jake to vraci hodnoty
# # python jargon = "string"

# vek = input("kolik ti je?")
# print(vek + "1")
# # ted se z toho stal text, takže to jen přidá jako další znak

# vek = int(input("kolik ti je?"))
# print(vek + 1)

# # to je to stejny jakobych měla     vek = int(66)
# #                                   print(vek + 1)

# # "co se hodi v pythonu z matiky"

# jmeno = input("jmeno?")
# print("tve jmeno je", len(jmeno), "dlouhe")

# # to je z excelu len, pocita pocet znaku, to by mohlo byt dobry na kontrolu delky hesla

# print(len("Ahoj pepo"))

# # python jargon.2 = substring, budeme si povidat o pozicich

# print(len("A") + 2)

# print(abs(7))
# # uplne stejny abs jako v excelu
# print(abs(-7))

# print(round(3.14159))

# # python zaokrouhlovava na cele cislo, pokud chceme definovat na co zaokrouhlovat, je potřeba další argument
# print(round(3.14159), 10)
# # proc to printuje 3 10???

# print(min(2, 3, -5))
# # stejne minimum jako excel, obdobne take max
# print(max(2, 3, -5))

# print(max(2, 3, -5) < 4)

# print(range(5))
# # DULEZITE, budeme pouzivat cely semsetr
# # takhle to vraci cisla od 0 do 4

# print(len(range(5)))

# for i in range(5):
#     print(i)

# for i in range(2, 10):
#     print(i)
# # range je pouze na cislo, neni ani na cislo ani retezec, je to interval cisel

# print(max(range(10)))
# # range (od-tohohle-cisla-vcetne, mimo-tohle-cislo) > range (od 2, do 10 takze napisu 11)
# umi to i minusova cisla, ale musi to mit spravny syntax

# for i in range(-10,2)
# # cyklus resp. v en: for loop, takze for cyklus

# print("Ahoj")
# print("Ahoj")
# print("Ahoj")
# print("Ahoj")

# # to je to stejny jako:

# for i in range(4):
#     print("Ahoj")

# for i in range(4):
#     print("Ahoj", str(i))
# # tohle bude v kazdem cyklu obsahovat cislo

# for i in range(100):
#     if(i % 2 == 0):
#       print("sude", i)
#     else:
#       print("liche", i)

# # str je opak int
# # je potreba davat pozor na odsazeni, opet, python exekuje linearne

# soucet = 0
# for i in range(0, 5):
#       soucet = soucet + i
# print(soucet)

# # to same jako 0 + 1 + 2 + 3 + 4
# # musime definovat zacatek mimo cyklus

# vnoreny cyklus:
# for i in range(5):
#     print(i)
#     for j in range(4):
#         print("kolo:", i, "pokus:", j)

# jmeno = input("jmeno?")

# for pismeno in jmeno:
#     print(pismeno)

#     # tohle vyhlaskuje

jmeno = input("jmeno?")

for pismeno in jmeno:
    print(pismeno, "!")

# range zvladne jeste treti argument (0, 10,2) coz podle toho bude preskakovat po tolikatem cisle, takze:
# (0, 10, 2) = 0, 2, 4, 6, 8