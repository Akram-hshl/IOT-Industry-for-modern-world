
import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

ssid = 'aeshotspot' #'UPCBF3B25D'
password = 'aesgroupC24' #'Jmhpsapyv23j'
mqtt_server = '192.168.0.59' #
mqtt_user = ''
mqtt_pass = ''

#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.144'
client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'bin/updates'
topic_pub = b'bin/updates'

last_message = 0
message_interval = 5
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
