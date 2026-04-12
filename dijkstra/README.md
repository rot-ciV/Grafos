# Algoritmo de Dijkstra

O algoritmo de Dijkstra é um algoritmo de caminho mínimo usado em grafos. A sua implementação foi desenvolvida com base no roteiro de aula da Universidade Federal de São João del-Rei (UFSJ). Para a construção da estrutura do vértice, foi utilizada a biblioteca `networkx`. 

O arquivo `main.py` possui tanto a lógica do algoritmo quanto o menu de execução. O arquivo `grafos.txt` possui 03 exemplos diferentes de grafos, sendo possível adicionar mais caso desejado.

**Como adicionar um grafo personalizado:**
Coloque o nome do novo grafo entre colchetes (ex: `[Grafo Maneiro]`). Nas linhas seguintes, utilize a seguinte lógica para expressar as arestas: `vértice_origem vértice_destino peso`. Cada linha deve representar apenas uma única ligação.


## Instruções de Execução

Para iniciar o algoritmo de Dijkstra:
1. É necessário ter Python 3 e a biblioteca `networkx` instalados.
2. Abra o seu terminal na pasta do projeto.
3. Digite o comando abaixo e pressione Enter:
   ```bash
   python3 main.py
   ```

4. Escolha o número do grafo e o vértice de origem conforme solicitado pelo programa.


### Exemplo de Saída

Grafos disponíveis no arquivo "grafos.txt":
1. [Exemplo de Sala]
2. [Grafo 01]
3. [Grafo 02]
Digite o número do grafo desejado: 2
Qual será o vertice origem? 5

----- RESULTADOS -----

Informações do vértice 1:
Vértice inalcançável a partir da origem.

Informações do vértice 2:
Vértice inalcançável a partir da origem.

Informações do vértice 3:
Vértice inalcançável a partir da origem.

Informações do vértice 4:
Vértice inalcançável a partir da origem.

Informações do vértice 5:
Menor distância: 0
Rota: 5