# Algoritmo de PERT / CPM

 Program Evaluation and Review Technique é uma ferramenta utilizada em gerenciamento de projetos que identifica atividades interdependentes, durações e o "caminho crítico". A sua implementação foi desenvolvida com base no roteiro de aula da Universidade Federal de São João del-Rei (UFSJ). Para a construção da estrutura do vértice, foi utilizada a biblioteca `networkx`. 

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
4. Escolha o número do grafo desejado.


### Exemplo de Saída

```text
Lista de Grafos disponiveis no arquivo grafos.txt:
1. [Exemplo de Sala]
2. [Grafo 01]
Digite o número do grafo desejado: 2

=== Resultados ===

 Tempo máximo: 9
Vertice: 1
Tempo Cedo: 0
Tempo Tarde: 0

Vertice: 3
Tempo Cedo: 7
Tempo Tarde: 7

Vertice: 2
Tempo Cedo: 0
Tempo Tarde: 2

Vertice: 4
Tempo Cedo: 5
Tempo Tarde: 7

Vertice: 5
Tempo Cedo: 9
Tempo Tarde: 9

Caminho crítico:
1 -> 3 ->  5
```