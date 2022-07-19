from bluepy.btle import Scanner, DefaultDelegate  # skan

import TagTypeEnum
from ela.bluetooth.advertising.TagFactory import TagFactory
from ela.bluetooth.advertising.TagRHT import TagRHT
from ela.bluetooth.advertising.TagTemperature import TagTemperature
from ela.bluetooth.advertising.TagAng import TagAng
from ela.bluetooth.advertising.TagDistance import TagDistance
from ela.bluetooth.advertising.TagBase import TagBase
from TagTypeEnum import TagType
import json
import binascii
import paho.mqtt.client as mqtt

UUID_SERVICE_TEMPERATURE = "6e2a"
UUID_SERVICE_HUMIDITY = "6f2a"
UUID_SERVICE_MOV = "3f2a01"
UUID_SERVICE_ANG = "a12a"
UUID_SERVICE_DISTANCE = "5020"

BROKER = "127.0.0.1"
PORT = 1883
KEEPALIVE = 60

CONST_LOCAL_NAME = "Complete Local Name"
CONST_MAX_SCAN_TIME = 20
headers = [u'Timestamp', u'MacAddress', u'Address Type', u'LocalName', u'RSSI (dBm)', u'RawData']

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected successs")
    else:
        print("connected fail with code{rc}")


# def on_publish(client, userdata, result):
#     print("data published")



client = mqtt.Client()
client.on_connect = on_connect
client.connect(BROKER, PORT, KEEPALIVE)

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

# PĘTLA SKANOWANIE+JSON-------------------------------------------------------------------------------------------------
while True:
    scanner = Scanner().withDelegate(ScanDelegate())
    devices = scanner.scan(1)
    for dev in devices:
        if isinstance(dev.rawData, bytes):
            try:
                (tag, tag_type) = TagFactory.getInstance().getTag(dev.rawData)
                if tag_type is not TagType.OTHER:
                    print("\tDevice type %s @ %s (%s), RSSI=%d dB, Interpreted ELA Data=%s" % (
                         tag_type.name, dev.addr, dev.addrType, dev.rssi, tag.formattedDataSensor))
                    attributes = {
                        "RSSI": int(dev.rssi),
                        "name": str(tag_type.name),
                    }
                    attributes.update(tag.formattedDataSensor)
                    json_str = json.dumps(attributes)
                    print(json_str)
                    client.publish("mqtt/" + tag_type.name.lower(), json_str)
            except Exception as e:
                # to znaczy ze znalezione urzadzenie Bluetooth nie jest znanym czujnikiem ELA
                # print(e)
                pass
        for (adtype, desc, value) in dev.getScanData():
                if (desc == CONST_LOCAL_NAME):
                    print("  %s = %s" % (desc, value))
    # time.sleep(10)


# PĘTLA KONIEC---------------------------------------------------------------------------------------------------------


