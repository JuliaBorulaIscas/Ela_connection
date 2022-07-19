from ela.bluetooth.advertising.TagBase import TagBase
import binascii

#@class Tag_Proxir P Proxir 000004

class TagDistance(TagBase):
    def __init__(self, payload):
        super().__init__(payload)
        self.formattedDataSensor = self.parsePayload(payload)
        
    def parsePayload(self, payload):
     
        parse = binascii.b2a_hex(self.payload[0:32]).decode('ascii')
        ##distance = int((parse[16:18] + parse[14:16]), 16)
        state = int(parse[16:18], 16)   
        count = int(parse[14:16], 16)
        result = ("state=" + str(state) + " count=" + str(count))
        #mm= int((parse[16:18] + parse[14:16]), 16)  
        #mm = int(parse[16:18], 16)   
        #mm= int(parse[14:16], 16)
        #result = str(mm)
        

        ## result = {
            # "distance": distance
            # }
        ##end of implement parsing
        return result
    