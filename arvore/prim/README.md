# Prim (MST)

O algoritmo de Prim é um algoritmo guloso empregado para encontrar uma árvore geradora mínima de um grafo conectado, valorado e não direcionado. A sua implementação foi desenvolvida com base no roteiro de aula da Universidade Federal de São João del-Rei (UFSJ). Para a construção da estrutura do vértice, foi utilizada a biblioteca `networkx`. 

O arquivo `main.py` possui tanto a lógica do algoritmo quanto o menu de execução. O arquivo `grafos.txt` possui 02 exemplos diferentes de grafos, sendo possível adicionar mais caso desejado.

**Como adicionar um grafo personalizado:**
Coloque o nome do novo grafo entre colchetes (ex: `[Grafo Saboroso]`). Nas linhas seguintes, utilize a seguinte lógica para expressar as arestas: `vértice_origem vértice_destino peso`. Cada linha deve representar apenas uma única ligação.


## Instruções de Execução

Para iniciar o algoritmo de Prim:
1. É necessário ter Python 3 e a biblioteca `networkx` instalados.
2. Abra o seu terminal na pasta do projeto.
3. Digite o comando abaixo e pressione Enter:
   ```bash
   python3 main.py
   ```


### Exemplo de Saída

```text

Grafos disponíveis no arquivo "grafos.txt":
1. [Exemplo de Aula]
2. [Grafo 01]

Digite o número do grafo desejado: 2

----- RESULTADOS -----

Custo total: 16
-----------------------
1 <----> 3 | Custo: 1
1 <----> 2 | Custo: 10
3 <----> 4 | Custo: 2
4 <----> 5 | Custo: 3
-----------------------

```
