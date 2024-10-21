"""As Organizações Tabajara resolveram dar um abono_minimo aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono_minimo.
Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:

a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro;

b.O piso do abono_minimo será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades.

Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários.

Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono_minimo concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:

O salário de cada funcionário, juntamente com o valor do abono_minimo;
O número total de funcionário processados;
O valor total a ser gasto com o pagamento do abono_minimo;
O número de funcionário que receberá o valor mínimo de 100 reais;
O maior valor pago como abono_minimo; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa."""

salarios = []
lista_abonos = []
abono_minimo = 100
total = 0

while True:
    entrada = float(input('Digite o salário do funcionário: '))
    if entrada > 0:
        salarios.append(entrada)
    if entrada == 0:
        break

print(salarios)
print(f'{"Salário":<12}{"- Abono":<10}')
for salario in salarios:
    if salario < 1000:
        total = salario + abono_minimo
        lista_abonos.append(abono_minimo)
        print(f'R${salario:<10.2f}- R${abono_minimo:<10.2f}')
    else:
        abono_com_20 = salario * 0.20
        lista_abonos.append(abono_com_20)
        print(f'R${salario:<10.2f}- R${abono_com_20:<10.2f}')

print(f'Forma processados {len(salarios)} colaboradores')
print(f'Total gasto com abonos: {sum(lista_abonos):.2f}')
print(f'Valor mínimo pago a {lista_abonos.count(100)} colaboradores')
print(f'Maior valor de abono pago: R${max(lista_abonos):.2f}')
