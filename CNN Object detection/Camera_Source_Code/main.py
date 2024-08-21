from machine import Pin, PWM
import time

# Servo setup
servo_pin1 = Pin(2)  # D4
servo_pin2 = Pin(4)  # D2
servo_pin3 = Pin(5)  # D1

servo1 = PWM(servo_pin1, freq=50)
servo2 = PWM(servo_pin2, freq=50)
servo3 = PWM(servo_pin3, freq=50)

# Global flag to control servo movement
continue_movement = False

def set_angle(servo, angle):
    duty = int(((angle / 180) * 115) + 40)
    servo.duty(duty)

def move_servos():
    global continue_movement
    continue_movement = True
    for i in range(1):
        if not continue_movement:
            break
        
        # Servo 1
        set_angle(servo1, 0)
        print("Servo 1 moved to 0 degrees")
        time.sleep(1)
        if not continue_movement:
            break
        set_angle(servo1, 90)
        print("Servo 1 moved to 90 degrees")
        time.sleep(1)
        if not continue_movement:
            break
        set_angle(servo1, 180)
        print("Servo 1 moved to 180 degrees")
        time.sleep(1)
        if not continue_movement:
            break

        # Servo 2
        set_angle(servo2, 0)
        print("Servo 2 moved to 0 degrees")
        time.sleep(1)
        if not continue_movement:
            break
        set_angle(servo2, 90)
        print("Servo 2 moved to 90 degrees")
        time.sleep(1)
        if not continue_movement:
            break
        set_angle(servo2, 180)
        print("Servo 2 moved to 180 degrees")
        time.sleep(1)
        if not continue_movement:
            break

        # Servo 3
        set_angle(servo3, 0)
        print("Servo 3 moved to 0 degrees")
        time.sleep(1)
        if not continue_movement:
            break
        set_angle(servo3, 90)
        print("Servo 3 moved to 90 degrees")
        time.sleep(1)
        if not continue_movement:
            break
        set_angle(servo3, 180)
        print("Servo 3 moved to 180 degrees")
        time.sleep(1)

def stop_servos():
    global continue_movement
    continue_movement = False
    set_angle(servo1, 0)
    set_angle(servo2, 0)
    set_angle(servo3, 0)
    print("All servos stopped at 0 degrees")

def sub_cb(topic, msg):
    print((topic, msg))
    if topic == b'bin/updates':
        if msg == b'2':
            print('Starting servo movement')
            move_servos()
        elif msg == b'1':
            print('Stopping servos')
            stop_servos()

def connect_and_subscribe():
    global client_id, mqtt_server, topic_sub
    client = MQTTClient(client_id, mqtt_server, user=mqtt_user, password=mqtt_pass)
    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(topic_sub)
    print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
    return client

def restart_and_reconnect():
    print('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(10)
    machine.reset()

try:
    client = connect_and_subscribe()
except OSError as e:
    restart_and_reconnect()

while True:
    try:
        client.check_msg()
        if (time.time() - last_message) > message_interval:
            msg = b'Hello #%d' % counter
            client.publish(topic_pub, msg)
            last_message = time.time()
            counter += 1
    except OSError as e:
        restart_and_reconnect()
