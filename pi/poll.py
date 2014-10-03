import requests
import time
import json
import RPIO

RPIO.setup(17,RPIO.OUT)
RPIO.output(17, True)

time.sleep(1)

for x in range(1,100):
	try:
		pass
		r = requests.get('http://192.168.1.12:8001/state')
	except:
		print('could not reach host')					
	else:
		#d = json.loads(r.text)
		print(r.text)
		if r.text == 'On':
			RPIO.output(17, True)
		else:
			RPIO.output(17, False)
	time.sleep(1)
RPIO.cleanup()
