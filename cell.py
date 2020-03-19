from direction import Direction

class Cell:
    def __init__(self, row, col):
        self._row = row
        self._col = col
        self._neighbors = {}
        self._links = []
    
    @property
    def row(self):
        """Returns cell's row."""
        return self._row

    @property
    def col(self):
        """Returns cell's col."""
        return self._col

    @property
    def neighbors(self):
        result = []
        for key in self._neighbors:
            if self._neighbors[key] is not None:
                result.append(self._neighbors[key])
        return result
    
    @property
    def north(self):
        return self._neighbors[Direction.north]

    @property
    def south(self):
        return self._neighbors[Direction.south]

    @property
    def east(self):
        return self._neighbors[Direction.east]

    @property
    def west(self):
        return self._neighbors[Direction.west]

    @property
    def links(self):
        return self._links
        
    def add_neighbor(self, direction, other):
        self._neighbors[direction] = other
    
    def link(self, other, bidir = True):
        self._links.append(other)
        if bidir:
            Cell.link(other, self, False)
    
    def unlink(self, other, bidir = True):
        self._links.remove(other)
        if bidir:
            Cell.unlink(other, self, False)

    def linked(self, other):
        return other in self._links
    
    def __str__(self):
        return 'Cell({}, {})'.format(self._row, self._col)
    
    def __repr__(self):
        return 'Cell({}, {})'.format(self._row, self._col)