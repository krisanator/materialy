# heslo = input("Zadej heslo: ")
# while heslo != "pyladies":
# 	print("Neprihlasena")
# 	heslo = input("Zadej heslo")
# print("Vitej")

# from random import randrange

# hod = randrange(1,7)
# while hod != 6:
#     print("Padlo:", hod, "hazime znovu")
#     hod = randrange(1,7)
# print("Padla", hod, ".Vyhrala jsi!")

# from random import randrange

# hod = randrange(1,7)
# while hod != 6:
#     if hod == 1:
#     print("koncime")
#     break
#     print("Padlo:", hod, "hazime znovu")
#     hod = randrange(1,7)
# print("Padla", hod, ".Vyhrala jsi!")

# je_pravda = 1 == 2
# print(je_pravda)

# while 1 == 2:
#     print("ahoj")

# soucet = 0
# while True:
#     odpoved = input("Zadej cislo(nebo 'konec')")
#     if odpoved == 'konec':
#         break

#     cislo = int(odpoved)
#     if cislo < 0:
#         print("Zaporna cisla ignorujeme")
#         continue
#     soucet = soucet + cislo
#     print("Zatim mame:", soucet)
# print("Soucet", soucet)



soucet = 0
while True:
    odpoved = input("Zadej cislo(nebo 'konec')")
    if odpoved == 'konec':
        break

    cislo = float(odpoved)
    if cislo < 0:
        print("Zaporna cisla ignorujeme")
        continue
    soucet = soucet + cislo
    print("Zatim mame:", soucet)
print("Soucet", soucet)

