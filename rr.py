from texttable import Texttable

class process:
    def __init__(self, sno, name, arrival, burst):
        self.sno = sno
        self.name = name
        self.arrival = arrival
        self.burst = burst
        self.rem = burst
        self.wt = 0
        self.tt = 0
    
    def to_list(self):
        return [self.sno,self.name,self.arrival,self.burst,self.wt,self.tt]
    def deb(self):
        return [self.name,self.arrival,self.burst,self.rem,self.wt,self.tt]
    

def roundrobin(d,quant):
    t = Texttable()
    t.add_row(["S.No","Process name","Arrival time","Burst time","Wait time","Turnaround time"])
    l = list(d.keys())
    l.remove(0) 
    que = list()
    q = []
    clock = 0
    i = 0
    total_wt=0
    total_tt=0
    que.append(d[0])
    while len(que)>0:
        if que[i].rem>quant:
            clock+=quant
            que[i].rem -=quant
            for at in l:
                if at <= clock:
                    if isinstance(d[at],list):
                        que.extend(d[at])
                    else:
                        que.append(d[at])
                    l.remove(at)
                else:
                    break
            que.append(que[i])
            que.remove(que[i])
        elif que[i].rem == quant:
            clock+=quant
            que[i].rem = 0
            que[i].wt = clock - que[i].burst-que[i].arrival
            que[i].tt = que[i].wt + que[i].burst
            total_tt+=que[i].tt
            total_wt+=que[i].wt
            q.append(que[i])
            que.remove(que[i])  
        else:
            clock+=que[i].rem
            que[i].rem=0
            que[i].wt = clock - que[i].burst-que[i].arrival
            que[i].tt = que[i].wt + que[i].burst
            total_tt+=que[i].tt
            total_wt+=que[i].wt
            q.append(que[i])
            que.remove(que[i])
    q = sorted(q,key = wrt_sno)
    for i in q:
        t.add_row(i.to_list())
    print(t.draw())
    
    print("Total waiting time :",total_wt)
    print("Averge waiting time :",(total_wt/len(d)))

    print("Total turnaround time :",total_tt)
    print("Average turnaround time :",(total_tt/len(d)))

def wrt_sno(x):
    return x.sno
        
if __name__ == "__main__":
    q = int(input("Enter the quantum in ns : "))
    n = int(input("Enter the number of processes : "))
    d,l={},[]
    for i in range(n):
        print(30*'*')
        name = input("Enter the name of process : ")
        at = int(input("Enter the arrival time of the process in ms: "))
        bt = int(input("Enter the burst of the process in ms : "))
        if at not in d.keys():
            d[at]=process(i+1,name,at,bt)
        else:
            d[at]=[d[at],process(i+1,name,at,bt)]

    roundrobin(d,q)
