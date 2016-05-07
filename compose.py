en = []
ua = []
with open ("data/en.txt", "r") as myfile:
    en=myfile.readlines()

with open ("data/ua.txt", "r") as myfile:
    ua=myfile.readlines()


if len(ua) != len(en):
	print("something wrong, amount of words is different")
else:
	f = open('data/compose.txt','w')
	for i in range(len(en)):
		f.write('{"en": "'+en[i].replace('\n', '')+'", "ua": "'+ua[i].replace('\n', '')+'"},\n')
	f.close()


