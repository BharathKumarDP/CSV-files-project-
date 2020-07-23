import csv
import matplotlib.pyplot as plt
import numpy as np

file1='books.csv'
file2='availability.csv'
file3='number.csv'
file4='ratings.csv'
output = 'data.csv'
fieldname=['ID','Name','Ratings','Available']

#opening input csv files
with open(file1, 'r') as csvname, \
 open(file4, 'r') as csvrate, open(file2, 'r') as csvavail, open(file3 , 'r') as csvnum,open(output,'w',newline= '') as file:

        num = csv.reader(csvnum)
        name = csv.reader(csvname)
        ratings = csv.reader(csvrate)
        avail = csv.reader(csvavail)
        
        file=csv.writer(file,delimiter=",")
        file.writerow(fieldname)
        
        for row, row1, row2, row3 in zip(num, name, ratings, avail):
            for x in range(len(row)):
               file.writerow([row[x], row1[x], row2[x], row3[x]])

#opening output file "data.csv"
fields, recs = [], []
with open(output, 'r') as new_file:
    read = csv.reader(new_file, delimiter = ',')
    
    fields = next(read)
    for row in read: 
        recs.append(row)


#task1-ID
for i in range(1,99,2):
    if(recs[i][0]==''):
        recs[i][0]=i
for i in range(98,0,-2):
    if(recs[i][0]==''):
        del recs[i]
        
#task2-Names
for i in range(len(recs)):
    if(recs[i][1]==''):
        if(i>=10):
            recs[i][1]=recs[i-10][1]
        else:
            recs[i][1]=recs[0][1]
    
#task3-Ratings
for i in range(len(recs)):
    if (recs[i][2] == ''):
        recs[i][2] = 0.0
    else:
        recs[i][2] = float(recs[i][2])
    if (recs[i][2] > 5.0):
      recs[i][2] = float(5.0)

#task4-Availability
for i in range(len(recs)):    
    if(recs[i][3] == '0'):
        recs[i][3] = 'f'
    if(recs[i][3] == '1'):
        recs[i][3] = 't'

        
#writing output with changes made
with open(output, 'w', newline='') as new_file:
   write = csv.writer(new_file, delimiter = ',')
   write.writerow(['ID', 'Name', 'Ratings','Available'])
    
   for row in recs:
      write.writerow(row)



##Matplotlib
x=[]
y=[]
z=[]
with open(output,'r') as new_file:
    graph=csv.reader(new_file,delimiter=',')
    next(graph)
    for row in graph:
        x.append(int(row[0]))
        y.append(float(row[2]))
        z.append(str(row[3]))
f1=plt.figure(1)
plt.plot(x,y,label="line",color='red',linewidth='2')
plt.title('Books Vs Rating')         
plt.xlabel('ID')
plt.ylabel('Ratings')
plt.xticks(np.arange(0,99,5))
plt.yticks(np.arange(0,5.5,0.5))



#Additional graph of Books VS Ratings.
f2=plt.figure(2)
plt.scatter(x,z,color="green")
plt.title('Books Vs Availability')
plt.xlabel('ID')
plt.ylabel('Availability')
plt.xticks(np.arange(0,99,5))
my_yticks=['Out of stock','Available']
y=np.array([0,1])
plt.yticks(y,my_yticks)
plt.show()




  
