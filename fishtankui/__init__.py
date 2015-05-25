import pymongo
import os
import logging
import argparse

dbMapping = {
	'PROD': 'fishtank',
	'TEST': 'test_fishtank',
	'DEV': 'dev_fishtank'
}

parser = argparse.ArgumentParser()
parser.add_argument('--log', help='Selects log level. Options: DEBUG, INFO, WARNING, ERROR, CRITICAL')
parser.add_argument('--env', help='Selects deployment to: PROD or DEV(default)')
args = parser.parse_args()

if args.log:
	numeric_level = getattr(logging, args.log.upper(), None)
	if not isinstance(numeric_level, int):
	    raise ValueError('Invalid log level: %s' % args.log)
	logging.basicConfig(level=numeric_level, format='%(levelname)s: %(message)s')
else:
	logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s')

logLevel = logging.getLevelName(logging.getLogger(__name__).getEffectiveLevel())
logging.getLogger(__name__).info('logging={}'.format(logLevel))

# Setup DB connection
if args.env:
	if args.env.upper() not in dbMapping:
		raise ValueError('--env argument not specified')
	dbName = dbMapping[args.env.upper()]
	db = pymongo.MongoClient()[dbName]
	logging.getLogger(__name__).info('db={}'.format(dbName))
