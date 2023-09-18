from Src.Models.Node import Node

class List(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def unshift(self, coord, level, father):
        new_node = Node(father, coord, level, None, None)

        if self.head == None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    # INSERE NO FIM DA LISTA
    def push(self, coord, level, father):

        new_node = Node(father, coord, level, None, None)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous   = self.tail
            self.tail = new_node

    # REMOVE NO INÍCIO DA LISTA
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

    # REMOVE NO FIM DA LISTA
    def pop(self):
        if self.tail is None:
            return None
        else:
            node = self.tail
            self.tail = self.tail.next
            if self.tail is not None:
                self.tail.previous = None
            else:
                self.head = None
            return node

    # RETORNA O PRIMEIRO DA LISTA
    def first(self):
        return self.head
    
    # RETORNA O ÚLTIMO DA LISTA
    def last(self):
        return self.tail

    # VERIFICA SE LISTA ESTÁ VAZIA
    def empty(self):
        if self.head is None:
            return True
        else:
            return False
        
    # EXIBE O CONTEÚDO DA LISTA
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
    
    # EXIBE O CAMINHO ENCONTRADO
    def getPath(self):
        
        atual = self.tail
        path = []
        
        while atual.father is not None:
            path.append(atual.coord)
            atual = atual.father
            
        path.append(atual.coord)
        path = path[::-1]
        return path
    
    # EXIBE O CAMINHO ENCONTRADO (BIDIRECIONAL)
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