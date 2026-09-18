def circulo():
    print("Cálculo de área do circulo")
    raio = float(input("Digite o tamanho do raio: "))
    area = (raio * raio) * 3.14
    print(f"A área é {area}")
def triangulo():
    print("Cálculo de área do triangulo")
    base = float(input("Digite o tamanho da base: "))
    altura = float(input("Digite o tamanho da altura: "))
    area = (base * altura) / 2
    print(f"A área é {area}")
def quadrado():
    print("Cálculo de área do quadrado")
    lado = float(input("Digite a medida do lado: "))
    area = lado * lado
    print(f"A área é {area}")
def retangulo():
    print("Cálculo de área do retangulo")
    base = float(input("Digite o tamanho da base: "))
    altura = float(input("Digite o tamanho da altura: "))
    area = base * altura
    print(f"A área é {area}")
def paralelogramo():
    print("Cálculo de área do paralelogramo")
    base = float(input("Digite o tamanho da base: "))
    altura = float(input("Digite o tamanho da altura: "))
    area = base * altura
    print(f"A área é {area}")
def losango():
    print("Cálculo de área do losango")
    diagonal1 = float(input("Digite o tamanho da diagonal maior: "))
    diagonal2 = float(input("Digite o tamanho da diagonal menor: "))
    area = (diagonal1 * diagonal2) / 2
    print(f"A área é {area}")
def trapezio():
    print("Cálculo de área do trapezio")
    base1 = float(input("Digite o tamanho da base maior: "))
    base2 = float(input("Digite o tamanho da base menor: "))
    altura = float(input("Digite o tamanho da altura: "))
    area = ((base1 + base2) * altura) / 2
    print(f"A área é {area}")



print("====================")
print("Calculadora de Áreas")
print("====================")
print("1 - Círculo")
print("2 -  Triangulo")
print("3 - Quadrado")
print("4 - Retangulo")
print("5 - Paralelogramo")
print("6 - Losango")
print("7 - Trapézio")
print("0 - Sair")
print("====================")   

opcao = int(input("Qual a opção? "))

while True:
    if opcao == 1:
        circulo()
        opcao = int(input("Qual a opção? "))
    elif opcao == 2:
        triangulo()
        opcao = int(input("Qual a opção? "))
    elif opcao == 3:
        quadrado()
        opcao = int(input("Qual a opção? "))
    elif opcao == 4:
        retangulo()
        opcao = int(input("Qual a opção? "))
    elif opcao == 5:
        paralelogramo()
        opcao = int(input("Qual a opção? "))
    elif opcao == 6:
        losango()
        opcao = int(input("Qual a opção? "))
    elif opcao == 7:
        trapezio()
        opcao = int(input("Qual a opção? "))
    elif opcao == 0:
        break
    else:
        print("Opção Inválida. Tente Novamente.")
        
