print("1-es szék, 2-es szék, 3-as szék, 4-es szék ,5-ös szék(1,2,3,4,5)")
szek_valasztas = int(input("Melyik széket szeretnéd lefoglalni?"))
szekek = [1,2,3,4,5,6,7,8]
if szek_valasztas == 1:
    for i in range(1):
        print(f"{szekek[0]}-es széket lefoglaltad")
elif szek_valasztas == 2:
    for i in range(1):
        print(f"{szekek[1]}-es széket lefoglaltad")
elif szek_valasztas == 3:
    for i in range(1):
        print(f"{szekek[2]}-as széket lefoglaltad")
elif szek_valasztas == 4:
    for i in range(1):
        print(f"{szekek[3]}-es széket lefoglaltad")
elif szek_valasztas == 5:
    for i in range(1):
        print(f"{szekek[4]}-ös széket lefoglaltad")
elif szek_valasztas == 6:
    for i in range(1):
        print(f"{szekek[5]}-os széket lefoglaltad")
elif szek_valasztas == 7: 
    for i in range(1):
        print(f"{szekek[6]}-es széket lefoglaltad")
elif szek_valasztas == 8:
    for i in range(1):
        print(f"{szekek[len(szekek)-1]}-as széket lefoglaltad")
else:
    print("Nem áll ilyen szék a rendelkezésre")















#extra commit
