from interfaces import IFileCollection, IFile
from zope.interface import implementer, providedBy

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
        assert IFile.providedBy(obj)
        self._collection.append(obj)
        return obj

    def remove(self, obj):
        self._collection.remove(obj)
        return obj
