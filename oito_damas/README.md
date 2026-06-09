# Problema das Oito Damas

O problema consiste em dispor oito damas em um tabuleiro de xadrez de dimensão 8x8, de forma que nenhuma delas seja atacada por outra. Portanto, é preciso que nenhuma das oito damas esteja em uma mesma linha, coluna, ou diagonal.

## Solução 

A lógica do algoritmo implementado consiste no esforço de tentativa e erro bruta. O processo inicia posicionando uma dama na primeira coluna de uma linha. Se nesta posição, a dama não for atacada por nenhuma outra já posicionada, o algoritmo avança para a próxima linha repetindo o mesmo processo. Caso contrário, a dama é movida para a próxima coluna. Se todas as colunas de uma linha forem testadas e nenhuma posição segura for encontrada, o algoritmo retrocede uma linha, trocando a posição da última dama posicionada.

## Instruções de Execução

1. É necessário ter Python 3 e a biblioteca `networkx` instalados.
2. Foi utilizado o arquivo "Tabuleiro_com_Incompatibilidades.gml" como dados do grafo.
3. Abra o seu terminal na pasta do projeto.
4. Digite o comando abaixo e pressione Enter:
   ```bash
   python3 main.py
   ```

### Exemplo de Saída

```text

=========== RESULTADO ===========

[♛] [ ] [ ] [ ] [ ] [ ] [ ] [ ] 
[ ] [ ] [ ] [ ] [♛] [ ] [ ] [ ] 
[ ] [ ] [ ] [ ] [ ] [ ] [ ] [♛] 
[ ] [ ] [ ] [ ] [ ] [♛] [ ] [ ] 
[ ] [ ] [♛] [ ] [ ] [ ] [ ] [ ] 
[ ] [ ] [ ] [ ] [ ] [ ] [♛] [ ] 
[ ] [♛] [ ] [ ] [ ] [ ] [ ] [ ] 
[ ] [ ] [ ] [♛] [ ] [ ] [ ] [ ] 

```