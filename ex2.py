notas = [7.0, 1.5, 10.0, 8.5, 3.0]
print(f"Essas são as notas: {notas}")
remove = float(input("Digite qual nota quer remover: "))
notas.remove(remove)

for x in notas:
        print(f"Sua nota é: {x}")