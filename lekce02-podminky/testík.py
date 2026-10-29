# print(5 != 5)
# print(5 == 5)

# print(5 > 5)
# print(5 < 3)

# print(5 >= 5)
# print(5 <= 5)
# print(5 <= 30.5)

# print("Anna" == "Anna")
# print("Anna" == "ANNA")
# print("Anna" != "ANNA")

# pravda = True #nepíše se v uvozovkách, protože Python tuto hodnotu umí rozeznat sám
# print(pravda)
# print("Promenna pravda je",pravda)

# pravda = 5 >= 3
# print("Promenna pravda je",pravda)

# teplota = 25
# je_zima = teplota < 5
# print("Zima", je_zima)

# teplota = 2
# je_zima = teplota < 5
# print("Zima", je_zima)

# vek = 20
# print("Neni mi", vek)
# print(vek == 20)
# # ""="" -> to je přiřazení ; ""=="" -> to je rovná se

# if podminka:
#     # prikaz kdyz podminka plati

# vek = int(input("Kolik je ti let?"))

# if vek >= 18:
#     print("jsi plnolety")
#     print('muzes volit')

#  print("Konec programu")

# teplota = 20
# if teplota > 15:
#     print("To je hezky.")
# else:
#     print("Je mi zima.")

# prikazovy radek vzdy konci : a pak je odsazovy blok, bez toho na sebe nebude navazovat, odsazeni je vzdy 4 mezery\


# elif podminka:
#     prikaz kdyz podminka plati

# elif podminka2:
#     prikaz kdyz druha podminka plati

# znamka = 3
# if znamka == 1:
#     print("Výborně")
# elif znamka == 2:
#     print("Chvalitebné")
# elif znamka == 3:
#     print("Dobré")
# elif znamka == 4:
#     print("Dostatečné")
# elif znamka == 5:
#     print("Nedostatečné")
# else:
#     print("To není platná známka.")

# venku_prsi = True
# mam_destnik = True

# if venku_prsi:
#     if mam_destnik:
#         print("Co se da delat, aspon ze nezmoknu")
#     else:
#         print("To je teda smula, zmoknu.")
# else:
#     if mam_destnik:
#         print("Tahnu destnik zbytecne")
#     else:
#         print("Mam stesti, neprsi.")
 
# vek = 68
# print(vek >= 18 and vek < 65)

# den = "neděle"
# if den == "sobota" or den == "neděle":
#     print("Je víkend.")

# a = int(input("Zadej stranu a:"))
# b = int(input("Zadej stranu b:"))

# if a >= 0 and b >= 0:
#     print("Obsah obdelníka je", a * b)
#     if a == b:
#         print("Tento obdelnik je ctverec.")
# else:
#     print("To neni obdelnik.")

# if a <= 0 or b <= 0:
#     print("Neni obdelnik.")

# print("not True je", not True)

# print("not False je", not False)

# a = -1
# b = 5
# print(not (a>0 and b>0))
# # ale je to stejny jako
# print(a < 0 or b < 0)

# heslo_ok = True
# jmeno_ok = True

# if not (heslo_ok and jmeno_ok):
#     print("Přihlášení je neplatné.")