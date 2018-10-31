
def Repeat(x): 
	flag=0
	size = len(x) 
	repeat = [] 
	for i in range(size): 
		k = i + 1
		for j in range(k, size): 
			if x[i] == x[j] and x[i] not in repeat: 
				repeat.append(x[i])
				flag=flag+1
	return(repeat,flag)
  
list1 = [1,2,2,3,3,3] 
print (Repeat(list1)) 
