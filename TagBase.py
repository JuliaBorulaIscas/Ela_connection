import binascii

##
# @class TagBase  
# @brief base class to intergrate all informations from ELA tags
class TagBase:
    """ tag base declaration to contain all information to parse ELA BLE frame """
    formattedDataSensor = "VOID"

    def __init__(self, payload):
        """ constructor / init """
        self.payload = payload
        
    def bin2decs(self, data):
        """bin2decs(data): Conversion chaîne binaire signée de longueur quelconque -> nombre entier signé"""
        return int(data,2)-(1<<len(data))
            
    def integer(self, data):
        if len(data) == 16 and data[0] == "1":
            data = data[1:len(data)]
            data = TagBase.bin2decs(self, data)
            return data
        elif len(data) == 16 and data[0:4] == "1111":
            data = data[4:len(data)]
            data = TagBase.bin2decs(self, data)
            return data
        else:
            data = int(data,2)
            data = data
            return data
