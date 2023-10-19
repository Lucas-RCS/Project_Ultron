from Src.Models.Node import Node

class No(object):
    def __init__(self, pai=None, estado=None, valor1=None, 
                valor2=None, anterior=None, proximo=None):
        # controle da árvore de busca
        self.pai       = pai
        # indica o nó do grafo
        self.estado    = estado
        # função de avaliação f(n) do método
        self.valor1    = valor1        
        # custo do caminho da origem até o nó atual
        self.valor2    = valor2     
        # controle da lista encadeada
        self.anterior  = anterior
        self.proximo   = proximo

class List(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA (inserePrimeiro)
    def unshift(self, coord, level, father):
        new_node = Node(father, coord, level, None, None)

        if self.head == None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    # INSERE NO FIM DA LISTA (insereUltimo)
    def push(self, coord, level, father):

        new_node = Node(father, coord, level, None, None)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous   = self.tail
            self.tail = new_node

    # REMOVE NO INÍCIO DA LISTA (deletaPrimeiro)
    def shift(self):
        if self.head is None:
            return None
        else:
            node = self.head
            self.head = self.head.next
            if self.head is not None:
                self.head.previous = None
            else:
                self.tail = None
            return node

    # REMOVE NO FIM DA LISTA (deletaUltimo)
    def pop(self):
        if self.tail is None:
            return None
        else:
            node = self.tail
            self.tail = self.tail.previous
            if self.tail is not None:
                self.tail.next = None
            else:
                self.head = None
            return node

    # RETORNA O PRIMEIRO DA LISTA (primeiro)
    def first(self):
        return self.head
    
    # RETORNA O ÚLTIMO DA LISTA (ultimo)
    def last(self):
        return self.tail

    # VERIFICA SE LISTA ESTÁ VAZIA (vazio)
    def empty(self):
        if self.head is None:
            return True
        else:
            return False
        
    # EXIBE O CONTEÚDO DA LISTA (exibeLista)
    def getList(self):
        
        aux = self.head
        str = []
        while aux != None:
            temp = []
            temp.append(aux.coord)
            temp.append(aux.level)
            str.append(temp)
            aux = aux.next
        
        return str
    
    # EXIBE O CAMINHO ENCONTRADO (exibeCaminho)
    def getPath(self):
        
        atual = self.tail
        path = []
        
        while atual.father is not None:
            path.append(atual.coord)
            atual = atual.father
            
        path.append(atual.coord)
        path = path[::-1]
        return path
    
    # EXIBE O CAMINHO ENCONTRADO (BIDIRECIONAL) (exibeCaminho1)
    def getPathBI(self,value):
                
        current = self.head
        
        while current.coord != value:
            current = current.next
    
        path = []
        current = current.father
        while current.father is not None:
            path.append(current.coord)
            current = current.father
        path.append(current.coord)

        return path
    
  # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, s, v1, v2, p):
        novo_no = No(p, s, v1, v2, None, None)
        if self.head == None:
            self.tail = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
        self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, s, v1, v2, p):

        novo_no = No(p, s, v1, v2, None, None)

        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior   = self.tail
        self.tail = novo_no
    
    # INSERE NO FIM DA LISTA
    def inserePos_X(self, s, v1, v2, p):
        
        # se lista estiver vazia
        if self.head is None:
            self.inserePrimeiro(s,v1,v2,p)
        else:
            atual = self.head
            while atual.valor1 < v1:
                atual = atual.proximo
                if atual is None: break
            
            if atual == self.head:
                self.inserePrimeiro(s,v1,v2,p)
            else:
                if atual is None:
                    self.insereUltimo(s,v1,v2,p)
                else:
                    novo_no = No(p,s,v1,v2,None,None)
                    aux = atual.anterior
                    aux.proximo = novo_no
                    novo_no.anterior = aux
                    atual.anterior = novo_no
                    novo_no.proximo = atual


    # REMOVE NO INÍCIO DA LISTA
    def deletaPrimeiro(self):
        if self.head is None:
            return None
        else:
            no = self.head
            self.head = self.head.proximo
            if self.head is not None:
                self.head.anterior = None
            else:
                self.tail = None
            return no

    # REMOVE NO FIM DA LISTA
    def deletaUltimo(self):
        if self.tail is None:
            return None
        else:
            no = self.tail
            self.tail = self.tail.anterior
            if self.tail is not None:
                self.tail.proximo = None
            else:
                self.head = None
            return no

    def vazio(self):
        if self.head is None:
            return True
        else:
            return False
        
    def exibeLista(self):
        
        aux = self.head
        str = []
        while aux != None:
            linha = []
            linha.append(aux.estado)
            linha.append(aux.valor1)            
            str.append(linha)
            aux = aux.proximo
        
        return str
    
    def exibeArvore(self):
        
        atual = self.tail
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho
    
    def exibeArvore1(self,s):

        
        atual = self.head
        while atual.estado != s:
            atual = atual.proximo
    
        caminho = []
        atual = atual.pai
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho
    
    
    def exibeArvore2(self, s, v1):
        
        atual = self.tail
        
        while atual.estado != s or atual.valor1 != v1:
            atual = atual.anterior
        
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho
    
    
    def primeiro(self):
        return self.head
    
    def ultimo(self):
        return self.tail