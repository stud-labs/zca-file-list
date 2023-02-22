from components import File, FileCollection
from utilities import register_utilities
from registries import register_adapters
from zope.component import getUtility
from interfaces import IFileCollection

class Application:
    def __init__(self):
        c = self.collection = getUtility(IFileCollection,
                                         "default")
        # FileCollection()
        # f1 = File("passwd.txt", 1350)
        c.add(File("passwd.txt", 1350))
        c.add(File("exports", 355))

    def print(self):
        for o in self.collection.list:
            print(o)


if __name__ == '__main__':
    register_adapters()
    register_utilities()
    a = Application()
    a.print()
