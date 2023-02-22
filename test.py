from components import FileCollection, File
from interfaces import IFile, IFileCollection


class TestComponents:

    def test_test(self):
        pass

    def test_IFile_interface(self):
        o = File("a_file.txt", 10000)
        assert IFile.providedBy(o)

    def test_IFileCollection(self):
        c = FileCollection()
        assert IFileCollection.providedBy(c)

    def test_collection(self):
        c = FileCollection()
        f1 = File("one.txt", 900)
        f2 = File("two.txt", 9000)

        assert len(c.list) == 0
        a1 = c.add(f1)
        assert a1 is f1
        c.add(f2)

        assert len(c.list) == 2
        a = c.remove(f2)
        assert a is f2
        assert len(c.list) == 1


if __name__ == '__main__':
    import nose2
    nose2.main()
