def revArray(list):
    tempList = []
    if (len(list) > 1):
        for i in range(len(list) - 1,-1,-1):
            tempList.append(list[i])
        return tempList

l1 = [1,2,3]
print(revArray(l1))
