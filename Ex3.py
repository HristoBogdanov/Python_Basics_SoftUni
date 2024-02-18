weight=float(input())
service=input()
distance=int(input())

price_under_1=3
price_under_10=5
price_under_40=10
price_under_90=15
price_under_150=20

total=0.0

if service=="standard":
    if weight<1:
        total=distance*price_under_1
    elif weight<10:
        total=distance*price_under_10
    elif weight<40:
        total=distance*price_under_40
    elif weight<90:
        total=distance*price_under_90
    elif weight<150:
        total=distance*price_under_150
else:
    if weight<1:
        total=distance*price_under_1 + distance*(weight*0.8*price_under_1)
    elif weight<10:
        total=distance*price_under_10 + distance*(weight*0.4*price_under_10)
    elif weight<40:
        total=distance*price_under_40 + distance*(weight*0.05*price_under_40)
    elif weight<90:
        total=distance*price_under_90 + distance*(weight*0.02*price_under_90)
    elif weight<150:
        total=distance*price_under_150 + distance*(weight*0.01*price_under_150)

print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {total/100:.2f} lv.")