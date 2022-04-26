# IoT_Simulation
Turn the LED ON/OFF using Broker: Microcontroller ESP32 on Python (Wokwi Simulation + Hivemq Broker Client)

Run the simulation on Wokwi, publish on Broker and then see the LED turns ON/OFF

Project on Wokwi (Micropython on ESP32): https://wokwi.com/projects/329467649115292243

Broker -> option 1: Hivemq Broker Client: http://www.hivemq.com/demos/websocket-client/

Broker -> option 2: Install the app MQTT DASH on Google Play Store

Language: Portuguese

# - Option 1: Hivemq Broker website config
# Connection
- Host -> broker.mqttdashboard.com
- Port -> 8000
- KeepAlive -> 60
- Click on 'Connect'

# Publish
- Topic: sala306/led
- QoS: 0
- Message: Digit '1' to turn the LED on // Digit '0' to turn the LED off
- Click on 'Publish'

# Subscriptions - Add new Topic (Optional)
- Topic: sala306/led 
- QoS: 0
- Click on 'Subscribe'

Run the simulation on Wokwi, publish the message on Broker and then see on Wokwi project the LED turns ON/OFF

# - Option 2: App MQTT Dash on Smartphone
# Config Broker
- Click on button '+' (upper right corner of the screen)
- Name the broker
- Address: broker.hivemq.com
- Port: 1883
- Click on diskette button (upper right corner of the screen) to save

# Publish (Turn ON/OFF) LED
-  Click on Broker
-  Click on '+' button (upper right corner of the screen)
-  Choose type: 'Switch/Button'
-  Name: LED
-  Topic: sala306/led
- Click on diskette button (upper right corner of the screen) to save

Run the simulation on Wokwi, press the button and see on Wokwi project the LED turns ON/OFF
