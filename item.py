
class ITEM:
	def __init__(self, name="", materials={}):
		self.name=name
		self.materials = materials

	def insert(self, name, materials):
		self.name = name
		self.materials = materials
	
	def Print(self):
		print(self.name,",", self.materials)		


def test():
    MM = ITEM("자작나무", {"자작나무 원목":3})
    MM.insert("느릅나무", {"자작나무 원목":3})
    #MM.insert(2, "느릅나무")
    #MM.insert(1, "자작나무")
    MM.Print()

test()