from Src.Util.HexagonalCartesian import adjacent_coords, has_in_ambient
from Src.Models.List import List

class GreedySearch: # Busca gulosa (o_o)

    # Construtor
    def __init__(self, ambient, beginning, destination):
        self.ambient = ambient
        self.beginning = beginning
        self.destination = destination

    def greedy(self): 
        # Manipular a fila para a busca
        search_list = List()
        copy_list = List()
        visited = []
            
        search_list.push(self.beginning, 0, None) # Insere ponto inicial como nó raiz da árvore
        copy_list.push(self.beginning, 0, None)

        visited.append([self.beginning, 0])

        while not search_list.empty(): # Verifica se é o objetivo
            current = search_list.shift()
            adjacents = adjacent_coords(current.coord)

            for coord in adjacents: # Varre todos as conexões dentro do grafo a partir de atual
                if has_in_ambient(coord, self.ambient):
                    flag = True
                    for j in range(len(visited)):
                        if visited[j][0] == coord:
                            if visited[j][1] <= (current.level + 1): # Se foi visitado, verifica se o nível é menor
                                flag = False
                            else:
                                visited[j][1] = current.level + 1 # Se foi visitado, atualiza o nível
                            break

                    if flag: # Se não foi visitado, inclui na fila
                        search_list.push(coord, current.level + 1, current)
                        copy_list.push(coord, current.level + 1, current)
                        visited.append([coord, current.level + 1])

                        if coord == self.destination: # Se é o objetivo, retorna o caminho
                            path = copy_list.getPath()
                            return path

        return "Caminho não encontrado"
