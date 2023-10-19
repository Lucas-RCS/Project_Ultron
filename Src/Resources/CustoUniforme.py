from Src.Models.List import List
from Src.Util.HexagonalCartesian import adjacent_coords, has_in_ambient, get_price

class CustoUniforme(object):
    
    def __init__(self, ambient, weights, beginning, destination):
        self.ambient = ambient
        self.weights = weights
        self.beginning = beginning
        self.destination = destination

    def make(self):

        l1 = List()
        l2 = List()
        visitado = []
        
        l1.insereUltimo(self.beginning,0,0,None)
        l2.insereUltimo(self.beginning,0,0,None)
        linha = []
        linha.append(self.beginning)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            
            if atual.estado == self.destination:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                return [caminho, atual.valor2]
        
            adjacents = adjacent_coords(atual.estado)

            for novo in adjacents:

                if has_in_ambient(novo, self.ambient):
                    # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                    v2 = atual.valor2 + get_price(novo, self.ambient, self.weights) # custo do caminho
                    v1 = v2 # f1(n)

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
                        l1.inserePos_X(novo, v1, v2, atual)
                        l2.inserePos_X(novo, v1, v2, atual)
                        if flag2:
                            linha = []
                            linha.append(novo)
                            linha.append(v2)
                            visitado.append(linha)
                    
        return "error"
