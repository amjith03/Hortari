flag =0 
data = []
for i in range(0,3):
	data.append(int(input()))
print("3 lengths are",data)
if (data[0] + data[1] > data[2]) :
	flag = flag+1
if(data[0] + data[2] > data[1]):
	flag = flag+1 
if(data[1] + data[2] > data[0]):
	flag = flag+1

if(flag>2):
	print("3 lengths are sides of triangle")
else:
	print("Lengths are not sides of the triangle")
	

