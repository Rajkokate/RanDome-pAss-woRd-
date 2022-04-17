#Personal Password Generator
import random
import string
lower="rajdattnarendrakokate"
upper="RAJDATTNARENDRAKOKATE"
numbers="1234567890"
symbols="[]{}()$&*"
all=lower+upper+numbers+symbols
length=16
password="".join(random.sample(all,length))
print(password)
