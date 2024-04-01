"""
"""
#question A
list1=list(range(1,16))
print(list1)
list2=[item for item in range(1,16)]
l=[30,40]
list2.extend(l)
print(list2)
del list2[14:15]
print('list 2 after del:', list2)
list3=[i**2 for i in list2]
print(list3)
list4=list(x**0.5 for x in list3 if x % 2 == 0)
print(list4)
list5=list(map(lambda x: x**0.5,filter(lambda y:  y % 2 == 0, list3)))
list6=[x**0.5 for x in list3 if x % 2 ==0]
print('list5:', list5)
print('list6:', list6)





"""
"""
#question B

responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]

for i in range(1,6):
    print(f'{i}:{responses.count(i)} times')
    
    
    
    
    
"""
"""
#question C

theList=[ [77, 68, 86, 73],
          [96, 87, 89, 81],
          [70, 90, 86, 81]]

print(theList)
for row in theList:
    for item in row:
        print(item, end=' ')
    print()
    


print(" ")

listsum=(list(map(sum, theList)))
maxsum=max(listsum)
print("The sum of each row is" ,listsum)
print("The max of rows is: " ,maxsum)

          

           