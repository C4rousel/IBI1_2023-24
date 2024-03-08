# Define the initial cell density as a percentage
Cell_density=5
# Define the first day 
day=1
#Initialize a loop that will continue until the cell density is less than 90 percent
while Cell_density<90:
#With each additional day, the cell density doubles
   Cell_density*=2
   day+=1
#when cell density exceeded 90 percent，the loop will stop
while Cell_density>90:
   break 
#print the answer
print (f"Cell density exceeded 90% on Day {day}.") 
print(f"Therefore, you can stay away and take a holiday from the lab for {day-1} days.")