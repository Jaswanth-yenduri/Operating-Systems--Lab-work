from texttable import Texttable

t = Texttable()
t.add_row(['Process','Memory acquired','Allocated?','internalfragmentation'])

process_memory = []
tif=0
total_memory = int(input("Enter the total memory available : "))
blocksize = int(input("Enter the blocksize: "))
numOfBlocks = int(total_memory/blocksize)
processes_num = int(input("Enter number of processes:"))
externalfrag=total_memory - (processes_num*blocksize)
if(processes_num <= numOfBlocks):
    for i in range(0,processes_num):
        print("Enter the size of process",i+1,'in bytes : ')
        mem = int(input())
        process_memory.append(mem)
    print("Number of block in memory are:",numOfBlocks)
    for i in range(0,processes_num):
        internalfrag = blocksize - process_memory[i]
        if internalfrag >= 0:
            tif += internalfrag
        else:
            internalfrag = blocksize
        if(process_memory[i] > blocksize):
            isAllocated = 'NO'
        else:
            isAllocated = 'YES'
        t.add_row([i+1,process_memory[i],isAllocated,internalfrag])

    print(t.draw())
    print("External fragmentation : ",externalfrag)
    print("Total internal fragmentation : ",tif)
else:
    print("Number of processes is more  than number of partitions")

