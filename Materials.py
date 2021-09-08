class Materials:

    def __init__(self, quantity=0, item=""):

        self.quantity = quantity
        self.item = item
        self.next = None

    def insert(self, quantity, item):
        if self.item == item:
            self.quantity += quantity
        #elif self.quantity == None:
        #     self.quantity = quantity
        #     self.item = item
        elif self.next == None:
            self.next = Materials(quantity, item)
        else:
            self.next.insert(quantity, item)
    # Print the tree

    def Print(self):
        print(self.quantity,",", self.item)
        if self.next != None:
            self.next.Print()


def test():
    MM = Materials(1, "자작나무")
    MM.insert(2, "느릅나무")
    MM.insert(2, "느릅나무")
    MM.insert(1, "자작나무")
    MM.Print()
