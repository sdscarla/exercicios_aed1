#Ler dois números. Somar os números lidos e, após, multiplicar o resultado da soma pelo primeiro número lido. Apresentar o resultado final.

n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))

soma = n1 + n2
multi = soma * n1

print(f"Resultado: {multi}")