notas = [7.0, 1.5, 10.0, 8.5, 3.0]
nova = float(input("Digite a nova nota: "))
notas.append(nova)

# contador = 0
# limite = len(notas) - 1

# while contador <= 4:
#         print(f"Sua nota é: {notas[contador]}")
#         contador += 1
for x in notas:
        print(f"Sua nota é: {x}")