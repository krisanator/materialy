basnicka = "Skakal pes pres oves pres zelenou louku"
pocet_pismen = {}


for pismeno in basnicka:
    if pismeno not in pocet_pismen:
        pocet_pismen[pismeno] = 1
    else:
        pocet_pismen[pismeno] = pocet_pismen[pismeno] + 1



print(pocet_pismen)