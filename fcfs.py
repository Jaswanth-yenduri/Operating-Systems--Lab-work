from texttable import Texttable

def wrt_arrival_time(x):
    return x[1]

if __name__ == "__main__":
    n = int(input("Enter the number of process : "))
    l=[]
    for i in range(n):
        print(30*'*')
        name = input("Enter the name of the process : ")
        arrival = int(input("Enter the arival time of process in ms : "))
        burst_time =int(input("Enter the burst time in ms : "))
        x = [name,arrival,burst_time,0,0]
        l.append(x)
    
    l = sorted(l,key=wrt_arrival_time)
    l[0][4]=l[0][2]
    for i in range(1,n):
        w=0
        for j in range(0,i):
            w+=l[j][2]
        l[i][3]=w-l[i][1]
        l[i][4]=l[i][2]+l[i][3]

    total_wt=0
    total_tt=0
    for i in l:
        total_wt +=int(i[3])
        total_tt += int(i[4])
    
    t = Texttable()
    head = ['Process Name','Arrival Time','Burst Time','Wait Time','Turnaround Time']
    l.insert(0,head)
    t.add_rows(l)
    print(t.draw())
    
    print("Total waiting time :",total_wt)
    print("Average waiting time :",total_wt/n)

    print("total turnaround time :",total_tt)
    print("Average turnaround time :",total_tt/n)
    

