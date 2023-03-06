import datetime
import time
import random

timestamp = 1678208220
timestamp1 = 1678208220 + 15150
timestamp2 = 1678208220 + 21500 # 5000
timestamp3 = 1678208220 + 40320 # 5000
random_number = random.choice([15150, 21500, 40320])
date = datetime.datetime.fromtimestamp(timestamp)
date1 = datetime.datetime.fromtimestamp(timestamp1)
date2 = datetime.datetime.fromtimestamp(timestamp2)
date3 = datetime.datetime.fromtimestamp(timestamp3)

unix_now_time = int(time.time())

print(date)
print(str(date1) + ' +6000')
print(str(date2) + ' +12000')
print(date3)

# result = 1678208220 + random_number
print(str('fffff ') + str(datetime.datetime.fromtimestamp(1678154526)))

aaaa = int(time.time()) + random.choice([15150, 21500, 40320])
print(aaaa)
