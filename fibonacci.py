def fibo(x):
    ultimo = 0
    penultimo = 1

    while True:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo

        if x == termo:
            print(f'O número {x} existe na Sequência de Fibonacci')
            break
        elif termo > x:
            print(f'o número {x}, não existe na Sequência de Fibonacci')
            break


fibo(7)
