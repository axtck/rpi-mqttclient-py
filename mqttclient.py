import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
import json

# On connent callback. 
def on_connect(client, userdata, flags, rc):
    print(f'On connect, result code: {str(rc)}.\n')

# On message callback.
def on_message(client, userdata, msg):
    # Parse json to Python dict.
    command = json.loads(msg.payload)

    # Get pin and status value.
    pin = int(command['pin']) 
    status = command['status']

    # Call write_gpio to write pin.
    write_gpio(pin, status)

    print(f'On message\nTopic: {msg.topic}\nPayload: {str(msg.payload)}\n')

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
input_topic = 'io/in'
output_topic = 'io/out'

# Set credentials.
client.username_pw_set(mqtt_user, mqtt_password)

# Connect.
client.connect(mqtt_host, mqtt_port, 60)

# Subscribe.
client.subscribe(output_topic)



def write_gpio(pin, status):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pin, GPIO.OUT)
    if status == True:
        GPIO.output(pin, GPIO.HIGH)
    else:
        GPIO.output(pin, GPIO.LOW)

# GPIO setup.
def input_gpio_setup(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    # Declare as input.
    GPIO.setup(pin, GPIO.IN)

# Declare pin.
input_pin = 21
# Call setup.
input_gpio_setup(input_pin)

# Start loop.
client.loop_start()
# Loop.
while True:
    if GPIO.input(input_pin):
        client.publish(input_topic, 'HIGH')
    else:
        client.publish(input_topic, 'LOW')
    time.sleep(10)

# Disconnect.
client.loop_stop()
client.disconnect()