# Vigilância Urbana: Algoritmo Genético

Este projeto implementa um Algoritmo Genético (AG) em Python para resolver uma variação do problema clássico de Cobertura de Vértices (*Minimum Vertex Cover*). O objetivo é determinar a quantidade mínima de câmeras de segurança e suas localizações exatas para monitorar 100% das ruas de uma cidade.

O mapa utilizado como base de estudo é a topologia viária do município de São João del-Rei - MG, contendo 550 cruzamentos e modelado em formato grafo estruturado (`.gml`).

## Arquitetura da Solução

A otimização é dividida em duas fases principais:

* **Kernelização (Limpeza Base):** Antes da evolução, o grafo é submetido a uma fase de pré-processamento. Vértices que possuem apenas uma conexão são classificados como "esquinas sem saída". A regra fundamental determina que uma câmera seja sempre instalada na esquina adjacente a essas ruas sem saída, otimizando o raio de visão e evitando que um equipamento proteja exclusivamente uma única via. Essa estratégia reduz drasticamente a complexidade e o tamanho do problema antes de repassá-lo ao motor heurístico.
* **Motor Evolutivo:** Uma população de soluções é gerada e submetida a um processo de seleção natural iterativo.

## Parâmetros Genéticos

A simulação biológica foi calibrada com os seguintes hiperparâmetros e operadores:

* **Representação do DNA:** Permutação sem repetição dos nós (cruzamentos) do grafo.
* **Avaliação (Fitness):** Simulação de instalação de câmeras seguindo a ordem do DNA até que o grafo perca todas as arestas. O fitness é a contagem final de câmeras (buscando minimização).
* **Seleção:** Roleta Viciada (Roleta Proporcional) utilizando o peso inverso do fitness.
* **Crossover:** *Order Crossover* (Cruzamento de Ordem) com taxa de corte transversal de 40%, garantindo a integridade dos genes permutados.
* **Mutação:** *Swap Mutation* (Mutação por Troca) com 5% de taxa de ocorrência, invertendo duas posições cirúrgicas no DNA para injeção de variabilidade.
* **Elitismo:** Preservação contínua dos 2 melhores indivíduos para a próxima geração.

## Bateria de Testes e Relatórios

Durante a execução, o sistema exibe no terminal o progresso em tempo real indicando o teste atual e, ao final, reporta a duração do tempo total de execução do programa.

O sistema gera dois arquivos na saída:
* `tabela_de_resultados.txt`: Histórico numérico da performance de cada teste executado na bateria.
* `relatorio_cameras.txt`: Documento final contendo a configuração topológica do indivíduo mais hábil, listando quais ruas específicas são monitoradas por cada câmera.

## Instruções de Execução

Para iniciar o algoritmo:
1. É necessário ter Python 3 e a biblioteca `networkx` instalados.
2. Abra o seu terminal na pasta do projeto.
3. Digite o comando abaixo e pressione Enter:
   ```bash
   python3 main.py
   ```

## Considerações Finais 

Essa foi a primeira vez que desenvolvi esse tipo de algoritmo. Tenho certas incertezas quanto o tamanho da população e sobre a eficacia da mutação, uma vez que o DNA do indivíduo é muito extenso e em sua maioria são genes que não se manifestam. Por fim, não sei se de fato foi a melhor aplicação para esse tipo de algoritmo, porém fico feliz com o seu resultado. Meu recorde pessoal foi de 291 câmeras usadas.