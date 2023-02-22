from components import FileCollection, File, Image
from interfaces import IFile, IFileCollection, IImage
from registries import register_adapters
from utilities import register_utilities

register_adapters()
register_utilities()

class TestComponents:

    def setup_method(self):
        self.coll = FileCollection()

    def teardown_method(self):
        del self.coll

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

    def test_test_setup(self):
        assert self.coll is not None

    def test_IImage(self):
        i = Image(100, 50)
        IImage.providedBy(i)
        IImage.implementedBy(Image)

    def test_adapt_IImage_to_IFile(self):
        i = Image(100, 50)
        o = IFile(i)
        assert IFile.providedBy(o)

    def test_Add_Image_to_collection(self):
        c = self.coll
        i = Image(100, 50)
        c.add(i)
        assert len(c.list) == 1



if __name__ == '__main__':
    import nose2
    nose2.main()
