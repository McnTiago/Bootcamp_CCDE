print('########## PROGRAMA PARA CALCULO DE SALÁRIO LÍQUIDO 1.0 ##########\n')
salario_fixo = int(input('Digite seu salário bruto: '))
venda_mes = int(input('Quantas vendas você realizou no mês: '))
valor_comissao = int(input('Qual sua comissão por venda? '))
descontos = int(input('Quanto de desconto há por mês od seu salário? '))
total_comissao = (venda_mes * valor_comissao)
salario_liquido = (salario_fixo + total_comissao - descontos)

print('Seu salário líquido é: \n', salario_liquido)