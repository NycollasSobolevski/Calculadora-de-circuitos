

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



# # def ResistCalc(list):
# #     for i in range(len(list)):
# #         b = i
# #         c = i+1
# #         if(i==0):
# #             calc = (b * c) / (b + c)
# #             b = calc
# #         else:
# #             calc = 

# #     return list*b/list+b


# def CapCalc(area,capacitancia,distancia,coeficiente):
#     c = k*a/d*(8,85*10**-12)


operation = int(input("Insira a operação:\n> "))

match operation:
    case 1:
        kcalc = 8.85*(10**(-12))
        chose = input("calcular c/ k/ a/ ou d/\n> ")
        match chose:
            case 'c':
                a = float(input("Insira A:\n> "))
                k = float(input("Insira K:\n> "))
                d = float(input("Insira D:\n> "))
                print(k*(a/d)*(kcalc))
            case 'd':
                a = float(input("Insira A:\n> "))
                k = float(input("Insira K:\n> "))
                c = float(input("Insira C:\n> "))
                print((k*a*(kcalc))/c)

