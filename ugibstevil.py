import random

vpr = input("Vnesi najvisje stevilo, ki naj bo med moznostmi za ugib : ")

if vpr.isdigit():
    vpr = int(vpr)

    if vpr <= 0:
        print('Vpisi stevilo vecje od 0.')
        quit()
else:
    print('Vpisati moras stevilo')
    quit()

nakljucno_stevilo = random.randint(0, vpr)
poskusi = 0
while True:
    poskusi += 1
    ugib = input("Ugibaj ustvarjeno stevilo: ")

    if ugib.isdigit():
        ugib = int(ugib)
    else:
        print('Vpisati moras stevilo')
        continue

    if ugib == nakljucno_stevilo:
        print("Uganil si stevilo " + str(nakljucno_stevilo))
        break
    elif ugib > nakljucno_stevilo:
        print("Stevilo je manjse")
    else: print("Stevilo je vecje")

print("Uganil si v " + str(poskusi) +" poskusih.")

