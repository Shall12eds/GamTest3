import random
import time

Rolls = [0]
Comum = [0]
Incomum = [0]
Raro = [0]
Épico = [0]
Lendário = [0]
Mítico = [0]
Arcano = [0]
Exótico = [0]
Divino = [0]
Celestial = [0]
Ascendente = [0]
Eterno = [0]
Supremo = [0]
Abissal = [0]
Cósmico = [0]
Primordial = [0]
Trancedental = [0]
Onírico = [0]
Interdimencional = [0]
Omniversal = [0]

print("Lets go Gambling!!!")
while True:
    RNG = input("")
    if RNG == "":
        Rolls[0] += 1
        a = random.randint(1, 5)
        if a != 1:
            b = random.randint(1, 20)
            if b != 1:
                c = random.randint(1, 50)
                if c != 1:
                    d = random.randint(1, 75)
                    if d != 1:
                        e = random.randint(1, 150)
                        if e != 1:
                            f = random.randint(1, 250)
                            if f != 1:
                                g = random.randint(1, 500)
                                if g != 1:
                                    h = random.randint(1, 750)
                                    if h != 1:
                                        i = random.randint(1, 1000)
                                        if i != 1:
                                            j = random.randint(1, 2500)
                                            if j != 1:
                                                k = random.randint(1, 5000)
                                                if k != 1:
                                                    l = random.randint(1, 10000)
                                                    if l != 1:
                                                        m = random.randint(1, 50000)
                                                        if m != 1:
                                                            n = random.randint(1, 75000)
                                                            if n != 1:
                                                                o = random.randint(1, 100000)
                                                                if o != 1:
                                                                    p = random.randint(1, 150000)
                                                                    if p != 1:
                                                                        q = random.randint(1, 300000)
                                                                        if q != 1:
                                                                            r = random.randint(1, 500000)
                                                                            if r != 1:
                                                                                s = random.randint(1, 1000000)
                                                                                if s != 1:
                                                                                    t = random.randint(1, 500000)
                                                                                    if t != 1:
                                                                                        time.sleep(0.0001)
                                                                                    else:
                                                                                        print("Omniversal")
                                                                                        Omniversal[0] += 1
                                                                                else:
                                                                                    print("Interdimensional")
                                                                                    Interdimencional[0] += 1
                                                                            else:
                                                                                print("Onírico")
                                                                                Onírico[0] += 1
                                                                        else:
                                                                            print("Trancedental")
                                                                            Trancedental[0] += 1
                                                                    else:
                                                                        print("Primordial")
                                                                        Primordial[0] += 1
                                                                else:
                                                                    print("Cósmico")
                                                                    Cósmico[0] += 1
                                                            else:
                                                                print("Abissal")
                                                                Abissal[0] += 1
                                                        else:
                                                            print("Supremo")
                                                            Supremo[0] += 1
                                                    else:
                                                        print("Eterno")
                                                        Eterno[0] += 1
                                                else:
                                                    print("Ascendente")
                                                    Ascendente[0] += 1
                                            else:
                                                print("Celestial")
                                                Celestial[0] += 1
                                        else:
                                            print("Divino")
                                            Divino[0] += 1
                                    else:
                                        print("Exótico")
                                        Exótico[0] += 1
                                else:
                                    print("Arcano")
                                    Arcano[0] += 1
                            else:
                                print("Mítico")
                                Mítico[0] += 1
                        else:
                            print("Lendário")
                            Lendário[0] += 1
                    else:
                        print("Épico")
                        Épico[0] += 1
                else:
                    print("Raro")
                    Raro[0] += 1
            else:
                print("Incomum")
                Incomum[0] += 1
        else:
            print("Comum")
            Comum[0] += 1
    elif RNG == "stats":
        print("")
        print(f"Rolls: {Rolls[0]}")
        print(f"Comum: {Comum[0]}")
        print(f"Incomum: {Incomum[0]}")
        print(f"Raro: {Raro[0]}")
        print(f"Épico: {Épico[0]}")
        print(f"Lendário: {Lendário[0]}")
        print(f"Mítico: {Mítico[0]}")
        print(f"Arcano: {Arcano[0]}")
        print(f"Exótico: {Exótico[0]}")
        print(f"Divino: {Divino[0]}")
        print(f"Celestial: {Celestial[0]}")
        print(f"Ascendente: {Ascendente[0]}")
        print(f"Eterno: {Eterno[0]}")
        print(f"Supremo: {Supremo[0]}")
        print(f"Abissal: {Abissal[0]}")
        print(f"Cósmico: {Cósmico[0]}")
        print(f"Primordial: {Primordial[0]}")
        print(f"Trancedental: {Trancedental[0]}")
        print(f"Onírico: {Onírico[0]}")
        print(f"Interdimensional: {Interdimencional[0]}")
        print(f"Omniversal: {Omniversal[0]}")
    elif RNG == "rarity":
        print("")
        print("Comum 1 em 5")
        print("Incomum 1 em 20")
        print("Raro 1 em 50")
        print("Épico 1 em 75")
        print("Lendário 1 em 150")
        print("Mítico 1 em 500")
        print("Arcano 1 em 750")
        print("Exótico 1 em 1000")
        print("Divino 1 em 2000")
        print("Celestial 1 em 5000")
        print("Ascendente 1 em 10000")
        print("Eterno 1 em 50000")
        print("Supremo 1 em 100000")
        print("Abissal 1 em 500000")
        print("Primordial 1 em 2 milhões")
        print("Trancedental 1 em 3 milhões")
        print("Onírico 1 em 5 milhões")
        print("Interdimensional 1 em 10 milhões")
        print("Omniversal 1 em 15 milhões")
        print("")
    elif RNG == "rarity+":
        print("Comum (20%)")
        print("Incomum (5%)")
        print("Raro (2%)")
        print("Épico (1.33%)")
        print("Lendário (0.67%)")
        print("Mítico (0.2%)")
        print("Arcano (0.13%)")
        print("Exótico (0.1%)")
        print("Divino (0.05%)")
        print("Celestial (0.02%)")
        print("Ascendente (0.01%)")
        print("Eterno (0.002%)")
        print("Supremo (0.001%)")
        print("Abissal (0.0002%)")
        print("Primordial (0.00005%)")
        print("Trancedental (0.000033%)")
        print("Onírico (0.00002%)")
        print("Interdimensional (0.00001%)")
        print("Omniversal (0.0000067%)")
        print("")
