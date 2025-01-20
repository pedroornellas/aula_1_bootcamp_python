
# print(int(input("Digite valor: ")) + int(input("Digite valor: ")))

constante_bonus = 1000
nome = input("Digite o nome: ")
valor_salario_mensal =int(input("Dgite o valor do salario mensal: "))
valor_percentual_bonus = float(input("Digite o percentual do bônus: "))
kpi = constante_bonus + valor_salario_mensal*valor_percentual_bonus

print(f"O usuário {nome}, possui o bônus de {kpi}")




