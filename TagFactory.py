from TagTypeEnum import TagType
from ela.bluetooth.advertising.TagBase import TagBase
from ela.bluetooth.advertising.TagDistance import TagDistance
from ela.bluetooth.advertising.TagRHT import TagRHT
from ela.bluetooth.advertising.TagTemperature import TagTemperature
from ela.bluetooth.advertising.TagAng import TagAng
import binascii

## 
# Constant declaration to decode Bluetooth Advertising payload
# For more information about the frame format, please consult our website 
UUID_SERVICE_TEMPERATURE = "6e2a"
UUID_SERVICE_HUMIDITY = "6f2a"
UUID_SERVICE_MOV = "3f2a01"
UUID_SERVICE_ANG = "a12a"
UUID_SERVICE_DISTANCE = "5020"


##
# @class Tagfactory 
# @brief tag factory to create tag object to decode data from Bluetooth advertising
class TagFactory:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if TagFactory.__instance == None:
            TagFactory()
        return TagFactory.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if TagFactory.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            TagFactory.__instance = self

    def getTag(self, payload):
        """ Getter on the target tag """
        if (isinstance(payload, bytes)):
            tempString = binascii.b2a_hex(payload).decode('ascii')
            # UUID START-------------------------------------------------------------------------------------------
            if ((UUID_SERVICE_HUMIDITY in tempString) and (UUID_SERVICE_TEMPERATURE in tempString)):
                print("Debug Tag RHT FOUND")
                tag = TagRHT(payload)
                tag_type = TagType.RHT
                print(tag_type)

            elif (UUID_SERVICE_TEMPERATURE in tempString):
                print("Debug Tag Temperature FOUND")
                tag = TagTemperature(payload)
                tag_type = TagType.TEMPERATURE
                print(tag_type)

            elif (UUID_SERVICE_ANG in tempString):
                print("Debug Tag Ang FOUND")
                tag = TagAng(payload)
                tag_type = TagType.ANG
                print(tag_type)

            elif (UUID_SERVICE_DISTANCE in tempString):
                print("Debug Tag Distance  FOUND")
                tag = TagDistance(payload)
                tag_type = TagType.DISTANCE

                print(tag_type)
            else:
                raise Exception("Unknown sensor")

            return (tag, tag_type)
        else:
            raise Exception("Invalid data")
            # UUID STOP--------------------------------------------------------------------------------------------
