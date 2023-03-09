palavra = input('Digite a palavar que deseja inverter: ')

valor = len(palavra) - 1

for letra in palavra:
    print(palavra[valor], end="")
    valor -= 1
