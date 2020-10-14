from texttable import Texttable

class process:
    def __init__(self, sno, name, arrival, burst):
        self.sno = sno
        self.name = name
        self.arrival = arrival
        self.rem = burst
        self.burst = burst
        self.wt = 0
        self.tt = 0
        self.ct = 0
    
    def to_list(self):
        return [self.sno,self.name,self.arrival,self.burst,self.wt,self.tt,self.ct]

def priority(d):
    t = Texttable()
    t.add_row(["S.No","Process name","Arrival time","Burst time","Wait time","Turnaorund time","Completion time"])
    clock = 0
    temp = []
    l = []
    total_wt=0
    total_tt=0
    n = len(d)
    while len(d) > 0:
        d= sorted(d,key=wrt_at)
        for at in d:
            if at.arrival <= clock:
                temp.append(at)
        temp = sorted(temp,key=wrt_rem)
        if len(temp)==0:
            clock+=1
            continue
        clock+=1
        temp[0].rem -=1
        if temp[0].rem ==0:
            temp[0].ct=clock
            temp[0].tt=temp[0].ct - temp[0].arrival
            temp[0].wt=temp[0].tt- temp[0].burst
            total_tt+=temp[0].tt
            total_wt+=temp[0].wt
            l.append(temp[0])
            d.remove(temp[0])
        temp.clear()
    l = sorted(l,key = wrt_sno)
    for i in l:
        t.add_row(i.to_list())
    print(t.draw())
    
    print("Total waiting time :",total_wt)
    print("Averge waiting time :",total_wt/n)

    print("Total turnaround time :",total_tt)
    print("Average turnaround time :",total_tt/n)
    
def wrt_at(x):
    return x.arrival

def wrt_rem(x):
    return x.rem

def wrt_sno(x):
    return x.sno

if __name__ == "__main__":
    n = int(input("Enter the number of processes : "))
    d=[]
    for i in range(n):
        print(30*'*')
        name = input("Enter the name of process : ")
        at = int(input("Enter the arrival time of process in ms: "))
        bt = int(input("Enter the burst time of process in ms: "))
        d.append(process(i+1,name,at,bt))

    priority(d)

