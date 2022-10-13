# 1
nome = 'Joao Joaquin'
rm = '00000'

print(f'Nome: {nome} \n'
      f'RM: {rm}')

# 2
mes_anterior = int(input('Leitura anterior (kWh): '))
mes_atual = int(input('Leitura atual (kWh): '))

consumo_mes = mes_atual - mes_anterior
tuds_alicota = 0.40942
te_alicota = 0.38317
pispasep_alicota = 0.1
confins_alicota = 0.462

tuds_calc = consumo_mes * tuds_alicota
te_calc = consumo_mes * te_alicota
pispasep_calc = consumo_mes * pispasep_alicota
confins_calc = consumo_mes * confins_alicota

total_pagar = tuds_calc + te_calc + pispasep_calc + confins_calc

print(f'Consumo do mês (kWh): {consumo_mes}')
print(f'TUSD: {tuds_calc:.2f}')
print(f'TE: {te_calc:.2f}')
print(f'PIS/PASEP: {pispasep_calc:.2f}')
print(f'COFINS: {confins_calc:.2f}')
print(f'Total a pagar (R$): {total_pagar:.2f}')

# 3
salario_bruto = float(input('Salário bruto = R$ '))
n_dependentes = int(input('Número de dependentes = '))
outros_descontos = float(input('Outros descontos (vale transporte, vale refeição, planos de saúde etc.) = R$ '))

if salario_bruto <= 1.212:
  inss = salario_bruto * 0.075
elif salario_bruto <= 2427.35:
  inss = salario_bruto * 0.09
elif salario_bruto <= 3641.03:
  inss = salario_bruto * 0.12
elif salario_bruto <= 7087.22:
  inss = salario_bruto * 0.14
else:
  inss = 828.39

base_calculo = salario_bruto - inss - n_dependentes * 189.59

if salario_bruto <= 1903.98:
  irrf = (base_calculo * 0) - 0
elif salario_bruto <= 2826.65:
  irrf = (base_calculo * 0.075) - 142.80
elif salario_bruto <= 3751.05:
  irrf = (base_calculo * 0.15) - 354.80
elif salario_bruto <= 4664.68:
  irrf = (base_calculo * 0.225) - 636.13
else:
  irrf = (base_calculo * 0.275) - 869.36

salario_liquido = salario_bruto - inss - irrf - outros_descontos

print(f'Salário bruto = R$ {salario_bruto:.2f}')
print(f'INSS = R$ {inss:.2f}')
print(f'IRRF = R$ {irrf:.2f}')
print(f'Outros descontos = R$ {outros_descontos:.2f}')
print(f'Salário líquido = R$ {salario_liquido:.2f}')
