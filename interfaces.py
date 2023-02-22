from zope.interface import Interface, implements, Attribute

# Scheme

class IFile(Interface):
    size = Attribute("The size of file") #, readonly=True)

    name = Attribute("Name of file") #, readonly=True)

class ICollection(Interface):

    list = Attribute("List of elements of collection") #,
                     # readonly=True)

    def add(obj):
        """Adds object `obj` to collection"""

    def remove(obj):
        """Remove object from collection if it exists"""


class IFileCollection(ICollection):
    pass
