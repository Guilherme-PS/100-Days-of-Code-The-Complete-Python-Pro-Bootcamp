# Boas vindas ao usuário.
print("Bem-Vindo a Calculadora de Gorjetas\n")

# Obtém o valor total da conta do usuário
total_account = float(input("Qual o valor total da conta? R$"))
# Obtém a porcentagem que o usuário gostaria de dar.
tip_percent = float(input("Qual porcentagem de gorjeta você gostaria de dar? [10], [12] ou [15]?: "))
# Obtém números de pessoas para dividir a conta.
split_account = int(input("Quantas pessoas são para dividir a conta?: "))

# Calcula o valor que cada pessoa deve pagar
math = total_account * (tip_percent / 100 + 1) / split_account

# Imprime o valor que cada pessoa deve pagar e formatando o resultado a duas casas decimais.
print(f"\nCada pessoa deve pagar R${math:.2f}")