from random import Random, random
import time

def current_time_millis():
    return round(time.time()*1000)

before = current_time_millis()
a = 0
for i in range(1,1000000):
    a += i
after = current_time_millis()
print("Addition")
print(after-before)

#Multplication logic
import random
b=1
before = current_time_millis()
for i in range(1,1000): 
    b *= random.randint(1,10)
after = current_time_millis()
print("Multplication")
print(after - before)

#Division Logic
before = current_time_millis()
for i in range(1,1000000): 
    c = random.randint(1,1000)/2
after = current_time_millis()
print("Division")
print(after - before)

