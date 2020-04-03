import pandas as pd
url1 = 'caminhoArquivoUsadoParaAnalise'
arquivo1 = pd.read_excel(url1)

data = arquivo1['nivel'].value_counts()

escrever = pd.ExcelWriter('caminho')
data.to_excel(escrever , 'aba', index=False)
escrever.save()
