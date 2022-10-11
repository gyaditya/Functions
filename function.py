#Functions By Adi

test = [4, 7, 2, 5, 10]
print(test)
 #Contains
def contains(aList, item):
  for i in range(len(aList)):
    if (aList[i]) == (item):
      return True


# Index Of
def indexOf(aList, item):
    for index, element in enumerate(aList):
        if element == item:
          return index
    return -1


#Reverse
def reverse(aList):
  reverse = aList[::-1]
  return reverse

#Swap
def swap(aList, index1, index2):
  save = aList[index1]
  aList[index1] = aList[index2]
  aList[index2] = save
  return aList

#IndexOfMin
def indexofmin(aList):
  minposition = 0
  for i in range(1, len(aList)):
    if aList[i] < aList[minposition]:
      minposition = i
  return minposition

# Run the function

#Contains
if contains(test, 7):
  print("Number is in the list")
else:
  print("Number is NOT in the list")

#Indexof
print(indexOf(test, 7))

#Reverse
print(reverse(test))

#Swap
print(swap(test, 2, 4))

#IndexofMin
print(indexofmin(test))
