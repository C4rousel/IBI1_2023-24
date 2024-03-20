#make lists
uk_cities=[0.56,0.62,0.04,9.7]
china_cities=[0.58,8.4,29.9,22.2]
lables=["Edinburgh","Glasgow","Stirling","London"]
lables2=["Haining","Hangzhou","Shanghai","Beijing"]
print(china_cities)
print(uk_cities)

#import plt
import numpy as np
import matplotlib.pyplot as plt
#set the style of bar chart
plt.style.use('bmh')
#set radix of bar chart
N = 8
scores = uk_cities
scores2=china_cities
scores3=scores+scores2
width = 0.25
#make a bar chart
plt.figure()
plt.bar(lables, scores, width)
plt.bar(lables2, scores2, width,color='#CE0000')
#Let the data display above the bar chart
for i in range(len(lables+lables2)) :
    plt.text(i,scores3[i],scores3[i],va='bottom',ha='center')
#set the title and ylabel of bar chart   
plt.ylabel("populations(million)")
plt.title("Cities in both the UK and China in 2024 are of varying populations")
plt.show()
plt.clf() 