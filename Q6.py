from curses.ascii import isdigit


def enterNum():
    
    count=0
   
    sum=0

    while(True):
        num=input("Enter the number: ")
        if num.isdigit():
            count+=1
            sum+=int(num)    
        elif num == "done":
            break
        else:
            print("Invalid input , Try again")
            continue
        
        

    
    print(f"""count of numbers: {count}
        sum of numbers: {sum}
        avg of numbers: {float(sum/count)}""")



enterNum()