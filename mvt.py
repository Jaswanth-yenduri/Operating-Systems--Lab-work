from texttable import Texttable

t = Texttable()
t.add_row(['Process','Memory allocated'])

total_memory = int(input("Enter the total memory available in bytes : "))
temp=total_memory
flag= True
i=1

while flag:
    print("Enter memory of process ",i,"in bytes : ",end="")
    mem = int(input())
    if mem <= temp:
        temp -= mem
        t.add_row([i,mem])
        i+=1
    else:
        print("Total memory execeeded")
        break
    inp = input("Do you want add another process? (y/n) : ")
    if inp=='n':
          flag=False


print(t.draw())
print("Total memory used is:",total_memory-temp)
print("External fragmentation is :",temp)
