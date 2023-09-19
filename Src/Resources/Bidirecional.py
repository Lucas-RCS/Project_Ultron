from Src.Models.List import List
from Src.Util.HexagonalCartesian import adjacent_coords, has_in_ambient

class Bidirecional(object):
    
    def __init__(self, ambient, beginning, destination):
        self.ambient = ambient
        self.beginning = beginning
        self.destination = destination

    # BUSCA EM AMPLITUDE
    def make(self):

        inicio = self.beginning
        fim = self.destination

        # Primeiro Amplitude"
        # Manipular a FILA para a busca
        l1 = List()
        # cópia para apresentar o caminho (somente inserção)
        l2 = List()
        
        # Segundo Amplitude"
        # Manipular a FILA para a busca
        l3 = List()
        # cópia para apresentar o caminho (somente inserção)
        l4 = List()
    
        # insere ponto inicial como nó raiz da árvore
        l1.push(inicio,0,None)
        l2.push(inicio,0,None)
        
        l3.push(fim,0,None)
        l4.push(fim,0,None)
    
    
        # controle de nós visitados
        visitado1 = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado1.append(linha)
        
        visitado2 = []
        linha = []
        linha.append(fim)
        linha.append(0)
        visitado2.append(linha)
        
        ni = 0
        while l1.empty()==False or l3.empty()==False:
            
            while l1.empty() == False:
                
                # para ir para o próximo amplitude
                if ni!=l1.first().level:
                    break
                    
                # remove o primeiro da fila
                atual = l1.shift()
        
                adjacents = adjacent_coords(atual.coord)

                # varre todos as conexões dentro do grafo a partir de atual
                for coord in adjacents:

                    if has_in_ambient(coord, self.ambient):
        
                        # pressuponho que não foi visitado
                        flag = True
            
                        # controle de nós repetidos
                        for j in range(len(visitado1)):
                            if visitado1[j][0]==coord:
                                if visitado1[j][1]<=(atual.level+1):
                                    flag = False
                                else:
                                    visitado1[j][1]=atual.level+1
                                break
                        
                        # se não foi visitado inclui na fila
                        if flag:
                            l1.push(coord, atual.level + 1, atual)
                            l2.push(coord, atual.level + 1, atual)
            
                            # marca como visitado
                            linha = []
                            linha.append(coord)
                            linha.append(atual.level+1)
                            visitado1.append(linha)
            
                            # verifica se é o objetivo
                            flag = False
                            for j in range(len(visitado2)):
                                if visitado2[j][0]==coord:
                                    flag = True
                                    break
                            
                            if flag:
                                caminho = []
                                caminho += l2.getPath()
                                caminho += l4.getPathBI(coord)
                                return caminho
                        
            while l3.empty() == False:
                
                # para ir para o próximo amplitude
                if ni!= l3.first().level:
                    break
                
                # remove o primeiro da fila
                atual = l3.shift()
        
                adjacents = adjacent_coords(atual.coord)

                # varre todos as conexões dentro do grafo a partir de atual
                for coord in adjacents:

                    if has_in_ambient(coord, self.ambient):
        
                        # pressuponho que não foi visitado
                        flag = True
            
                        # controle de nós repetidos
                        for j in range(len(visitado2)):
                            if visitado2[j][0]==coord:
                                if visitado2[j][1]<=(atual.level+1):
                                    flag = False
                                else:
                                    visitado2[j][1]=atual.level+1
                                break
                            
                        # se não foi visitado inclui na fila
                        if flag:
                            l3.push(coord, atual.level + 1, atual)
                            l4.push(coord, atual.level + 1, atual)
            
                            # marca como visitado
                            linha = []
                            linha.append(coord)
                            linha.append(atual.level+1)
                            visitado2.append(linha)
            
                            # verifica se é o objetivo
                            flag = False
                            for j in range(len(visitado1)):
                                if visitado1[j][0]==coord:
                                    flag = True
                                    break
                                
                            if flag:
                                caminho = []
                                caminho += l4.getPath()
                                caminho += l2.getPathBI(coord)
                                return caminho[::-1]
                            
            ni += 1
    
        return "error"
