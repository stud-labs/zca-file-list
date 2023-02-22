from components import File, FileCollection


class Application:
    def __init__(self):
        c = self.collection = FileCollection()
        # f1 = File("passwd.txt", 1350)
        c.add(File("passwd.txt", 1350))
        c.add(File("exports", 355))

    def print(self):
        for o in self.collection.list():
            print(o)


if __name__ == '__main__':
    a = Application()
    a.print()
