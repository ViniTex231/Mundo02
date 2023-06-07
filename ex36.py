valor = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
anos = int(input("Quantos anos vai pagar? "))

mensalidade = valor / (anos * 12)
minimo = salario * 30 / 100
if mensalidade <= minimo:
    print("O empréstimo foi aprovado")
else:
    print("O empréstimo foi negado")