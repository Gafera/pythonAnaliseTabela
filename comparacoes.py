from tabulate import tabulate
import pandas as pd
def analisa():
    dados = []
    listaFinal = []
    url1 = 'C:/Users/40413844/Documents/aquaTrivy/redis505Anchore.xlsx'
    url2 = 'C:/Users/40413844/Documents/aquaTrivy/redis505Clair.xlsx'
    caminhoFinal = 'C:/Users/40413844/Desktop/aquaTrivy/results/'
    #caminhoFinal += saida[j]
    arquivo1 = pd.read_excel(url1)
    arquivo2 = pd.read_excel(url2)
    for j in range(0, len(arquivo1)):
        var1 = arquivo1['CVE'] [j]
        nivel1 = arquivo1['Nivel'] [j]
        for i in range(0, len(arquivo2)):
            var2 = arquivo2['CVE'] [i]
            nivel2 = arquivo1['Nivel'] [i]
            if(var1.strip() == var2.strip()):
                dados.append(var1.strip())
                dados.append(nivel1.strip())
                dados.append(nivel2.strip())
                listaFinal.append(dados[:])
                dados.clear()
                
    print(tabulate(listaFinal, headers=['CVE', 'Anchore', 'Clair'], tablefmt ='orgtbl'))            
                
analisa()
