
import matplotlib.pyplot as plt

dados = open('CORONA1.csv').readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(';')
        x.append(str(linha[1]))
        y.append(str(linha[0]))
        
plt.stem(y,x)

plt.title('Faixa etária de pessoas atingida pelo COVID-19 na região proximo a Frutal-MG ate 24/06/2020\nFonte:"http://coronavirus.saude.mg.gov.br/painel"')
plt.suptitle('COVID-19')
plt.xlabel('Idades')
plt.ylabel('Cidades')

plt.show()





