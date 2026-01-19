from flask import Flask, request, render_template,redirect,url_for
import pandas as pd
import os
import csv
import random
import haversine as hs
from haversine import Unit
app = Flask(__name__)

dictt ={}
def append_data(booking_id,name,phone,src,dst,distant,price,seat_type,bus_selection,seat_number,no_pass,total_price):
    csv_path='booking.csv'
    if os.path.exists(csv_path):
        with open(csv_path,mode='a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow([booking_id,name,phone,src,dst,distant,price,seat_type,bus_selection,seat_number,no_pass,total_price])
    else:
        with open(csv_path,mode='w',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Booking_Id','name','phone','source','destination','distance','price','seat_type','Selected_bus','Seat_number','No_passengers','Total_price'])
    return True
places={'Hyderbad': (17.38504, 78.48667),
    'Chennai': (13.08268, 80.27072),
    'Palamaner': (13.2010, 78.7490),
    'Tirupati': (13.6288, 79.4192),
    'Manglore': (12.9141, 74.8560),
    'Delhi': (28.6139, 77.2090),
    'Banglore': (12.9716, 77.5946),
    'Pune': (18.5204, 73.8567)}

@app.route('/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        src_var = request.form['source']
        dst = request.form['destination']
        return redirect(url_for("book",src=src_var,dst=dst))
    return render_template('index.html')

@app.route('/book',methods=['GET','POST'])
def book():
    s=request.args.get('src')
    d=request.args.get('dst')
    print(s,d)
    distance = hs.haversine(places[s], places[d], unit=Unit.KILOMETERS)
    distant = round(distance,2)
    price = round(int(distant) * 1.85,2)
    booking_id = random.randint(1000000000,9999999999)
    if request.method=='POST':
        no_pass = request.form.get('no_pass')
        buss_type = request.form.get('bus_type')
        bus_selection = request.form.get('bus_selection')
        total_price = request.form.get('total_price')
        df = pd.read_csv('booking.csv')
        dff=df.loc[(df['source']==s)&(df['destination']==d)&(df['Selected_bus']==bus_selection)&(df['seat_type']==buss_type),['Seat_number']]
        booked_lst=dff['Seat_number'].tolist()
        available_seats=list(set(range(1,31))-set(booked_lst))
        if len(available_seats)<int(no_pass):
            return redirect(url_for("alert_noseat",message=f"Required {no_pass} Seats Not Avaialble Seats available {len(available_seats)} Try Again ,..Thank You",redirect_url="/",booking_id="None",alert_type='danger'))
        for i in range(1,int(no_pass)+1):
            username = request.form.get(f'name{i}')
            phone = request.form.get(f'phone{i}')
            dff=df.loc[(df['source']==s)&(df['destination']==d)&(df['Selected_bus']==bus_selection)&(df['seat_type']==buss_type),['Seat_number']]
            booked_lst=dff['Seat_number'].tolist()
            available_seats=list(set(range(1,31))-set(booked_lst))
            seat_number = random.choice(available_seats)
            append_data(booking_id,username,phone,s,d,distant,price,buss_type,bus_selection,seat_number,no_pass,total_price)
        return redirect(url_for("alert_noseat",message=f"{no_pass} Seats Booked successfully \n Booking Id {booking_id} \n Thanks For Choosing Our site...Happy Journey",redirect_url="/Bill",booking_id=int(booking_id),alert_type='success'))
        # return redirect(url_for("Bill",booking_id=booking_id))
    return render_template('Book.html',booking_id=booking_id,src=s,dst=d,distance=distant,price=price)

@app.route('/Bill',methods=['GET','POST'])
def Bill():
    booking_id=request.args.get('booking_id')
    df = pd.read_csv('booking.csv')
    if int(booking_id) in df.values:
        person_details=df.loc[df['Booking_Id']==int(booking_id),['name','phone','Seat_number']].to_dict(orient='records')
        booking_data=df.loc[df['Booking_Id']==int(booking_id),~df.columns.isin(['name','phone','Seat_number'])].drop_duplicates().to_dict(orient='records')    
    return render_template('Bill.html',invoices=booking_data,person_details=person_details)

@app.route('/admin_login',methods=['GET','POST'])
def admin_login():
    if request.method == 'POST':
        usr = request.form['username']
        psw = request.form['password']
        if usr =='Madhan' and psw == 'Madhan2001@mr':
            return redirect(url_for("alert_noseat",message=f"Login successfull Loading....Admin Page......",redirect_url="/admit",booking_id='',alert_type='success'))
        else:
            return redirect(url_for("alert_noseat",message=f"Login failed Incorrect username or password",redirect_url="/admin_login",booking_id='',alert_type='danger'))

    return render_template('login.html')



@app.route('/admit',methods=['GET','POST'])
def admit():
    df = pd.read_csv('booking.csv')
    df1=df
    summary_df = (df.groupby(["source", "destination", "seat_type", "Selected_bus"]).agg(no_seats_booked=("Booking_Id", "count"),total_amount=("Total_price", "sum")).reset_index().rename(columns={"seat_type": "seattype","Selected_bus": "bustype"}))
    summary_df["no_empty_seats"] = 30-summary_df["no_seats booked] 
    person_details=df[['Booking_Id','name','phone','Seat_number']].drop_duplicates().to_dict(orient='records')
    detailed_records=df1.drop(columns=['name','phone','Seat_number']).drop_duplicates().to_dict(orient='records')  
    return render_template('admit.html',invoices=detailed_records,person_details=person_details)

@app.route('/alert_noseat',methods=['GET','POST'])
def alert_noseat():
    message=request.args.get('message')
    booking_id=request.args.get('booking_id')
    alert_type=request.args.get('alert_type')
    redirect_url=request.args.get('redirect_url')
    return render_template('alert.html',message=message,redirect_url=redirect_url,booking_id=booking_id,alert_type=alert_type)

if __name__ == '__main__':
    app.run(debug=True)
