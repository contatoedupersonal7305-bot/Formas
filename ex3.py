notas = [7.0, 1.5, 10.0, 8.5, 3.0]
print(f"Essas são as notas: {notas}")

posicao = int(input("Digite a posição da nota a alterar (0 a 4): "))

nova_nota = float(input("Digite o novo valor da nota: "))

notas[posicao] = nova_nota

for x in notas:
    print(f"Sua nota é: {x}")