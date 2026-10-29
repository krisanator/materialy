# Cvičení 1 – And, or a not
# Doplň kód pod zadání a soubor spusť (Run).

# Platný trojúhelník. Ze tří stran jde sestavit trojúhelník jen tehdy,
#    když je součet každých dvou stran větší než ta třetí.
#    Vypiš "Platný trojúhelník." / "Takový trojúhelník nejde.".
a = -1
b = 1
c = -1

if (a + b) > c or (b + c) > a or (c + a) > b:
    print("Platný trojújelník")
else:
    print("Takový trojúhelník nejde.")

