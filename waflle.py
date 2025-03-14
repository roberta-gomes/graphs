# Waffle Charts
# Otima alternativa para o grafico de pizza. Porque mostra melhor a proporcionalidade
# Existe um biblioteca que monta o Waffle Chart: PyWaffle
# O Primeiro passo é instalar a biblioteca
# O segundo passo é importar a biblioteca para ser usada:

import matplotlib.pyplot as plt
from pywaffle import Waffle

# A seguir usar o seguinte código para gerar o gráfico:
# No caso eu quero que seja um quadrado do tamanho 10x10, ou seja tenha 100 quadradrinhos, para que no final gere a visualização do
# que no final seria 100%

# Criando um dicionario com os dados, aqui eu tenho somente 50, então eu tenho que preencher o restante como Outros para serem branco,
# já que quero que seja um waffle chart que vai de 0 a 100%.

dados = {
    'Palmeiras': 20,
    'Corinthians': 15,
    'São Paulo': 10,
    'Santos': 5
}


# Estou calculando a quantidade que tem nos dados, ou seja os 50 informados anteriormente
total = sum(dados.values())

# Adicionar a categoria "Outros" para preencher até 100 em branco

if total < 100:
    dados['Outros'] = 100 - total

fig = plt.figure(
    FigureClass=Waffle, # Qual tipo de gráfico que eu quero
    rows=10,  # Quantidade de linhas que eu quero no grafico
    columns=10, # quantidade de colunas que eu quero na coluna
    values=dados, # A base de dados que quero que seja lida.
    legend={'loc': 'upper left', 'bbox_to_anchor': (1.1, 1)}, # Local que quero que coloque a legenda
    title={'label': 'Para qual time de futebol você torce?', 'loc': 'left'}, # Local que quero que coloque o título da imagem
    figsize=(12, 10), # O tamanho que eu quero, lembre-se que se for criar um PDF depois, tenho que alterar para um tamanho que condiz com o PDF
    colors=["#4CAF50", "#F44336", "#2196F3", "#FFC107", "#E0E0E0"],  # Cores para cada categoria, incluindo branco para "Outros", na ordem do dicionario
)

fig.set_tight_layout(False)
plt.show()