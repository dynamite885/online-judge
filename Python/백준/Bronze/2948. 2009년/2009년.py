D,M=map(int,input().split())
days=[31,28,31,30,31,30,31,31,30,31,30,31]
day=["Wednesday","Thursday","Friday","Saturday","Sunday","Monday","Tuesday"]
for i in range(M-1):D+=days[i]
print(day[D%7])