from datetime import datetime, timedelta
from sys import stdout
from time import sleep
d=int(input())
tempo=timedelta(seconds=d)
'\n'
while (str(tempo) != '0:00:00'):
    stdout.write("\r%s" % tempo)
    stdout.flush()
    tempo = tempo - timedelta(seconds=1)
    sleep(1)
stdout.write("\r0:00:00")
stdout.flush()