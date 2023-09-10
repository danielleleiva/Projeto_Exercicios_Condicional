ano_nascimento = int(input("Digite seu ano de nascimento:\n"))
conta_votar = 2023 - ano_nascimento

if conta_votar >= 18:
    print("De acordo com sua idade, você poderá votar esse ano!")
else:
    print("De acordo com sua idade, você não poderá votar esse ano!")

    