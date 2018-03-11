import csv
'''
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
'''
def getFloat(str):
    if not str:
        return 0
    else:
        return float(str)

def loadcsv(str):
    data = [];
    data2 = [];
	
    ahl_data = [];
    chl_data = [];
    ncaa_data = [];
    khl_data = [];
    europe_data = [];
	
    with open('condensed16-17.csv', 'r') as csvfile:
        data = list(csv.reader(csvfile))
        for row in data[2:]:
			if row[3] == 'AHL' and getFloat(row[2]) / getFloat(row[4]) <= 1.1:
				ahl_data += [[getFloat(row[2]), row[3], getFloat(row[4])]]
			
			elif row[3] == "OHL" or row[3] == "WHL" or row[3] == "QMJHL" and getFloat(row[2]) / getFloat(row[4]) <= 1.1:
				chl_data += [getFloat(row[2]), row[3],  getFloat(row[4])]
				
			elif row[3] == "NCAA" and getFloat(row[2]) / getFloat(row[4]) <= 1.1:
				ncaa_data += [getFloat(row[2]), row[3],  getFloat(row[4])]
				
			elif row[3] == "KHL" and getFloat(row[2]) / getFloat(row[4]) <= 1.1:
				khl_data += [getFloat(row[2]), row[3],  getFloat(row[4])]
				
			elif getFloat(row[2]) / getFloat(row[4]) <= 1.1:
				europe_data += [getFloat(row[2]), row[3],  getFloat(row[4])]
				
			else:
				continue
				
	#ahl_ly_ppg_x_train = ahl_data
				
    print "europe: ", europe_data 
    print "khl: ", khl_data
    print "ahl: ", ahl_data
    print "chl: ", chl_data
    print "ncaa: ", ncaa_data

loadcsv('condensed16-17.csv')
#print data2