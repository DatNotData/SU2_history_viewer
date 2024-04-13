# Script to plot all variables in the history.vtk file from the SU2 solver
# To run the script, open a command prompt and enter the following command (assuming you start in the folder where the script is)
# py .\history_viewer.py .\history.vtk
# where history_viewer.py is the script, and history.vtk (or wtv you renamed it) is the name of the history file
# Author: Dat Ha
# Year: 2024

import matplotlib.pyplot as plt
import numpy as np
import os
import sys


script_dir = os.path.dirname(os.path.abspath(__file__))

def get_data(filepath):
    file = open(filepath, 'r', )
    raw = file.read()
    file.close()

    tmp = raw.replace(' ','')
    tmp = tmp.split('\n')
    raw_data = []
    headers = []
    tmp[0] = tmp[0].replace('"','')
    headers = tmp[0].split(',')

    for i in range(1,len(tmp)):
        if tmp[i] == '':
            continue
        line_tmp = tmp[i].split(',')
        line_tmp = [float(value) for value in line_tmp]
        raw_data += [line_tmp]
    raw_data = np.array(raw_data)

    data = {}
    for i in range(len(headers)):
        data[headers[i]] = raw_data[:,i]
    return data, headers


filepath1 = sys.argv[1]
data1, headers1 = get_data(filepath1)


print('##########################################################################################################')
print('OPTION LIST')
print('##########################################################################################################')
for i in range(len(headers1)):
    print('Option: '+ str(i) + '; Header: ' + headers1[i])
print('##########################################################################################################')
print()

while True:
    plt.clf()
    x_index = int(input('Enter x option number: '))    
    y_index = int(input('Enter y option number: '))
    #for i in range(5):
        #plt.plot(data['Time(min)'],data['Res_Flow['+str(i)+']'],label='Res_Flow['+str(i)+']')
    plt.plot(data1[headers1[x_index]],data1[headers1[y_index]])
    plt.grid(visible=True, which='both')
    plt.xlabel(headers1[x_index])
    plt.ylabel(headers1[y_index])
    plt.title(headers1[y_index] + ' VS ' + headers1[x_index])
    plt.show()
    print()