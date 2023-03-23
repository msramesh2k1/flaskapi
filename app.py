#performing flask imports
from flask import Flask,jsonify
import requests
import json


app = Flask(__name__) #intance of our flask application 

#Route '/' to facilitate get request from our flutter app
@app.route('/', methods = ['GET','POST'])


 
def index():
    headers = {"Content-Type": "application/json; charset=utf-8",
             "x-api-version" : "2022-09-01",
               "x-client-id" :"TEST34816092a7954fcb7998350c53061843",
               "x-client-secret" : "TEST1ca6f237d6fedfa174b5719edc9b4137f1d32ccf"
               
              
                 }
    dbody = {
    "customer_details": {
        "customer_id": "7112AAA812234",
        "customer_email": "msramesh2k1@gmail.com",
        "customer_phone": "7010862331"
    },"order_meta": {
        "notify_url": "https://webhook.site/0578a7fd-a0c0-4d47-956c-d02a061e36d3"
    },
    "order_amount": 30.00,
    "order_currency": "INR"
}
    req = requests.post('https://sandbox.cashfree.com/pg/orders' ,headers=headers, json=dbody  )
    data = json.loads(req.content)
    # print(req.content)
    print(data['payment_session_id'])
    # print(data[0])
    # return "hello"
    return  '{}  + " Sesssion ID "  +  {}'.format(str(data['cf_order_id']) ,str(data['payment_session_id']))    #returning key-value pair in json format


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug = True) #debug will allow changes without shutting down the server 