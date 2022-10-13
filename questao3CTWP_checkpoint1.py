salarioBruto = float(input("Salário bruto: R$ "))
numDepend = int(input("Número de dependentes: "))
outrosDesc = float(input("Outros descontos (vale transporte, vale refeição, plano de saúde etc.): R$ "))

if salarioBruto <= 1212.00:
    inss = salarioBruto * 0.075
elif salarioBruto <= 2427.35:
    inss = salarioBruto * 0.09
elif salarioBruto <= 3641.03:
    inss = salarioBruto * 0.12
elif salarioBruto <= 7087.22:
    inss = salarioBruto * 0.14
else:
    inss = 828.39

if (salarioBruto - inss - (numDepend * 189.59)) <= 1903.98:
    irrf = 0
elif salarioBruto - inss - (numDepend * 189.59) <= 2826.65:
    irrf = (salarioBruto - inss - (numDepend * 189.59)) * 0.075 - 142.80
elif salarioBruto - inss - (numDepend * 189.59) <= 3751.05:
    irrf = (salarioBruto - inss - (numDepend * 189.59)) * 0.15 - 354.80
elif salarioBruto - inss - (numDepend * 189.59) <= 4664.68:
    irrf = (salarioBruto - inss - (numDepend * 189.59)) * 0.225 - 636.13
else:
    irrf = (salarioBruto - inss - (numDepend * 189.59)) * 0.275 - 869.36

salarioLiquido = salarioBruto - outrosDesc - inss - irrf

print("\nSalário bruto = R$ %.2f"%salarioBruto)
print("INSS = R$ %.2f"%inss)
print("IRRF = R$ %.2f"%irrf)
print("Outros descontos = R$ %.2f"%outrosDesc)
print("Salário líquido = R$ %.2f"%salarioLiquido)