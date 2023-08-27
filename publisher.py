import time
import paho.mqtt.client as mqtt

qos_levels = [0,1,2]

client = mqtt.Client()

broker_address = "localhost"
client.connect(broker_address, 1883)

topic = "sensors/temperature"
message = "22.5C"

def publish(client, topic, message, qos):
    client.publish(topic, message, qos)

n = 0

timings = [
        [],[],[]
        ]

for qos in qos_levels:
    while True:

        print(f"{qos=} {n=}")

        start_time = time.time()

        publish(client, topic, message, qos)

        end_time = time.time()

        # I think this is in seconds
        elapsed_time = end_time - start_time

        timings[qos - 1].append(elapsed_time)

        n += 1
        if n == 100:
            n = 0
            break

client.disconnect()

with open('publisher_timings.txt', "w") as f:
    for qos_timings in timings:
        for timing in qos_timings:
            f.write("str(timing)\n")

