def add(num_1, num_2):
    """
    Soma de dois números e retorna o resultado.
    :param num_1: Primeiro número a ser somado.
    :param num_2: Segundo número a ser somado.
    :return: A soma dos dois números.
    """
    return num_1 + num_2

def subtract(num_1, num_2):
    """
    Subtrai dois números e retorna o resultado.
    :param num_1: Primeiro número a ser subtraído.
    :param num_2: Segundo número a ser subtraído.
    :return: A diferença entre os dois números.
    """
    return num_1 - num_2

def multiply(num_1, num_2):
    """
    Multiplica dois números e retorna o resultado.
    :param num_1: Primeiro número a ser multiplicado.
    :param num_2: Segundo número a ser multiplicado.
    :return: A multiplicação entre os dois números.
    """
    return num_1 * num_2

def divide(num_1, num_2):
    """
    Divide dois números e retorna o resultado.
    :param num_1: Primeiro número a ser dividido.
    :param num_2: Segundo número a ser dividido.
    :return: A divisão entre os dois números.
    """
    return num_1 / num_2


print("Bem-vindo a Calculadora!")

def calculator():
    """
    Calculadora básica que permite o usuário escolher entre operações aritméticas básicas
    e continuar realizando cálculos com o resultado da operação anterior.
    """
    operations = {"+": add,
                  "-": subtract,
                  "*": multiply,
                  "/": divide}

    first_num = float(input("\nDigite o primeiro número: "))

    for operation in operations.keys():
        print(operation)

    answer = "S"
    while answer.upper() == "S":
        op_symbol = input("Escolha um operador: ")
        if op_symbol in operations.keys():

            next_num = float(input("Digite o próximo número: "))

            result = operations[op_symbol](first_num, next_num)
            print(f"{first_num} {op_symbol} {next_num} = {result}")

            answer = input(f"Digite [S] para continuar o cálculo com {result}, digite [N] para iniciar um "
                           f"novo cálculo ou digite [Sair] para sair: ")

            if answer.upper() == "S":
                first_num = result
            elif answer.upper() == "N":
                calculator()
            else:
                exit()
        else:
            print("Opção Inválida!")


# Inicia a calculadora
calculator()