from tabulate import tabulate
import pandas as pd
def analisa():
    dados = []
    listaFinal = []
    url = ['C:/Users/40413844/Documents/aquaTrivy/redis505.xlsx', 'C:/Users/40413844/Documents/aquaTrivy/redis505Anchore.xlsx', 'C:/Users/40413844/Documents/aquaTrivy/redis505Clair.xlsx']
    cont = False
    caminhoFinal = 'C:/Users/40413844/Documents/aquaTrivy/results/teste.txt'
    #caminhoFinal += saida[j]
    arquivo1 = pd.read_excel(url[0])
    arquivo2 = pd.read_excel(url[1])
    arquivo3 = pd.read_excel(url[2])
    for j in range(0, len(arquivo1)):
        var1 = arquivo1['CVE'] [j]
        nivel1 = arquivo1['Nivel'] [j]
        for i in range(0, len(arquivo2)):
            var2 = arquivo2['CVE'] [i]
            nivel2 = arquivo2['Nivel'] [i]
            if cont == True:
                    cont = False
                    break
            for y in range(0, len(arquivo3)):
                var3 = arquivo3['CVE'] [y]
                nivel3 = arquivo3['Nivel'] [y]
                if(var1.strip() == var2.strip() and var3.strip() == var1.strip()):
                    dados.append(var1.strip())
                    dados.append(nivel1.strip())
                    dados.append(nivel2.strip())
                    dados.append(nivel3.strip())
                    listaFinal.append(dados[:])
                    dados.clear()
                    cont=True
                    break
    data= tabulate(listaFinal, headers=['CVE', 'Trivy','Anchore', 'Clair'], tablefmt ='orgtbl')
    print(data)
    #escrever = open(caminhoFinal, 'w')
    #escrever.write(data)
    #escrever.close()           
analisa()
