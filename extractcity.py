import read
import codecs

town = []
f = open('town.txt','w')
temp = ''
with codecs.open("in.txt") as file:#open
	count = 0
	for line in file:
		str1 = ''
		longitude = ''
		latitude = ''
		app = ''
		for k in line:
			if ('\t' == k):
				count = count+1
			if (count == 2):
				#print k
				if not('\t' in k):
					str1+=k
			if (count == 4):
				#print k
				if not('\t' in k):
					longitude+=k
			if (count == 5):
				#print k
				if not('\t' in k):
					latitude+=k
			if (count == 6):
				break
		#town.append((str1,longitude,latitude))
		print str1
		print longitude
		print latitude
		
		if (temp != str1):
			app = str1+'\t'+longitude+'\t'+latitude+'\n'
			f.write(app)
		count = 0;
		temp = str1	

#print town

#with open("in.txt") as f:
#	k = f.readlines()
#	print k
#print fo.name
#file1 = fo.readlines()
#counter = 0;
#print file1
#for  line in file1:
#	counter = counter+1;
#	print counter
#print lien