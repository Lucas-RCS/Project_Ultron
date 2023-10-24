from Src.Util.HexagonalCartesian import adjacent_coords, has_in_ambient, get_price
from Src.Models.List import List

class AIAestrela: # Busca gulosa (o_o)

    # Construtor
    def __init__(self, ambient, weights, beginning, destination, H):
        self.ambient = ambient
        self.weights = weights
        self.beginning = beginning
        self.destination = destination
        self.H = H

    def make(self):
        ind_i = self.ambient.index(self.destination)
        ind_f = self.ambient.index(self.destination)

        limite = self.H[ind_i][ind_f]

        while True:
            lim_exc = []
            l1 = List()
            l2 = List()
            visitado = []
            
            l1.insereUltimo(self.beginning,0,0,None)
            l2.insereUltimo(self.beginning,0,0,None)
            linha = []
            linha.append(self.beginning)
            linha.append(0)
            visitado.append(linha)
            
            #print("Limite: ",limite)
            while l1.vazio() == False:
                atual = l1.deletaPrimeiro()
                
                if atual.estado == self.destination:
                    caminho = []
                    caminho = l2.exibeArvore2(atual.estado,atual.valor1)

                    return caminho[::-1]
            
                adjacents = adjacent_coords(atual.estado)

                for novo in adjacents:

                    if has_in_ambient(novo, self.ambient):
                    
                        ind1 = self.ambient.index(novo)
                        
                        # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                        v2 = atual.valor2 + get_price(novo, self.ambient, self.weights)  # custo do caminho
                        v1 = v2 + self.H[ind_f][ind1] # f2(n)
        
                        if v1<=limite:
                            flag1 = True
                            flag2 = True
                            for j in range(len(visitado)):
                                if visitado[j][0]==novo:
                                    if visitado[j][1]<=v2:
                                        flag1 = False
                                    else:
                                        visitado[j][1]=v2
                                        flag2 = False
                                    break
            
                            if flag1:
                                l1.inserePos_X(novo, v1 , v2, atual)
                                l2.inserePos_X(novo, v1, v2, atual)
                                if flag2:
                                    linha = []
                                    linha.append(novo)
                                    linha.append(v2)
                                    visitado.append(linha)
                        else:
                            lim_exc.append(v1)
                            
            limite = sum(lim_exc)/len(lim_exc)
                    
        return "Caminho não encontrado"