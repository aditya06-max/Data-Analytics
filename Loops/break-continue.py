for i in range(0,10):
    #in this for loop the condition is checked everytime its running and when i == 5 the code execution breaks and execution stops immediately. 
    if(i==5):
        break
    print(i) 
    
for i in range(0,10):
    if(i==5):
        #In this continue statement loop runs until value of i becomes 4 and when it becomes 5 it will skip it and then continue from 6 onwards.
        continue
    print(i)
