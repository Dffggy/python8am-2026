print("========Welcome to computer bazaar=======")
print("1, dell(30000) 2, hp(20000) 3, mac(40000)")
dell_price=0
hp_price=0
mac_price=0
product_name="" 
quantity=0
option=int(input("enter the optional number you want to buy: "))

if option==1:
    quantity=int(input("enter the quantity u want to buy: "))
    dell_price=30000*quantity
    product_name="dell"
elif option==2:
    quantity=int(input("enter the quantity u want to buy: "))
    hp_price=20000*quantity
    product_name="hp"
elif option==3:
     quantity=int(input("enter the quantity you want to buy: "))
     mac_price=40000*quantity
     product_name="mac"
else:
     print("invalid option")

total=dell_price+hp_price+mac_price
print("delivery option: 1,home(rs.2000) 2,store pickup(rs.0)")
delivery_price=0
dev_option=int(input("enter the delivery option number: "))
if dev_option==1:
   delivey_price=2000

packaging_price=0
print ("packaging: 1. Plastic bag(rs:1000) 2. bag(rs;2000) 3. gift box(Rs:5000) 4. no packaging(rs:0)")    
pack_option=int(input("enter the packing option number:"))
if pack_option==1:
    packaging_price=1000
elif pack_option==2:
    packaging_price=2000
elif pack_option==3:
    packaging_price=5000
elif pack_option==4:
    packing_price=0


enter_amoumt=0
print("location:1, KTM(RS:13%) 2, LTP(Rs:0)")
loc_option=int(input("enter your location option number: "))
if loc_option==1:
    tax_amount=total*0.13
grand_total= total+delivery_price+packaging_price+tax_amount

print("======invoice=======")
print("product Name:",product_name)
print("quantity:",quantity)
print("total price:",total)
print("Deliver Price:",delivery_price)
print("packaging Price:",packaging_price)
print("Tax Amount:",tax_amount)
print("Grand totsl:",grand_total)


distance = 27
fare = 0

if distance <= 5:
    fare = 15
elif distance <= 10:
    fare = 30
elif distance <= 15:
    fare = 45
elif distance <= 20:
    fare = 60
elif distance <= 25:
    fare = 75
else:
    fare = 90   # for distance above 25 km up to 27 km

print("Total bus fare is Rs.", fare)
