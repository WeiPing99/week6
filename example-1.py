import csv 

file = open("TitanicSurvival.csv","r")
data = list(csv.reader(file, delimiter= ","))
#last_element = data [len(data)-1]
file.close()

zimmer = data[-1]
zimmer[4] = ('1st')

#print(data[-1])
print(zimmer)
