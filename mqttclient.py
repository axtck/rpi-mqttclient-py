import paho.mqtt.client as mqtt
import time

# On connent callback. 
def on_connect(client, userdata, flags, rc):
    print(f'Connected with result code {str(rc)}.\n')

# On message callback.
def on_message(client, userdata, msg):
    print(f'Message\nTopic: {msg.topic}\nPayload: {str(msg.payload)}.\n')

# On publish callback.
def on_publish(client, obj, mid):
    print(f'On publish\nMessage ID: {str(mid)}.\n')

# On subscribe callback.
def on_subscribe(client, obj, mid, grated_qos):
    print(f'On subscribe:\nMessage ID: {str(mid)}\n')


# Create client.
client = mqtt.Client()

# Link callbacks.
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.on_subscribe = on_subscribe

# Personal client data.
mqtt_host = 'farmer.cloudmqtt.com'
mqtt_port = 14511
mqtt_user = 'itiwppsz'
mqtt_password = 'BkRYsnNyy_tk'

# Topic.
topic = '/io/ion'

# Set credentials.
client.username_pw_set(mqtt_user, mqtt_password)

# Connect.
client.connect(mqtt_host, mqtt_port, 60)

# Subscribe.
client.subscribe(topic)

rpi_gpio_1 = 5

# Start loop.
client.loop_start()
# Loop.
while True:
    # gpiostatus = rpi_gpio_1.read() # Change with function to read pin status
    # client.publish(topic, gpiostatus)
    time.sleep(10)
client.loop_stop()
client.disconnect()