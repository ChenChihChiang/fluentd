import datetime

d1 = datetime.datetime.now()
d3 = d1 + datetime.timedelta(minutes=-5)
print (d3.ctime())

print (d3.date())
print (d3.time())
print (d3.isoformat())

print (d3.isoformat(), '%Y-%m-%dT%H:%M:%S')

print (d3.strftime("%Y-%m-%dT%H:%M:%S"))
