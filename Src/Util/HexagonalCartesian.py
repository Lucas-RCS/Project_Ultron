
def adjacent_coords(coord):
    coord = coord.split('-')
    
    x = int(coord[0])
    y = int(coord[1])

    coords = []

    if (y%2) == 0:
        coords.append("%s-%s" % (x, y))

        coords.append("%s-%s" % (x, y + 1))
        coords.append("%s-%s" % (x, y - 1))
        coords.append("%s-%s" % (x-1, y))

        coords.append("%s-%s" % (x + 1, y))
        coords.append("%s-%s" % (x + 1, y + 1))
        coords.append("%s-%s" % (x + 1, y - 1))
    else:
        coords.append("%s-%s" % (x, y))

        coords.append("%s-%s" % (x - 1, y))
        coords.append("%s-%s" % (x - 1, y - 1))
        coords.append("%s-%s" % (x - 1, y + 1))

        coords.append("%s-%s" % (x, y - 1))
        coords.append("%s-%s" % (x + 1, y))
        coords.append("%s-%s" % (x, y + 1))

    return coords 
    
