# Python program to print the content of each line of the input file along with line number   
  
List = ["Python is an interpreted, high-level and general-purpose programming language.\n",
     "Its language constructs and object-oriented approach aim to help programmers write clear, logical code.\n",
     "Python is dynamically typed and garbage-collected.\n"] 
  
# Writing to a file 
file = open('AboutPython.txt', 'w') 
file.writelines((List)) 
file.close() 
  
# Using readline() 
file = open('AboutPython.txt', 'r') 
count = 0
  
while True: 
    count += 1
  
    # Get next line from file 
    line = file.readline() 
  
    # if line is empty 
    # end of file is reached 
    if not line: 
        break
    print("Line{}: {}".format(count, line.strip())) 
  
file.close()
