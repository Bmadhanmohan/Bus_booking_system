import pandas as pd
from flask import jsonify
import haversine as hs
from haversine import Unit
# Booking_Id=7616139487
# df = pd.read_csv('booking.csv')
# df1 = df
# # booking_id,username,phone,s,d,distant,price,buss_type,bus_selection,seat_number,no_pass,total_price
# # dff=df.loc[(df['source']==s)&(df['destination']==d)&(df['Selected_bus']==bus_selection)&(df['seat_type']==buss_type),['Seat_number']]
# # dff=df.loc[(df['source']=='Tirupati')&(df['destination']=='Manglore')&(df['Selected_bus']=='APSRTC')&(df['seat_type']=='NON-AC'),['Seat_number']]
# # # lst=dff.tolist()
# # booked_lst=dff['Seat_number'].tolist()
# # available_seats=list(set(range(1,31))-set(booked_lst))
# # print(booked_lst,end="\n")
# person_details=df[['Booking_Id','name','phone','Seat_number']].drop_duplicates()
# detta=df.drop(columns=['name','phone','Seat_number'])
# detta=detta.apply(lambda x: x.strip() if isinstance(x,str) else (round(x,0) if isinstance(x,(int,float)) else x))
# # detta.round(decimals=5).drop_duplicates(inplace=True)
# detta.drop_duplicates(inplace=True)
# # booking_data=df.loc[df['Booking_Id']==int(booking_id),~df.columns.isin(['name','phone','Seat_number'])].drop_duplicates().to_dict(orient='records')    
   ## demder method
# # print(detta.columns)
places={'Hyderbad': (17.38504, 78.48667),
    'Chennai': (13.08268, 80.27072),
    'Palamaner': (13.2010, 78.7490),
    'Tirupati': (13.6288, 79.4192),
    'Manglore': (12.9141, 74.8560),
    'Delhi': (28.6139, 77.2090),
    'Banglore': (12.9716, 77.5946),
    'Pune': (18.5204, 73.8567),
    'bangarupalyam':(13.19623,78.9133) }#jio location on bangarupalyam
distance = hs.haversine(places['Palamaner'], places['bangarupalyam'], unit=Unit.KILOMETERS)
distant = round(distance,2)
print(distant)
