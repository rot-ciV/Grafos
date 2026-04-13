import networkx as nx
import sys

grafo = nx.DiGraph()
grafos_disp = []

def logica_dijkstra(grafo_analisado, vertice_origem):

    # Grava a menor distância entre o vertice origem com o restante dos vértices
    dicio_distancia = {}
    # Grava o vértice predecessor (o passo anterior) na rota mais curta de cada destino
    dicio_rotas = {}

    # Utiliza a variável vertice para caminhar entre todos os vértices do grafo
    for vertice in grafo_analisado.nodes:
        
        # Preenche todo o "dicio_rotas" com vazio (Ainda não há rotas)
        dicio_rotas[vertice] = None
        
        #Se o vertice em questão for a origem, já sabemos qual é a distância: 0
        if vertice == vertice_origem:

            dicio_distancia[vertice] = 0
        
        #Se não for, devemos supor o pior
        else:

            dicio_distancia[vertice] = float('inf')

    
    nao_visitados = list(grafo_analisado.nodes)

    # Deve acontecer enquanto ainda há vertices para visitar
    while len(nao_visitados) > 0:

        vertice_atual = None
        menor_distancia = float('inf')

        # Busca o vértice com a menor distância que ainda não foi visitado
        for vertice in nao_visitados:

            # Se encontrar, define ele como vertice_atual e grava sua distância
            if dicio_distancia[vertice] < menor_distancia:

                menor_distancia = dicio_distancia[vertice]
                vertice_atual = vertice

        # Condição de segurança: se os vértices restantes são inalcançáveis, deve-se encerra a busca
        if vertice_atual == None:
            break
        
        # Remove o vertice_atual da lista de nao_visitados
        nao_visitados.remove(vertice_atual)

        # Passa por cada vértice diretamente conectado com o vértice_atual
        for vizinho in grafo_analisado.neighbors(vertice_atual):

            # Atribuí o peso do caminho entre o vertice_atual com o vizinho em "distância"
            distancia = grafo_analisado[vertice_atual][vizinho]['weight']

            # Se a distância gravada no dicionario for maior que o caminho entre vertice_atual e o vizinho
            if dicio_distancia[vizinho] > dicio_distancia[vertice_atual] + distancia:
                
                # Troca a distância no dicionário pelo atual
                dicio_distancia[vizinho] = dicio_distancia[vertice_atual] + distancia

                # Define o vertice_atual como o predecessor (passo anterior) na rota para o vizinho
                dicio_rotas[vizinho] = vertice_atual

    return dicio_distancia, dicio_rotas

#Abre o arquivo grafos.txt em modo leitura e cria a variavel arquivo
with open('grafos.txt', 'r') as arquivo:

    for linha in arquivo:

        #transforma a String "linha" em uma nova sem quebra de linha e depois atribuí a linha_simples
        linha_simples = linha.strip()
        
        #Se a linha começar com "[" e termina com "] adiciona ela em grafos_disp 
        if linha_simples.startswith('[') and linha_simples.endswith(']'):

            grafos_disp.append(linha_simples)
            

# Caso não haja nenhum grafo para analisar, o programa fecha
if len(grafos_disp) == 0:

    sys.exit(('Nenhum grafo foi encontrado.'))


print('Grafos disponíveis no arquivo "grafos.txt":')

# O enumerate pega a lista de grafos e retorna o indice e o nome do grafo
for indice, nome in enumerate(grafos_disp):
    
    print(f'{indice + 1}. {nome}')    


while True:
    
    # Se o usuario digitar um inteiro e for válido, o loop é quebrado
    try:
        num_grafo = int(input('Digite o número do grafo desejado: '))

        if num_grafo <= 0 or num_grafo > len(grafos_disp):
            print('Opção inválida')
    
        else:
            break
    
    # Se o usuário escrever algo que não seja um inteiro, printa um aviso e recomeça um loop
    # "except ValueError" faz com que o programa não feche 
    except ValueError:
        print('Opção inválida')

grafo_escolhido = grafos_disp[num_grafo - 1]
lendo_alvo = False

# Lógica para ler o grafo requisitado
with open('grafos.txt', 'r') as arquivo:

    for linha in arquivo:

        linha_simples = linha.strip()
        
        # Pula linha vazia
        if not linha_simples:
            continue
        
        # Se a linha é um titulo
        if linha_simples.startswith('[') and linha_simples.endswith(']'):

            # E esse for o grafo requisitado
            if linha_simples == grafo_escolhido:
                # Aciona a flag
                lendo_alvo = True
                continue
            
            # Caso contrário abaixa a flag
            else:

                lendo_alvo = False
                continue
        
        # Se a flag estiver acionada, guarde as informações do grafo
        if lendo_alvo:

            origem, destino, peso = linha.split()
            grafo.add_edge(int(origem), int(destino), weight = int(peso))


vertice_origem = int(input('Qual será o vertice origem? '))

dicio_distancia, dicio_rotas = logica_dijkstra(grafo, vertice_origem)

print('\n----- RESULTADOS -----\n')

for destino in grafo.nodes:

    print(f'Informações do vértice {destino}:')

    if dicio_distancia[destino] == float('inf'):
        print('Vértice inalcançável a partir da origem.\n')
        continue

    print(f'Menor distância: {dicio_distancia[destino]}')
    print('Rota: ', end='')
    caminho = destino
    rota = []

    # Começa no destino final e termina no início
    while caminho != vertice_origem:

        # Adiciona o vertice atual em caminho
        rota.append(caminho)
        # Caminho agora é o predecessor dele
        caminho = dicio_rotas[caminho]

    rota.append(vertice_origem)
    # Como adicionamos o final da rota primeiro, é preciso inverter a lista
    rota.reverse()

    for resultado in rota:

        if resultado == destino:

            print(f'{resultado}\n')

        else:

            print(f'{resultado} -> ',end='')