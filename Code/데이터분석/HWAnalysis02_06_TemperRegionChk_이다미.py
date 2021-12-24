import csv
regionData=open("./../_dataSetGilBut01/temperRegion.txt","r")
city=csv.reader(regionData)
regionList=[]
spList=[]
sList=[]
finList=[]
for x in city:
	regionList.append(x)
print()
print()
print()

for vmyList in regionList:
	for x in vmyList:
		spList.append(x)

for x in spList:
	if ":" in x:
		finList.append(x.split(":")[1])
	else:
		finList.append(x)

for x in range(len(finList)):
	x=finList[x].split("(")[1].split(")")[0], finList[x].split("(")[0]+"\n"
	sList.append(list(x))


regionFin=open("../_dataSetGilBut01/temperRegionChk.csv", "w")
for x in sList:
	x=",".join(x)
	regionFin.write(x)	
regionFin.close()