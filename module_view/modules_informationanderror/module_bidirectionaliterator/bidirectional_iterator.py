##############################
#### CLASES DE ITERADORES ####
##############################

class bidirectional_iterator(object):
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def next(self):
        try:
            self.index += 1
            result = self.collection[self.index]
        except IndexError:
            self.index = 0
            return self.collection[0]
        return result

    def prev(self):
        self.index -= 1
        if self.index < 0:
            self.index = 0
            self.collection[0]
        return self.collection[self.index]

    def __iter__(self):
        return self
