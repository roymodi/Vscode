file1=open('file_handaling\\sample.txt','r')
line = file1.readline() 

# Using readline() 
count = 0

while True: 
	count += 1

	# Get next line from file 
	line = file1.readline() 

	# if line is empty 
	# end of file is reached 
	if not line: 
		break
	print("Line{}: {}".format(count, line.strip())) 


file1.close() 
