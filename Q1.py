length=int(input("Enter the length of the array: "))
start=int(input("Enter the start of the array: "))

def myArray(length,start):

    newArray=[]
    for i  in range(start,length,1):
    
        newArray.append(i)
    print(newArray)

myArray(length,start)