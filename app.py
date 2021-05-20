from flask import Flask, render_template, request, redirect
import requests
from datetime import date
import json

app = Flask(__name__)
print(__name__)

@app.route('/')
@app.route('/<id>')
def home(id='363'):
    today = date.today().strftime("%d-%m-%Y")
    age = request.args.get("age")
    age = 18 if age != '45' else 45

    dummy = True if request.args.get("dummy") == 'true' else False
    print(request.args.get("dummy"))

    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+str(id)+"&date="+today

    payload={}
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Accept": '*/*',
        "Accept-Encoding": 'gzip, deflate, br',
        "User-Agent": "PostmanRuntime/7.26.8"
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_text = response.json();

    if dummy == True:
        response = open('dummy.json',)
        response_text = json.load(response)

    def filter_age(centers):
        filtered_center = [];
        for center in centers:
            newSession = []
            flag = False;
            for session in center['sessions']:
                if session['min_age_limit'] == age and session['available_capacity'] > 0 :
                    newSession.append(session);
                    flag = True;

            if flag == True :
                center['sessions'] = newSession
                filtered_center.append(center)
               
                    
        return filtered_center;

    # print(response_text['centers']);


    res = filter_age(response_text['centers'])
    if len(res) and age==18 and (id == '154' or id == '363'):
        ifttt_webhook_url1 = 'https://maker.ifttt.com/trigger/vaccine/with/key/bMd5VRSXwc7EXXySzbSVR'
        ifttt_webhook_url2 = 'https://maker.ifttt.com/trigger/vaccine/with/key/dDJENlOeoIpu_ZDVMNAmZTW8E1o0HarfqVmgsRIc1_P'
        
        city = 'Ahmedabad' if id=='154' else 'Pune'
        data = {
            'value1': city
        }

        if dummy == True:
            data = {
                'value1': "Dummy-" +city
            }
        requests.post(ifttt_webhook_url1, data=data)
        requests.post(ifttt_webhook_url2, data=data)

    return render_template('index.html', result = res, id=id, length=len(res))