
class Array:
    def __init__(self, size):
        self.add = []
        self.size = size
        self.__add_to_list()


    def __setitem__(self, index, value):
        self.add[index] = value

    def __getitem__(self, index):
        return self.add[index]

    def __len__(self):
        return self.size

    def __add_to_list(self):
        for num in range(self.size):
            self.add.append(0)

    def __str__(self):
        return str(self.add)