myList = [1,2,3]
myList = [item+1 for item in myList]
print('myList: ', myList)   
#  ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

myList = [1,2,3]

for index, item in enumerate (myList):
    
    myList[index] = item+1
    print('index:' , index   ,   '        item :', item )
  


print('myList: ', myList)   


#  ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
myList = [1,2,3]
for i in range(len(myList)):
    myList[i] +=1

print('myList: ', myList)   