import os
import csv
import random
import pandas as pd
print("WLECOME TO ONLINE BOOKING")
print("please select any option:")


def append_data(booking_id,name,phone,src,dst,distant,price,seat_type):
    csv_path='booking.csv'
    if os.path.exists(csv_path):
        with open(csv_path,mode='a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow([booking_id,name,phone,src,dst,distant,price,seat_type])
    else:
        with open(csv_path,mode='w',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Booking_Id','name','phone','source','destination','distance','price','seat_type'])
    return True
source = ['Hyderbad','Chennai','Banglore','Tirupati','Manglore','Palamaner']
destination = ['Hyderbad','Chennai','Banglore','Tirupati','Manglore','Palamaner']
distance ={"Hyderbad-Chennai":"620",
"Hyderbad-Banglore":"635",                                                        
"Hyderbad-Tirupati":"639",
"Hyderbad-Manglore":"595",
"Hyderbad-Palamaner":"335",
"Chennai-Hyderbad":"474",
"Chennai-Banglore":"403",
"Chennai-Tirupati":"670",
"Chennai-Manglore":"442",
"Chennai-Palamaner":"355",
"Banglore-Hyderbad":"684",
"Banglore-Chennai":"509",
"Banglore-Tirupati":"441",
"Banglore-Manglore":"663",
"Banglore-Palamaner":"317",
"Tirupati-Hyderbad":"507",
"Tirupati-Chennai":"319",
"Tirupati-Banglore":"662",
"Tirupati-Manglore":"611",
"Tirupati-Palamaner":"546",
"Manglore-Hyderbad":"424",
"Manglore-Chennai":"671",
"Manglore-Banglore":"329",
"Manglore-Tirupati":"579",
"Manglore-Palamaner":"332",
"Palamaner-Hyderbad":"378",
"Palamaner-Chennai":"343",
"Palamaner-Banglore":"351",
"Palamaner-Tirupati":"483",
"Palamaner-Manglore":"472"}
print('''1.To check bus availability and book 
2.To check reservation status
      ''')
inpu_flag=True
inp=int(input("enter selected option:"))
while True:
    if inp not in (1,2):
        inp = int(input("enter selected option:"))
    else:
        break
if inp ==1:
    print('Bus Availability:')
    print([i for i in source])
    src = input("enter source place :")
    print([i for i in destination])
    dst = input("eneter destination place:")
    while True:
        src = src.capitalize()
        dst = dst.capitalize()
        if src not in source:
            src = input("please enter valid source place :")
        if dst not in destination:
            dst = input("please enter destination place:")
        elif src == dst:
            print("source and destination should not be same")
        else :
            break
    select=f'{src}-{dst}'
    distant = distance[select]
    price = int(distance[select]) * 4.5
    print("you have selected ",select,"distnace:",distant,"kms  ","Price:RS.",price)
    print("Do you want book tiket yes/no: ")
    chos=input(":")
    while True:
        if chos.lower()!='yes' and  chos.lower()!='no':
            chos=input(":")
        if chos.lower() == 'no':
                      
            print(".........Thanks you .............")
            break
        else :
            print("booking process started.................")   
            usr_nam=input("Enter use name: ")
            usr_phn=int(input("enter your personal phone number: "))
            print("choose booking sites--\n 3 Ac seats\n4 Non Ac seats")
            var=("3-ac sites\n4-non ac sites\n")
            chose=int(input("select option: "))
            while True:
                    if chose not in  (3,4):
                        chose=int(input("kindly request please select option: "))
                        print(" please selected option in below"+var)
                    booking_id = random.randint(1000000000,9999999999)
                    if chose == 3:
                        append_data(booking_id,usr_nam,usr_phn,src,dst,distant,price,'AC')
                        print(" AC seat booking successfuly...Booking Id:",booking_id)
                        break  
                    elif chose == 4:
                        append_data(booking_id,usr_nam,usr_phn,src,dst,distant,price,'Non-AC')
                        print("Non AC seat booking successfuly...Booking Id:",booking_id)
                        break  
            break   
  
if inp ==2:
    print("reservation status...............+")
    id =int(input("enter Booking Id"))
    df = pd.read_csv('booking.csv')
    if id in df.values  :
        print(df[df['Booking_Id']==id])
    else:
        print("Booking_id not found...")

 
# bus_type=['olaBuss','redBuss','kvBuss','mpBuss']
# var1=input("choose bus types")
# var=input("to check buss availble: ")