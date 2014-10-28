import pymongo
import json
import random
import calendar
import datetime

client = pymongo.MongoClient()
db = client.dummy_database
collection = db.sensorData

data = {}
now = calendar.timegm(datetime.datetime.now().timetuple())*1000

dates = [now + (i-5000)*100000 for i in range(10000)]
delta1 = [random.randint(-1,1)/10 for i in range(10000)]
delta2 = [random.randint(-1,1)/10 for i in range(10000)]

for i in range(10000):
    collection.insert({
        'date':dates[i],
        'oxygen':round(sum(delta1[:i])*10)/10,
        'temperature':round(sum(delta2[:i])*10)/10
        })
#print(data['oxygen'])

