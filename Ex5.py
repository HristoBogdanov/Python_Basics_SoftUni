vacations_sea=int(input())
vacations_mountain=int(input())

profit=0

while(vacations_sea!=0 or vacations_mountain!=0):
    data=input()
    if data=="Stop":
        break
    elif data=="sea":
        if vacations_sea>0:
            profit+=680
            vacations_sea-=1
    elif data=="mountain":
        if vacations_mountain>0:
            profit+=499
            vacations_mountain-=1

if(vacations_sea==0 and vacations_mountain==0):
    print("Good job! Everything is sold.")

print(f"Profit: {profit} leva.")