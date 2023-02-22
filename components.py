from interfaces import IFileCollection, IFile, IImage
from zope.interface import implementer, providedBy
from zope.component import adapter


@implementer(IFile)
class File:

    def __init__(self, name, size):
        self._name = name
        self._size = size

    @property
    def size(self):
        return self._size

    @property
    def name(self):
        return self._name

    def __str__(self):
        return "File '{}' of size {}".format(
            self.name,
            self.size,
        )


@implementer(IFileCollection)
class FileCollection:

    def __init__(self):
        self._collection = []

    @property
    def list(self):
        return self._collection

    def add(self, obj):
        o = IFile(obj)  # WORD(i);  (unsigned int) i
        assert IFile.providedBy(o)
        self._collection.append(o)
        return obj

    def remove(self, obj):
        self._collection.remove(obj)
        return obj


@implementer(IImage)
class Image:

    def __init__(self, width, height, bpp=8):
        self.width = width
        self.height = height
        self.bpp = bpp

    def __str__(self):
        return "Image w={} h={} bpp={}".format(self.width, self.height,
                                               self.bpp)


@implementer(IFile)
@adapter(IImage)
class AdaperOfIImageToIFile:

    def __init__(self, context):
        self.context = context

    @property
    def name(self):
        c = self.context
        return "Image{}x{}@{}".format(c.width, c.height, c.bpp)

    @property
    def size(self):
        c = self.context
        return c.height * c.width * c.bpp / 8
