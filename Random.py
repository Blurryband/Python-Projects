import time
import random
numbers = []
length = raw_input("PLZ Enter A Number.")

for n in range(int(length)):
    x = random.randint(1,26)
    numbers.append(x)


print "Thanks"

print numbers

print "Look At what I Did"

time.sleep(20)
