import network
import time
from umqtt.simple import MQTTClient
from machine import Pin

##################################################################################

# MQTT CONFIG
MQTT_BROKER    = "broker.hivemq.com"
MQTT_USER      = ""
MQTT_PASSWORD  = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC     = "sala306/led"
MQTT_PORT = 1883

################################################################################

# CONNECT WI-FI WOKWI-GUEST
def wifi_connect():
  print("Connecting", end="")

  sta_if = network.WLAN(network.STA_IF)
  sta_if.active(True)
  sta_if.connect('Wokwi-GUEST', '')

  while not sta_if.isconnected():
    print(".", end="")
    time.sleep(0.3)

  print(" Wi-Fi connected!")

################################################################################

# LED MESSAGE CONFIG
def message_arrived(topic, msg):
  if (msg == b'1'):
      led.value(1)
  if (msg == b'0'):
      led.value(0)

################################################################################

# SUBSCRIBER
def subscribe():
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=0)
 
    # Subscribed messages will be delivered to this callback
    client.set_callback(message_arrived)
    client.connect()
    client.subscribe(MQTT_TOPIC)
    print("Conected on %s, topic subscribed: %s " % (MQTT_BROKER, MQTT_TOPIC))
    return client

################################################################################

# MAIN PROGRAM
led = Pin(4, Pin.OUT)
led.value(0)

wifi_connect()
client = subscribe()

while True:
  client.wait_msg()
  #time.sleep(0.5)      # BLINK LED