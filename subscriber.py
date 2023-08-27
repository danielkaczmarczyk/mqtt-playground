import time
import paho.mqtt.client as mqtt


def on_message(client, userdata, message):
    start_time = time.time()
    print(f"{client}, {userdata}")
    print(f"Received message on topic '{message.topic}': {message.payload.decode()}")
    end_time = time.time()
    elapsed_time = end_time - start_time
    with open('subscriber_timings.txt', 'a') as file:
        file.write(f"{elapsed_time}\n")

client = mqtt.Client()

client.on_message = on_message

broker_address = "localhost"
client.connect(broker_address, 1883)

topic = "sensors/temperature"
client.subscribe(topic)

client.loop_forever()

