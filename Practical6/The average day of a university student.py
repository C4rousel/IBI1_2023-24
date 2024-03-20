import matplotlib.pyplot as plt
#make a new dictionary 
dict = {}
#input data from input list
dict['Time spent during an average day of Sleeping']= '8 hours'
dict['Time spent during an average day of Classes']= '6 hours'
dict['Time spent during an average day of Studying']= '3.5 hours'
dict['Time spent during an average day of TV']= '2 hours'
dict['Time spent during an average day of Music']= '1 hours'
dict['Time spent during an average day of Others']= '3.5 hours'
print (dict)

#makeing a pie chart
#input data of pie chart 
Activity_labels = [
"Sleeping", "Classes", "Studying ", "TV", 
"Music", "Others"]
#input the proportion of data 
time_day = [8, 6, 3.5, 2, 1,3.5]
# use data to make pie chart 
plt.figure()
plt.pie(time_day, labels =
Activity_labels, 
startangle = 90, )
#show the pie chart 
plt.show()
#close the pie chart 
plt.clf()

#create variables
Sleeping=8
classes=6
studying=3.5
TV=2
Music=1
Others=3.5
print("the number of hours spent on sleeping during an average day is",Sleeping,"hours")
print("the number of hours spent on classes during an average day is",classes,"hours")
print("the number of hours spent on studying during an average day is",studying,"hours")
print("the number of hours spent on TV during an average day is",TV,"hours")
print("the number of hours spent on music during an average day is",Music,"hours")
print("the number of hours spent on others during an average day is",Others,"hours")

