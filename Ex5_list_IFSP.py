num1 = int(input("Digite um número inteiro:"))
num2 = int(input("Digite outro número inteiro:"))
num3 = int(input("Digite outro número inteiro:"))

if num1 != num2 and num1 != num3 and num2 != num3:

    if num3 > num2 and num3 > num1:
        if num2 > num1:
            print(f"A ordem crescente dos números digitados é:\n{num1}\n{num2}\n{num3}")
        else:
            print(f"A ordem crescente dos números digitados é:\n{num2}\n{num1}\n{num3}")

    if num2 > num3 and num2 > num1:
        if num3 > num1:
            print(f"A ordem crescente dos números digitados é:\n{num1}\n{num3}\n{num2}")
        else:
            print(f"A ordem crescente dos números digitados é:\n{num3}\n{num1}\n{num2}")

    if num1 > num3 and num1 > num2:
        if num3 > num2:
            print(f"A ordem crescente dos números digitados é:\n{num2}\n{num3}\n{num1}")
        else:
            print(f"A ordem crescente dos números digitados é:\n{num3}\n{num2}\n{num1}")
else:
    print("Escreva números diferentes!")

    