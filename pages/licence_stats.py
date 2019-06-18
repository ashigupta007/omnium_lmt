import csv

def generate_licence_stats():
	file = open('/Users/ashish/documents/projects/omnium/omnium_lmt/static/user_log.csv', "r")
	reader = csv.reader(file)
	time = {}
	next(reader, None)
	for row in reader:
		licence_name = row[2]
		server = row[1]
		timestamp = row[0]
		if licence_name in time:
			if timestamp in time[licence_name]:
				if server in time[licence_name][timestamp]:
					time[licence_name][timestamp][server]['count'] += 1
				else:
					time[licence_name][timestamp][server] = { "count": 1 }
			else:
  				time[licence_name][timestamp] =  { server: { "count": 1 } }
		else :
  			time[licence_name] = { timestamp: { server: { "count": 1 } } }

	return time
