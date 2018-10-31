flag=0
def Repeat(x): 
    size = len(x) 
    repeated = [] 
    for i in range(size): 
        k = i + 1
        for j in range(k, size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i])
		flag=flag+1 
    return repeated 
  
list1 = [1,2,2,3,3,3] 
print (Repeat(list1)) 
