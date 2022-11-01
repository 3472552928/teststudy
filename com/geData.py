from com.redTxtconfig import getini
from com.redTxtconfig import getTxt
def getHost():
    host = getini(name="\conf\data.ini",section="HOST",option="host")
    return host