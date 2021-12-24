import csv

f = open('./../_dataSetGilBut01/SEOUL.csv', 'r')
temperatureFile = csv.reader(f, delimiter=',')
vHeader = next(temperatureFile)
print(vHeader)

f.close()