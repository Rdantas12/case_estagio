# Case 1
indice = 13 # Iniciando variáveis
soma = 0
k = 0

while k < indice:
    k = k +1
    soma += k
print(soma)
#saida: soma == 91


# Case 2
def fibonacci_check(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a+b
        return b == num
numero = int(input('Digite um número para a checagem: '))

if fibonacci_check(numero):
    print(f'O número {numero} pertence à sequência de Fibonacci.')
else:
    print(f'O numero {numero} não pertence à sequência de Fibonacci.')

# Case 3

import pandas as pd
import openpyxl

def analise_faturamento(excel):
    df = pd.read_excel(excel)
    df['valor'] = pd.to_numeric(df['valor'])
    
    menor_valor = df['valor'].min()
    maior_valor = df['valor'].max()
    media_valor = df['valor'].mean()
    dias_acima_medio = (df['valor'] > media).sum()
    resultados = pd.DataFrame({'Estatística':['Menor valor', 'Maior valor', 'Dais acima da média'], 
                                'Valor':[menor_valor, maior_valor, dias_acima_medio]})
    
    with pd.ExcelWriter('resultados.xlsx') as writer:
        resultados.to_excel(writer, index=False)
        return resultados

# Exemplos de uso
arquivo_excel = 'faturamento.xlsx'
analise_faturamento(arquivo_excel)


# Case 4
def percentual_faturamento(fat_por_estado):
    faturamento_total = sum(fat_por_estado.values())
    percentuais = {}
    for estado, valor in fat_por_estado.items():
        percentual = (valor / faturamento_total) * 100
        percentuais[estado] = f'{percentual:.2f}%'
        return percentuais

    
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53}

resultados =  percentual_faturamento(faturamento)

for estado, percentual in resultados.items():
    print(f'{estado}: {percentual}')

# Case 5

def inverter_string(texto):
    texto_invertido = ""
    for i in range(len(texto) - 1, -1, -1):
        texto_invertido += texto[i]
    return texto_invertido

texto = input("Digite a string que você deseja inverter: ")
resultado = inverter_string(texto)
print("A string invertida é:", resultado)