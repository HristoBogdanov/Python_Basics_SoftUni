n=int(input())

isABCDfound=False
isDCBAfound=False

for a in range(1, 10):
    for b in range(9, a, -1):
        for c in range(0, 10):
            for d in range(9, c, -1):
                if isABCDfound==False and isDCBAfound==False:
                    if ((a + b + c + d)==(a * b * c * d) and n % 10 == 5):
                        print(f"{a}{b}{c}{d}")
                        isABCDfound=True
                        break
                    elif ((a * b * c * d)//(a + b + c + d))==3 and n % 3 == 0:
                        print(f"{d}{c}{b}{a}")
                        isDCBAfound=True
                        break
                else: continue

if(isABCDfound==False and isDCBAfound==False):
    print("Nothing found")
