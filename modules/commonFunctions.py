import configparser


import jsonpickle
import jsonpickle.ext.numpy
import demjson

jsonBackend = "demjson"
jsonpickle.ext.numpy.register_handlers()
jsonpickle.load_backend(jsonBackend,"encode","decode", ValueError)
jsonpickle.set_preferred_backend(jsonBackend)
jsonpickle.set_decoder_options(jsonBackend,decode_float=float)

def jsonDump(obj,file,compact=False,*args,**kargs):
    global jsonBackend
    jsonpickle.set_encoder_options(jsonBackend,compactly=compact,*args,**kargs)
    file.write(jsonpickle.encode(obj))
    
def jsonParse(s):
    return jsonpickle.decode(s)
    
def jsonLoad(filePath):
    f = open(filePath)
    return jsonParse(f.read())
    


def loadIniFile(filePath):
    config = configparser.ConfigParser()
    config.read(filePath)
    return config
        
