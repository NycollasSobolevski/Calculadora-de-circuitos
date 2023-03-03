

# escolha = int(input("Escolha uma operação: \n 1 - Calcular resistencia\n 2 - Calcular Potencia\n 3 - Calcular corrente\n\n"))

# match escolha:
#     case 1:
#         numbers = []
#         quantity = input("Insira a quantidade de resistores:\n>")
#         for i in range(quantity):
#             resistors = int(input(f"Insira o resistor {i}\n>"))
#             numbers.append(resistors)
#         print("oi")
#     case 2:
#         print("DOIS")
#     case 3:
#         print("DOIS")



def ResistCalc():
    chose = int(input("""
    Calcular:
    1 - Associacao de Resistores (Ohm)
    2 - Potencia (v)
    3 - Corrente (A)
    """))

    match chose:
        case 1:
            associacao = input(" P - Paralelo\n S - Serie \n> ")
            match associacao:
                case 'p':
                    qnt = int(input("Insira a quntidade de resistores: \n> "))
                    resists = []
                    for i in range(qnt):
                        resists.append(float(input(f"Insira o {i+1}º resistor: \n> ")))
                    aux = (resists[0]*resists[1]) / (resists[0]+resists[1])
                    if len(resists) > 2:
                        for i in range(len(resists)):
                            if i > 1:
                                Req = ((resists[i]*aux) / (resists[i]+aux))
                                aux = Req
                        print("\n\nResultado =" + Req)
                    else:
                        print("\n\nResultado =" + aux)
                case 's':
                    qnt = int(input("Insira a quntidade de resistores: \n> "))
                    resists = []
                    for i in range(qnt):
                        resists.append(float(input(f"Insira o {i+1}º resistor: \n> ")))
                    print(f"\n\nResultado: {sum(resists)}")
        case 2:
            i = float(input("Insira a corrente (i)A: \n> "))
            r = float(input("Insira a resistencia (r)OHM: \n> "))
            print("Resultado = " + (r*i))
        case 3:
            v = float(input("Insira a potencia (v)V: \n> "))
            r = float(input("Insira a resistencia (r)OHM: \n> "))
            print("Resultado = " + (v/r))






def CapCalc():
    kcalc = 8.85*(10**(-12))
    chose = input("calcular c/ k/ a/ d/ ou Ceq(T)/\n> ")
    match chose:
        case 'c':
            a = float(input("Insira Area (A):\n> "))
            k = float(input("Insira Constante Dielétrica(K):\n> "))
            d = float(input("Insira Distancia (D):\n> "))
            print(k*(a/d)*(kcalc))
        case 'd':
            a = float(input("Insira Area (A):\n> "))
            k = float(input("Insira Constante Dielétrica(K):\n> "))
            c = float(input("Insira Capacitancia (C):\n> "))
            print((k*a*(kcalc))/c)
        case 'a':
            d = float(input("Insira Distancia (D):\n> "))
            k = float(input("Insira Constante Dielétrica(K):\n> "))
            c = float(input("Insira Capacitância (C):\n> "))
            print((c*d)/(k*kcalc))
        case 'k':
            c = float(input("Insira Capacitância (C):\n> "))
            a = float(input("Insira Area (A):\n> "))
            d = float(input("Insira Distancia (D):\n> "))
            print(-((-1*c)*((a/d)*kcalc)))
        case 't':

            qtd = int(input("Insira a quantidade total de capacitores:"))
            parallel = []
            serie = []
            sum_serie = 0
            while 1:
                chose = input("Deseja adicionar Série (s), Paralelo (p) ou Calcular (c):")
                if(chose == 's'):
                    qtd = int(input("insira a quantidade"))
                    sum = 0
                    for i in range(qtd):
                        serie.append(int(input(f"insira o {i+1}º capacitor: \n>")))
                    qtd = 0
                elif(chose == 'p'):
                    qtd = int(input("insira a quantidade"))
                    sum = 0
                    for i in range(qtd):
                        sum += int(input(f"insira o {i+1}º capacitor: \n>"))
                    parallel.append(sum)
                    qtd = 0
                elif(chose == 'c'):
                    for item in parallel:
                        serie.append(item)
                    for item in serie:
                        sum_serie += (item**-1)
                    res = (sum_serie**-1)
                    print(f"Resultado: {res}")
                    res = 0
                    qtd = 0
                    break





while 1:
    operation = int(input("""
    Insira a operação:\n> 
        1 - Calcular Resistor 
        2 - Calcular Capacitor
        0 - Sair
    """))

    match operation:
        case 1:
            ResistCalc()
        case 2:
            CapCalc()
        case 0:
            break


