# Cvičení 1 – Seznamy
# Doplň kód pod zadání a soubor spusť (Run).

# Vytvoř seznam pěti svých oblíbených filmů. Vypiš:
#    - první film,
#    - poslední film,
#    - první tři filmy jako výřez,
#    - všechny filmy, každý na vlastní řádek s pomlčkou na začátku,
#    - kolik filmů v seznamu je.

filmy = ["Forrest Gump", "Legally Blonde", "The Matrix", "Inception", "Interstellar"]

print(filmy[0])

print(filmy[-1])

print(filmy[0:3])

for film in filmy:
    print("-", film)
    
print(len(filmy))