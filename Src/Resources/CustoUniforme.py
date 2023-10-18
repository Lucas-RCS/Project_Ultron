from Src.Models.List import List
from Src.Util.HexagonalCartesian import adjacent_coords, has_in_ambient

class CustoUniforme(object):
    
    def __init__(self, ambient, beginning, destination):
        self.ambient = ambient
        self.beginning = beginning
        self.destination = destination

    def search(self):

        search_list = List()
        copy_list = List()

        search_list.push(self.beginning, 0, None)
        copy_list.push(self.beginning, 0, None)

        visited = []
        line = [self.beginning, 0]
        visited.append(line)

        while not search_list.empty():
            current = search_list.shift()
            adjacents = adjacent_coords(current.coord)

            for coord in adjacents:
                if has_in_ambient(coord, self.ambient):
                    flag = True
                    for j in range(len(visited)):
                        if visited[j][0] == coord:
                            if visited[j][1] <= (current.level + 1):
                                flag = False
                            else:
                                visited[j][1] = current.level + 1
                            break

                    if flag:
                        search_list.push(coord, current.level + 1, current)
                        copy_list.push(coord, current.level + 1, current)

                        line = [coord, current.level + 1]
                        visited.append(line)

                        if coord == self.destination:
                            path = copy_list.getPath()
                            return path

        return "Caminho não encontrado"
