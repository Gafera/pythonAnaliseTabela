import pandas as pd

def analisa(entrada, saida, quantidade):
    url1 = 'C:/Users/Gabriel de Freitas/Documents/analises/repositorios/'
    caminhoFinal = 'C:/Users/Gabriel de Freitas/Downloads/'    
    for j in range(0, quantidade):
        url1 = url1 + entrada[j]
        caminhoFinal = caminhoFinal + saida[j]
        arquivo1 = pd.read_excel(url1)
        data = arquivo1['CVE'].value_counts()
        escrever = pd.ExcelWriter(caminhoFinal)
        data.to_excel(escrever, 'aba', index=True)
        escrever.save()
    
saida =[]
entrada = []
quantidade = int(input("Digite quantas arquivos serão analisados: "))
for i in range(0, quantidade):
    entrada.append(str(input("Digite o nome do arquivo a ser analisado: ")))
    saida.append(str(input("Digite um nome para essa análise: ")))
analisa(entrada, saida, quantidade)
    
    
    
