from Src.Models.List import List
from Src.Util.HexagonalCartesian import adjacent_coords

class Profundidade(object):
    
    def __init__(self, ambient, beginning, destination):
        self.ambient = ambient
        self.beginning = beginning
        self.destination = destination

    
    # BUSCA EM PROFUNDIDADE
    def make(self, limit = None):

        # manipular a FILA para a busca
        search_list = List()

        # cópia para apresentar o caminho (somente inserção)
        copy_list = List()

        # insere ponto inicial como nó raiz da árvore
        search_list.push(self.beginning,0,None)
        copy_list.push(self.beginning,0,None)

        # controle de nós visiteds
        visited = []
        line = []
        line.append(self.beginning)
        line.append(0)

        visited.append(line)

        while search_list.empty() == False:
            
            # remove o primeiro da fila
            current = search_list.pop()

            in_not_the_end = False

            if limit != None:
                if current.level < limit:
                    in_not_the_end = True

            if  in_not_the_end:
                adjacents = adjacent_coords(current.coord)

                # varre todos as conexões dentro do grafo a partir de atual
                for coord in adjacents:


                    if coord in self.ambient:

                        # pressuponho que não foi visitado
                        flag = True

                        # controle de nós repetidos
                        for j in range(len(visited)):
                            if visited[j][0]==coord:
                                if visited[j][1] <= (current.level + 1):
                                    flag = False
                                else:
                                    visited[j][1]= current.level + 1
                                break

                        
                        # se não foi visited inclui na fila
                        if flag:
                            search_list.push(coord, current.level + 1, current)
                            copy_list.push(coord, current.level + 1, current)

                            # marca como visited
                            line = []
                            line.append(coord)
                            line.append(current.level + 1)
                            visited.append(line)

                            # verifica se é o objetivo
                            if coord == self.destination:
                                path = []
                                path += copy_list.getPath()
                                
                                return path

        return "caminho não encontrado"
