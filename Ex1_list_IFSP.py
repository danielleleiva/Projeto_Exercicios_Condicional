valor1 = int(input("Digite o valor 1:\n"))
valor2 = int(input("Digite o valor 2:\n"))

if valor1 != valor2:
    if valor1 > valor2:
        print("O valor 1 digitado é maior que o valor 2 digitado!")
    else:
        print("O valor 2 digitado é maior que o valor 1 digitado!")
else:
    print("Digite valores diferentes!")