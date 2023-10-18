from Src.Models.List import List
from Src.Util.HexagonalCartesian import adjacent_coords, has_in_ambient

class CustoUniforme(object):
    
    def __init__(self, ambient, beginning, destination):
        self.ambient = ambient
        self.beginning = beginning
        self.destination = destination

    def search(self):

        search_list = List() # Manipular a fila para a busca
        copy_list = List() # Cópia para apresentar o caminho (somente inserção)

        search_list.push(self.beginning, 0, None) # Insere ponto inicial como nó raiz da árvore
        copy_list.push(self.beginning, 0, None)

        # Controle de nós visiteds
        visited = []
        line = [self.beginning, 0]
        visited.append(line)

        # Verifica se é o objetivo
        while not search_list.empty():
            current = search_list.shift()
            adjacents = adjacent_coords(current.coord) # Remove o primeiro da fila
            
            for coord in adjacents: # Varre todos as conexões dentro do grafo a partir de atual
                if has_in_ambient(coord, self.ambient):
                    flag = True # Pressupõe que não foi visitado
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

                        line = [coord, current.level + 1]
                        visited.append(line)

                        if coord == self.destination:
                            path = copy_list.getPath()
                            return path

        return "Caminho não encontrado"
