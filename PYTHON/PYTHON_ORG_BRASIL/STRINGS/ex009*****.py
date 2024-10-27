def verificar_cpf(cpf):
    """Verifica se o CPF está no formato xxx.xxx.xxx-xx."""
    # Verifica o comprimento e se contém caracteres corretos
    if len(cpf) != 14:
        return False

    # Verifica cada parte do formato
    if not (cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-'):
        return False

    # Verifica se todos os outros caracteres são dígitos
    for i in range(14):
        if i in [3, 7, 11]:  # Ignora os caracteres de formatação
            continue
        if not cpf[i].isdigit():
            return False

    return True

# Solicita a digitação do CPF
cpf_input = input("Digite o CPF no formato xxx.xxx.xxx-xx: ")

if verificar_cpf(cpf_input):
    print("O CPF está no formato correto.")
else:
    print("O CPF está no formato inválido.")
