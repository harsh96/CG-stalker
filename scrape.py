import urllib2
import re

dept = 'MA'
year = '14'
batch = '2' # 1, 2 or 3
total_students = 57

roll_nos = []
cgpas = []

for i in range(1, total_students+1):
  roll = dept+year+batch+'00'
  if i < 10:
    roll += '0'+`i`
  else:
    roll += `i`
  roll_nos.append(roll)

for roll in roll_nos:
	url = "https://erp.iitkgp.ernet.in/StudentPerformance/view_performance.jsp?rollno="
	url += roll
	data = urllib2.urlopen(url)
	page = data.read()

	searchObj = re.search( r'<b> CGPA</b></td><td>\d.\d\d</td>', page, re.M|re.I)
	if searchObj:
	   primary = searchObj.group(0)
	   secondary = re.search( r'\d.\d\d', primary, re.M|re.I)
	   if secondary:
	   		cgpa = secondary.group(0)
	   		cgpas.append(cgpa)
	   		print cgpa
	else:
		cgpa = 0
		cgpas.append(cgpa)
   		print cgpa


sorted_cgpas = [(cg,roll) for (cg,roll) in sorted(zip(cgpas, roll_nos))]
i = 0
for x in sorted_cgpas:
	print (total_students-i), x
	i = i+1

