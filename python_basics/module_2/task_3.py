class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, elem):
        if elem <= 0:
            raise NonPositiveError
        else:
            super().append(elem)


l = PositiveList()
l.append(1)
print(l)
l.append(-1)
