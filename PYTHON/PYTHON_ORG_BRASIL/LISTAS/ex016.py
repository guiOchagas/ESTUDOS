def calcular_salario(vendas_brutas):
    salario_base = 200
    comissao = 0.09 * vendas_brutas
    return salario_base + comissao


def intervalo_salario(salario):
    if salario < 200:
        return -1  # Para salários abaixo de $200
    return min(int(salario // 100) - 2, 8)  # A partir de $200 até $999 e $1000+


def main():
    vendedores = [100, 3000, 4000, 1500, 2000, 10000, 2500, 5000]  # Exemplo de vendas brutas
    contadores = [0] * 9  # Para os 9 intervalos

    for vendas in vendedores:
        salario = calcular_salario(vendas)
        posicao = intervalo_salario(salario)

        if posicao != -1:  # Ignora salários abaixo de $200
            contadores[posicao] += 1

    # Exibe resultados
    intervalos = [
        "$200 - $299",
        "$300 - $399",
        "$400 - $499",
        "$500 - $599",
        "$600 - $699",
        "$700 - $799",
        "$800 - $899",
        "$900 - $999",
        "$1000 e acima"
    ]

    for i in range(len(contadores)):
        print(f"Intervalo {intervalos[i]}: {contadores[i]} vendedor(es)")


if __name__ == "__main__":
    main()
