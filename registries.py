from components import AdaperOfIImageToIFile
from zope.component import getGlobalSiteManager

def register_adapters():
    gsm = getGlobalSiteManager()
    gsm.registerAdapter(AdaperOfIImageToIFile)
