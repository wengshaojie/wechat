
import urllib
import urllib2,json
def getResultFromRobot(text,userid):   
    url='http://www.tuling123.com/openapi/api'
    value={"key": u"ef065a8120674119a005035f98df21d5","info":text,"userid":userid}
    request=urllib2.Request(url=url,headers={'Content-Type':'text/json'},data=json.dumps(value))
    res=urllib2.urlopen(request)
    result = json.loads(res.read()) 
    return result