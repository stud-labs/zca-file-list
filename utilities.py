from components import FileCollection
from interfaces import IFileCollection
from zope.component import getSiteManager

def register_utilities():
    gsm  = getSiteManager()
    coll = FileCollection()
    gsm.registerUtility(coll, name="default")
