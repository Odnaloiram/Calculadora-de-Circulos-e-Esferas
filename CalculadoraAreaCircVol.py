print("=== CALCULADORA DE CÍRCULOS E ESFERAS ===\n")

pi = 3.14

while (True):
    opcao = str(input("Qual operação deseja realizar?\n'A' para Área\n'C' para Circunferencia\n'V' para Volume\nDigite: "))

    match opcao:
        case 'A':
            print("\n=== CALCULADORA DE ÁREA DE CÍRCULO ===\n")

            raio = float(input("Insira o valor do raio: "))

            area = pi * raio ** 2

            print("\n------------------------")
            print("A área do círculo é: ", area)
            print("------------------------\n")


        case 'C':
            print("\n=== CALCULADORA DE CIRCUNFERÊNCIA DE CÍRCULO ===\n")

            raio = float(input("Insira o valor do raio: "))

            circunferencia = 2 * pi * raio

            print("\n-----------------------")
            print("A circunferencia do círculo é: ", circunferencia)
            print("-----------------------\n")


        case 'V':
            print("\n=== CALCULADORA DE VOLUME DE ESFERA ===\n")

            raio = float(input("Insira o valor do raio: "))

            volume = 4/3 * pi * raio**3

            print("\n-----------------------")
            print("O volume da esfera é: ", volume)
            print("-----------------------\n")

    reiniciar = str(input("Deseja reiniciar as calculadoras? S/N (S para sim N para não): "))
    if reiniciar != 'S' and reiniciar != 's' and reiniciar != 'N' and reiniciar != 'n':
        print("Caracteres Inválidos")
        break
    if reiniciar == 'N' or reiniciar == 'n':
        break