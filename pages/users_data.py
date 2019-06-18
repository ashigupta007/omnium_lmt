import csv

def generate_user_data():
	file = open('/Users/ashish/documents/projects/omnium/omnium_lmt/static/userlogs_Logins.csv', 'r')
	reader =csv.reader(file)
	users={}
	next(reader, None)
	for row in reader:
		country = row[2]
		level = row[6]
		if country in users :
			if level in users[country] :
				users[country][level]['count'] += 1
			else :
				users[country][level] = {'count' : 1 }
		else :
			users[country]= { level : {'count' : 1 } }
	return users