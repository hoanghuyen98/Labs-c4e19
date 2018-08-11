def is_inside(point = [], rect = []):
    if (point[0] >= rect[0]) and (point[0] <= rect[0] + rect[2]):
        if (point[1] >= rect[1]) and (point[1] <= rect[1] + rect[3] ):
            return True
    else:
        return False