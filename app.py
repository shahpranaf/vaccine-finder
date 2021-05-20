from flask import Flask, render_template, request, redirect
import requests
from datetime import date
import json

app = Flask(__name__)
print(__name__)

@app.route('/')
def home():
    today = date.today().strftime("%d-%m-%Y")
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=363&date="+today

    payload={}
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Accept": '*/*',
        "Accept-Encoding": 'gzip, deflate, br',
        "User-Agent": "PostmanRuntime/7.26.8"
    }

    # response = requests.request("GET", url, headers=headers, data=payload)
    # response_text = response.text;

    response_text = {
    "centers": [
        {
            "center_id": 694629,
            "name": "KOHINOOR PUB PARKING (DRIVE)",
            "address": "Kohinoor Public Parking Lot Harishchandra Yewale Marg Dadar West Mumbai-28",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward G North Corporation - MH",
            "pincode": 400028,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "796a165c-967c-447e-be5f-76fe61028004",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 700372,
            "name": "Om Siddhivinayak Sra Bldg P1 3",
            "address": "Behind Kasturba Police Station Carter Road No 1boriwali East",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward R Central Corporation - MH",
            "pincode": 400066,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "0821727d-c673-403c-beab-f9d3439a8625",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 698789,
            "name": "World Trade MCGM Centre Colaba",
            "address": "World Trade MCGM Centre Ground Floor W G Union Road Azad Nagar Colaba",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward A Corporation - MH",
            "pincode": 400005,
            "lat": 18,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "1af79361-e7a0-47c1-962b-d5de0cfa2fda",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 578106,
            "name": "NESCO 1",
            "address": "GOREGAON (EAST) WESTERN EXPRESS HIGHWAY",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward P South Corporation - MH",
            "pincode": 400063,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "56208cbe-d45f-4403-b493-7f7c00afdda8",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                },
                {
                    "session_id": "fb53a481-6522-4a99-8d3b-ff53b4ea36d0",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVAXIN",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 688176,
            "name": "Worli Koliwada Dispensary",
            "address": "Worli Koliwada Kesribuvabhai Marg Near Police Chowki",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward G South Corporation - MH",
            "pincode": 400030,
            "lat": 19,
            "long": 73,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "5ce6eb73-a197-44f7-96c0-a4c8cf84d280",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 670466,
            "name": "GOKULDHAM MAT HOME GOREGAON(E)",
            "address": "19 Krishna Vatika Marg Yashodham Goregaon Mumbai Maharashtra 400063",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward P South Corporation - MH",
            "pincode": 400063,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "b9ab39e6-d46d-4232-b977-92882495fa6b",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 694498,
            "name": "BMC MURLI DEVRA NETRA RUGNALAY",
            "address": "197 1- 13 MS Ali Rd Opp Durgadevi Garden Kamathipura",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward E Corporation - MH",
            "pincode": 400008,
            "lat": 18,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "68a71fe4-d40c-41b5-b98d-713af45305ba",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 700683,
            "name": "Rangsharda Hotel Hall P.-102",
            "address": "Rangsharda Hotelrahul Nagarbehind Apapt Ngok.c.margnear Lilavati Hospitalbandra Westmumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward H West Corporation - MH",
            "pincode": 400050,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "f18f8c97-4db1-45a6-97c8-7d2ba302da24",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 597031,
            "name": "KOKILABEN HOSPITAL 1",
            "address": "Four Bungalow Andheri West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K West Corporation - MH",
            "pincode": 400053,
            "lat": 19,
            "long": 72,
            "from": "09:00:00",
            "to": "18:00:00",
            "fee_type": "Paid",
            "sessions": [
                {
                    "session_id": "26adf1ed-b7b8-4a11-a9a3-5f1d5f7bf404",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 18,
                    "vaccine": "COVAXIN",
                    "slots": [
                        "09:00AM-11:00AM",
                        "11:00AM-01:00PM",
                        "01:00PM-03:00PM",
                        "03:00PM-06:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                },
                {
                    "session_id": "91936d0b-0dcc-403f-bd9c-25f7612e2592",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVAXIN",
                    "slots": [
                        "09:00AM-11:00AM",
                        "11:00AM-01:00PM",
                        "01:00PM-03:00PM",
                        "03:00PM-06:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ],
            "vaccine_fees": [
                {
                    "vaccine": "COVAXIN",
                    "fee": "1250"
                }
            ]
        },
        {
            "center_id": 700243,
            "name": "Lokbharati Garden Marol HP",
            "address": "Lokbharati Garden Marol ANdheri East 400059",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K East Corporation - MH",
            "pincode": 400059,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "354d5c73-0657-4b50-bbb3-37386f36a98c",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 700269,
            "name": "JSS Municipal School P 217",
            "address": "JSS Municipal School Grant Road Nanachowk Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward D Corporation - MH",
            "pincode": 400007,
            "lat": 18,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "b032b431-a159-435e-926e-bf27b14299b4",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                },
                {
                    "session_id": "f9e7fc87-8550-4d51-84c9-316a4f5c76d0",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVAXIN",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 695525,
            "name": "PWD COMMUNITY HALL H EAST",
            "address": "J.L. SHIRSEKAR MARG GOVERNMENT COLONY BANDRA EAST",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward H East Corporation - MH",
            "pincode": 400051,
            "lat": 19,
            "long": 72,
            "from": "11:00:00",
            "to": "16:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "d3e75f3a-760d-408c-8f0f-f27e0120f144",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVAXIN",
                    "slots": [
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-02:00PM",
                        "02:00PM-04:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                },
                {
                    "session_id": "5d442b04-0aeb-42e2-b172-4f26b2144696",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-02:00PM",
                        "02:00PM-04:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 699274,
            "name": "PRABODHANKAR THAKRE HALL P202",
            "address": "Prabodhankar Thakre Marg Sewri West Shivaji Nagar Parel Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward F South Corporation - MH",
            "pincode": 400015,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "c31e546e-4b1c-4fde-9816-970dcd383b44",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 594089,
            "name": "CAMA SESSION 1",
            "address": "Mahapalika Marg BMC Office Opp. Azad Maidan Mumbai Maharashtra",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward A Corporation - MH",
            "pincode": 400001,
            "lat": 0,
            "long": 0,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "9bac02c8-34ac-4569-9591-184d467c9f5d",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                },
                {
                    "session_id": "183da4da-da36-49de-a41a-c2af773d7ef4",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVAXIN",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 594392,
            "name": "H N Reliance Hospital",
            "address": "Raja Rammohan Roy Road Prarthana Samaj Girgaon",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward C Corporation - MH",
            "pincode": 400004,
            "lat": 18,
            "long": 72,
            "from": "09:00:00",
            "to": "13:00:00",
            "fee_type": "Paid",
            "sessions": [
                {
                    "session_id": "1b1a427e-9265-4244-8216-54d50e73acfc",
                    "date": "19-05-2021",
                    "available_capacity": 48,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "09:00AM-10:00AM",
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 48
                },
                {
                    "session_id": "c8da6696-1a6b-474d-a94b-c49fb8e4cdfb",
                    "date": "19-05-2021",
                    "available_capacity": 23,
                    "min_age_limit": 18,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "09:00AM-10:00AM",
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 23
                },
                {
                    "session_id": "c8da6696-1a6b-474d-a94b-c49fb8e4cdfb",
                    "date": "19-05-2021",
                    "available_capacity": 30,
                    "min_age_limit": 18,
                    "vaccine": "COVAXIN",
                    "slots": [
                        "09:00AM-10:00AM",
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 23
                }
            ],
            "vaccine_fees": [
                {
                    "vaccine": "COVISHIELD",
                    "fee": "700"
                }
            ]
        },
        {
            "center_id": 584183,
            "name": "BHAGWATI HOSPITAL 1",
            "address": "SVP Road Borivali West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward R North Corporation - MH",
            "pincode": 400092,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "12d1dd39-05c3-44bd-b052-fe188897139d",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 698745,
            "name": "AMBOLISHWAR MANDIR HALL",
            "address": "OFF CAREE RD NEAR SHIVSENA SHAKHA ANDHERI (W)",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K West Corporation - MH",
            "pincode": 400058,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "bebe295c-8050-4a32-b2c1-9ea149f806e7",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 583008,
            "name": "Kasturba Hospital 01",
            "address": "Kasturba Hospital Sane Guruji Ma Chinchpokli",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward E Corporation - MH",
            "pincode": 400011,
            "lat": 18,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "8e21d349-9186-4327-bab0-82974783f50d",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVAXIN",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                },
                {
                    "session_id": "2d9bbb0f-a70b-44a3-a302-3a5da2676cd1",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "09:00AM-11:00AM",
                        "11:00AM-01:00PM",
                        "01:00PM-03:00PM",
                        "03:00PM-05:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 702155,
            "name": "Ghatkopar Police Ground P125",
            "address": "Ghatkopar Police Ground Pant Nagar  Ghatkopar East",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward N Corporation - MH",
            "pincode": 400075,
            "lat": 19,
            "long": 72,
            "from": "12:00:00",
            "to": "17:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "5c5f3e68-0c95-46eb-925b-443e70b88933",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "12:00PM-01:00PM",
                        "01:00PM-02:00PM",
                        "02:00PM-03:00PM",
                        "03:00PM-05:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 644281,
            "name": "TATA MEMORIAL HOSPITAL PAREL",
            "address": "Dr. E Borges Road Parel Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward F South Corporation - MH",
            "pincode": 400012,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "4203e77a-042b-48c0-a22e-7c2ab47f30e0",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 696041,
            "name": "Squatter Colony HP- E Library",
            "address": "E LibraryIcchapurti Ganesh Mandir Road Jogeshwari East.",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K East Corporation - MH",
            "pincode": 400060,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "b91ca1c0-a564-4870-ac8e-b0c68110eeba",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 614417,
            "name": "Mahim Municipal Maternity Home",
            "address": "Lieutenant Dilip Gupte Marg Mahim West Mahim Mumbai Maharashtra 400016",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward G North Corporation - MH",
            "pincode": 400016,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "a9bf72ef-cd01-47d3-8314-5cc1548562d3",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 699638,
            "name": "COLABA HP LINKED RADIO CLUB",
            "address": "Arthur Bunder Road Colaba Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward A Corporation - MH",
            "pincode": 400005,
            "lat": 18,
            "long": 72,
            "from": "10:00:00",
            "to": "15:30:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "58a49964-e3f0-4a61-8863-101dc096b2e6",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:30PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 694484,
            "name": "Naigaon Maternity Home",
            "address": "Naigaon Maternity Home Daivalkar Hua Marg Near Police Ground",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward F South Corporation - MH",
            "pincode": 400014,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "731d5f61-df75-421b-a510-d83551001889",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 704027,
            "name": "CWC Institute 59",
            "address": "Sai Nagar Yari Road Versova Andheri West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K West Corporation - MH",
            "pincode": 400061,
            "lat": 19,
            "long": 72,
            "from": "12:00:00",
            "to": "17:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "b7db7ff5-5f2d-42a4-8174-11602f9d1c3e",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "12:00PM-01:00PM",
                        "01:00PM-02:00PM",
                        "02:00PM-03:00PM",
                        "03:00PM-05:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 681813,
            "name": "CHARKOP SEC 1 DISP.KANDIVALI",
            "address": "Ambedkar Road Near BMC School Kandivali West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward R South Corporation - MH",
            "pincode": 400067,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "5af8aded-cae4-4b03-9363-3ee9cc8d5a40",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 696472,
            "name": "Willingdon DRIVE IN 60yr PLUS",
            "address": "Willingdon Sports Club K Khadey Marg Tardeo Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward D Corporation - MH",
            "pincode": 400034,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "f44d100f-bff9-4753-bdbd-62255757e281",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 596469,
            "name": "NANAVATI HOSPITAL 1",
            "address": "Mumbai - Vile Parle",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K West Corporation - MH",
            "pincode": 400056,
            "lat": 19,
            "long": 72,
            "from": "16:00:00",
            "to": "18:00:00",
            "fee_type": "Paid",
            "sessions": [
                {
                    "session_id": "fdbdc1fb-5c82-4484-a5d1-8780d1a5fd5b",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "04:00PM-06:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                },
                {
                    "session_id": "c717b1c7-b98d-49f0-880a-0c5994a5b05c",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 18,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "09:00AM-11:00AM",
                        "11:00AM-01:00PM",
                        "01:00PM-03:00PM",
                        "03:00PM-06:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ],
            "vaccine_fees": [
                {
                    "vaccine": "COVISHIELD",
                    "fee": "900"
                }
            ]
        },
        {
            "center_id": 23613,
            "name": "Anand Nagar HP ANDHERI W",
            "address": "43 Parth Tower Link RoadNext To Mira Tower Jogeshwari (W) 400103",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K West Corporation - MH",
            "pincode": 400102,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "3c37f258-1cd9-4f34-9305-bee4158a3dfa",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 612360,
            "name": "JJ Hospital 2",
            "address": "J J Marg Nagpada-Mumbai Central J J Marg Nagpada-Mumbai Central Mazgaon Mumbai Maharashtra",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward E Corporation - MH",
            "pincode": 400008,
            "lat": 18,
            "long": 72,
            "from": "10:00:00",
            "to": "13:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "b72a08a0-5b1b-415b-aeb1-8b30ff739612",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-12:00PM",
                        "12:00PM-01:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 694639,
            "name": "Central Rail Off Waiting Room",
            "address": "Platform No 18 CST Station  P Demello Road CST Mumbai -400001",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward A Corporation - MH",
            "pincode": 400001,
            "lat": 18,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "4ad31303-f521-4b77-8fd0-760a2f5f874f",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 630364,
            "name": "Rajawadi Hospital Ghatkopar(E)",
            "address": "Rajawadi Hospital Vidhyavihar Ghatkopar E",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward N Corporation - MH",
            "pincode": 400077,
            "lat": 19,
            "long": 72,
            "from": "09:00:00",
            "to": "17:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "64219ad8-d158-40cc-b266-50fcf9c3768b",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVAXIN",
                    "slots": [
                        "09:00AM-11:00AM",
                        "11:00AM-01:00PM",
                        "01:00PM-03:00PM",
                        "03:00PM-05:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 695693,
            "name": "Tata Compound HP Adhar Kendra",
            "address": "Lallu Bhai Park Road Vile Parle West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K West Corporation - MH",
            "pincode": 400056,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "7bb58f85-ac93-4133-85b5-48291dc9203d",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 700262,
            "name": "BPK Sahakari V Mandir P 215",
            "address": "BPK SAHAKARI VIDHYA MANDIR TARDEO ROAD MUMBAI",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward D Corporation - MH",
            "pincode": 400034,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "f228eaf9-38de-4cc1-9a56-0d2584655e0d",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 30401,
            "name": "Charkop Maternity Home",
            "address": "Sec 3 Near Provident Fund Office Kandivali West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward R Central Corporation - MH",
            "pincode": 400067,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "c6cc9f1d-e37e-4ba4-91ab-e7ecf4d6a7a1",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 620921,
            "name": "RCF Hospital",
            "address": "RCF ColonyBehind Ashish Cinema Chembur",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward M East Corporation - MH",
            "pincode": 400074,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "c2c89695-9618-4374-b621-0cc49abcf917",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                },
                {
                    "session_id": "c10d8ce5-326a-48e6-820c-25d8cc3eb1dc",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVAXIN",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 702076,
            "name": "CGHS Wellness Center P 175",
            "address": "219 CC.G.S Colony Antop Hill Road Mothilal Nehru Nagar Sector 7CGS Colony Antop Hill Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward F North Corporation - MH",
            "pincode": 400037,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "50c72ed4-88ae-4d97-915c-f6ac59d4869f",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 699588,
            "name": "MCF SPORTS COMPLEX",
            "address": "Gymkhana Road Prem Nagar Borivali West 400092",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward R Central Corporation - MH",
            "pincode": 400092,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "e83501ec-ea07-4a2f-ae5e-378e88c2e4ad",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 698768,
            "name": "Bhandup Village Mat.P 111 HP",
            "address": "Bhandup Village Maternity Building Juvekar Marg Bhandup Village Bhundap",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward S Corporation - MH",
            "pincode": 400042,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "b5aae7a5-2e5c-4324-b79a-16b8e15b02d2",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 685278,
            "name": "APPAPA MATERNITY HOME MALAD",
            "address": "ANAND NAGAR APPAPADA MALAD EAST",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward P North Corporation - MH",
            "pincode": 400097,
            "lat": 19,
            "long": 19,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "5806cdee-480c-467e-88e2-a1a01da166a3",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 694516,
            "name": "Chandraprabhu Jain Temple",
            "address": "ZAOBAWADI HEALTH POST JAIN TEMPLE BHULESWAR MUMBAI",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward C Corporation - MH",
            "pincode": 400002,
            "lat": 18,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "e0743170-1f99-44f9-9301-08bc1a8279cf",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 696413,
            "name": "SRA Building Ghatkopar East",
            "address": "SRA Building Kamraj Nagar",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward N Corporation - MH",
            "pincode": 400077,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "6f050e1a-7481-4b04-a00f-a8fb4d9f2556",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 659877,
            "name": "Mithanagar Mun. School Mulund",
            "address": "Mithanagar Municipal School Mithanagar Road Mulund East",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward T Corporation - MH",
            "pincode": 400081,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "11c9187e-a15c-494a-8ee6-1882ddfc687d",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 700170,
            "name": "Shivalik Venture Office",
            "address": "Shivalik Builder Sales Office Near Shri Sai Mandir Golibar Road Khar East",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "",
            "pincode": 400051,
            "lat": 19,
            "long": 72,
            "from": "11:00:00",
            "to": "16:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "1a590784-3023-4982-807d-094076419650",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-02:00PM",
                        "02:00PM-04:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 699071,
            "name": "Nagpada Police Hospital",
            "address": "Sophia Zuber Road Nagpada-mumbai Central Mumbai - 400008 Near Cafe Sagar Restaurant (Map)",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward E Corporation - MH",
            "pincode": 400008,
            "lat": 18,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "98f752a2-f195-4490-86dd-d9e9e8157137",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 700369,
            "name": "Shantidham Prathnalay P 16",
            "address": "Amarkant Jha Road Shimpoli Kastur Park Boriwali West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward R Central Corporation - MH",
            "pincode": 400092,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "f8c5876f-d63b-49fe-aa62-afe95d37e9cc",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 691967,
            "name": "SHREE CINEMA MUN DISP MAHIM",
            "address": "DILIP GUPTE ROAD OPP GOA PORTUGUESE HOTEL MAHIM",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward G North Corporation - MH",
            "pincode": 400016,
            "lat": 0,
            "long": 0,
            "from": "14:00:00",
            "to": "20:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "d6988fcd-3d77-434f-8973-572abf1a698b",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "02:00PM-03:00PM",
                        "03:00PM-04:00PM",
                        "04:00PM-05:00PM",
                        "05:00PM-08:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 699403,
            "name": "Shyam Satsang Hall",
            "address": "Adarsh Nagar Shravan Nagar Kandivali West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward R South Corporation - MH",
            "pincode": 400067,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "daef3d32-45de-4cde-a6eb-483e43e46f69",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 23808,
            "name": "CIVIC TRANING RESEARCH CENTER",
            "address": "Abhinav Nagar Borivali East",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward R Central Corporation - MH",
            "pincode": 400066,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "c78d60bf-cb42-4a92-b581-6c95b2e1cdc1",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 627697,
            "name": "Family Clinic NNN For Navy 1",
            "address": "NAVY NEW NAVY NAGAR COLABA",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward A Corporation - MH",
            "pincode": 400005,
            "lat": 18,
            "long": 72,
            "from": "09:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "7c4050b1-cc73-4afc-9dbe-c3b7f04ac87c",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "09:00AM-10:00AM",
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 562287,
            "name": "JJ Hospital Covaxin",
            "address": "J J Marg Nagpada-Mumbai Central J J Marg Nagpada-Mumbai Central Mazgaon Mumbai Maharashtra",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward E Corporation - MH",
            "pincode": 400008,
            "lat": 18,
            "long": 72,
            "from": "10:00:00",
            "to": "14:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "bd63b0ef-89e3-447f-8933-54cccd06f2ae",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVAXIN",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-02:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 561990,
            "name": "KEM Hospital 1",
            "address": "Acharya Donde Marg parel mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward F South Corporation - MH",
            "pincode": 400012,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "b05541af-d71f-409a-b998-6628edb71037",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVAXIN",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                },
                {
                    "session_id": "6a24dcf5-b543-41f1-9899-6c4f15995cf9",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "09:00AM-11:00AM",
                        "11:00AM-01:00PM",
                        "01:00PM-03:00PM",
                        "03:00PM-05:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 695692,
            "name": "Oshiwara HP Community Hall",
            "address": "Oshiwara Community Hall",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K West Corporation - MH",
            "pincode": 400102,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "aebbc253-917a-46b3-8215-77becb493f67",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 637921,
            "name": "SK PATIL HOSPITAL MALAD MUMBAI",
            "address": "Daftari Road Near Pushpa Park Malad East",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward P North Corporation - MH",
            "pincode": 400097,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "0a778370-2045-4666-9fe0-6d93419dafaf",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVAXIN",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 561565,
            "name": "Bhabha Hospital Bandra 1",
            "address": "R.K.Patkar Road",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward H West Corporation - MH",
            "pincode": 400050,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "54a1c16e-19c9-464e-a521-afaabd4d71c7",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 696299,
            "name": "Sarvoday Nagar HP Gurudwara",
            "address": "Gurudwara Shere-E-Punjab Jijamata Road Andheri (East) PRABHAG 79",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K East Corporation - MH",
            "pincode": 400093,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "46e6ef9e-d7ec-40cd-9d61-a57ff89be87f",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 651121,
            "name": "ESIS HOSPITAL WORLI",
            "address": "ESIS Hospital G.K Marg Behind Poddar Hospital Worli",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward G South Corporation - MH",
            "pincode": 400018,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "10571dc5-b652-4314-b0b5-3b215958d966",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 695242,
            "name": "Apollo Spectra Hospital Deonar",
            "address": "Ujagar Compound Opp. Deonar Bus Depot Main Gate Deonar Chembur Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward M East Corporation - MH",
            "pincode": 400088,
            "lat": 19,
            "long": 72,
            "from": "11:00:00",
            "to": "15:00:00",
            "fee_type": "Paid",
            "sessions": [
                {
                    "session_id": "a67b7274-185f-4fe5-b5eb-552ab908b310",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 18,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-02:00PM",
                        "02:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ],
            "vaccine_fees": [
                {
                    "vaccine": "COVISHIELD",
                    "fee": "850"
                }
            ]
        },
        {
            "center_id": 685800,
            "name": "AKURLI MATERNITY KANDIVALI",
            "address": "Akurli Mat HomeThakur Village  Kandivali (East)",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward R South Corporation - MH",
            "pincode": 400101,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "79cabb95-1e4e-487c-a551-0521f63ad502",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 659851,
            "name": "Shivaji Nagar Covid Centre",
            "address": "AHILYABAI HOLKKAR MARG SHIVAJI NAGAR GOVANDI EAST MUMBAI",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward M East Corporation - MH",
            "pincode": 400043,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "946276ee-dd3d-42a9-bcb4-13b51b4d2eec",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 23682,
            "name": "Malwani Government Hosp.Malad",
            "address": "Jan Kalyan Nagar Bhumi Park Malad West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward P North Corporation - MH",
            "pincode": 400095,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "5fd25a68-9f5c-4c2f-bd8a-bf5749222025",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 27450,
            "name": "Banganga HP Center Camp",
            "address": "Kawdemath Municipal School Dongarsi Road",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward D Corporation - MH",
            "pincode": 400006,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "120ec77e-2abf-4029-ba94-69214723bb68",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 699433,
            "name": "Symphony Building Center",
            "address": "Symphony Building Welfare Center Kandivali West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward R South Corporation - MH",
            "pincode": 400067,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "c748a54e-156f-445f-a9f4-7514ec6be172",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 556228,
            "name": "BDBA Hospital 1",
            "address": "S V ROAD KANDIVALI WEST",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward R South Corporation - MH",
            "pincode": 400067,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "3ef57e20-22e0-4b78-9a80-d39667aa31c9",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 698038,
            "name": "Atal Smriti Udyan Borivali",
            "address": "Opp Shimpoli Telephone Exchange Shimpoli Road Borivali West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward R Central Corporation - MH",
            "pincode": 400092,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "bc826a1b-f6fa-47dd-81f2-52ec3ff7a1fe",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 688193,
            "name": "TOPIWALA DISPENSARY",
            "address": "Topiwala Dispensary Station Road Opp I B Patel Muncipal School Near Railway Stn.Goregoan West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward P South Corporation - MH",
            "pincode": 400064,
            "lat": 19,
            "long": 72,
            "from": "14:00:00",
            "to": "18:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "cd7dea44-299a-4ea8-9f2d-38417cb3bc52",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "02:00PM-03:00PM",
                        "03:00PM-04:00PM",
                        "04:00PM-05:00PM",
                        "05:00PM-06:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 694800,
            "name": "Najam Baug",
            "address": "Najam Baug Vaccination Center Samantbhai Nanji Marg Noor BaugDongri Umerkhadi Mumbai Maharashtra",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward B Corporation - MH",
            "pincode": 400009,
            "lat": 18,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "2cb4c535-17b9-41eb-aadd-377f1ac27a2b",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 700143,
            "name": "BMC Facility Community Centre",
            "address": "6282 A Pride Of Kalina Sunder Nagar Rd No 2 Santacruz East",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward H East Corporation - MH",
            "pincode": 400055,
            "lat": 19,
            "long": 72,
            "from": "11:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "2f39eb27-6c59-4c1a-9634-6a48233200da",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-02:00PM",
                        "02:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 582425,
            "name": "Maa Hospital 1 -Chembur",
            "address": "Postal Colony Road Chembur (E)",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward M West Corporation - MH",
            "pincode": 400071,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "2db1ce43-8701-456d-8474-48050a944d96",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 561621,
            "name": "BKC Jumbo COVID Facility 1",
            "address": "MMRDA GROUND BKC MUMBAI",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward H East Corporation - MH",
            "pincode": 400051,
            "lat": 0,
            "long": 0,
            "from": "10:00:00",
            "to": "18:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "59468238-f020-4feb-8b24-66233bba3987",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-12:00PM",
                        "12:00PM-02:00PM",
                        "02:00PM-04:00PM",
                        "04:00PM-06:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 579049,
            "name": "NAIR HOSPITAL- MUMBAI CITY",
            "address": "Dr. A L Nair Road Mumbai Central Mumbai - 400008 Near Martha Mandir",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward E Corporation - MH",
            "pincode": 400008,
            "lat": 18,
            "long": 69,
            "from": "10:00:00",
            "to": "16:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "b883e4ce-f595-4292-884f-db6f7abdae74",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVAXIN",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-04:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 700624,
            "name": "Harmony Hall S. V .Road HP",
            "address": "Harmony Hallopposite Rizvi College Of Engineeringsherly Village Roadkhar Westmumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward H West Corporation - MH",
            "pincode": 400052,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "844f8064-7cab-4f75-a6f7-111ede193c90",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 27468,
            "name": "R S Nimkar Health Post",
            "address": "R S Nimkar Marg Grant Road West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward D Corporation - MH",
            "pincode": 400007,
            "lat": 18,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "0a82e3b6-670a-4b90-813d-282c8d5f3321",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 561546,
            "name": "Nair Hospital 1",
            "address": "Dr. A L Nair Road Mumbai Central Mumbai - 400008 Near Martha Mandir",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward E Corporation - MH",
            "pincode": 400008,
            "lat": 0,
            "long": 0,
            "from": "09:00:00",
            "to": "17:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "5c46e8f9-882a-4953-aa12-dd953d8f3f3d",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "09:00AM-11:00AM",
                        "11:00AM-01:00PM",
                        "01:00PM-03:00PM",
                        "03:00PM-05:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                },
                {
                    "session_id": "d2561e28-37ce-4d4d-bcea-af2dc0fd06f2",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVAXIN",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 696047,
            "name": "Marol HP Pallotti Church",
            "address": "Pallotti Church Marol",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K East Corporation - MH",
            "pincode": 400059,
            "lat": 19,
            "long": 72,
            "from": "12:00:00",
            "to": "17:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "6ff578cc-267c-4e56-b96d-908a77a5e751",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "12:00PM-01:00PM",
                        "01:00PM-02:00PM",
                        "02:00PM-03:00PM",
                        "03:00PM-05:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 561602,
            "name": "Rajawadi Hospital 1",
            "address": "Rajawadi Hospital Vidhyavihar Ghatkopar (E)",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward N Corporation - MH",
            "pincode": 400077,
            "lat": 0,
            "long": 72,
            "from": "09:00:00",
            "to": "17:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "da68ddad-88ef-4699-a276-a271df545402",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "09:00AM-11:00AM",
                        "11:00AM-01:00PM",
                        "01:00PM-03:00PM",
                        "03:00PM-05:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 631316,
            "name": "MAA HOSPITAL CHEMBUR MUMBAI",
            "address": "POSTAL COLONY ROAD CHEMBUR ( E )",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward M West Corporation - MH",
            "pincode": 400071,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "ac4a93d1-2acd-4d51-9efb-c7c3730a92a8",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVAXIN",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 699974,
            "name": "Charkop Goan Maternity Home",
            "address": "Ground Floor Charkop Gaon Maternity Home Charkop Gaon Kandivali West Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward R South Corporation - MH",
            "pincode": 400067,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "00496bdd-55d9-4b73-a950-04038f69ad8c",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 699482,
            "name": "Saibaba Path BMC School P204",
            "address": "Saibaba Path Sankul Opp Best Colony Shri Sai Baba Marg Lalbaug Parel Near Finlay Mill Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward F South Corporation - MH",
            "pincode": 400012,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "f4d7ca00-6e6a-4dcc-8f4a-73420b52f882",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 650950,
            "name": "URBAN HEALTH CENTER DHARAVI",
            "address": "Urban Health Posts Building 60 Ft Road Dharavi 16",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward G North Corporation - MH",
            "pincode": 400019,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "0160aa6f-29ec-4420-82e1-80b64a36d497",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                },
                {
                    "session_id": "a1dfca20-e338-43e5-a840-b312da052868",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVAXIN",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 23910,
            "name": "ESIS Gh Kandiwali",
            "address": "ESIS Hospital  Ashok Nagar Kandivali (East)",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward R South Corporation - MH",
            "pincode": 400101,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "a11cf6ca-2bc1-4e4e-8fcf-7657973a7246",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 627444,
            "name": "ECHS Polyclinic INHS Asvini",
            "address": "NAVY RC CHURCH COLABA",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward A Corporation - MH",
            "pincode": 400005,
            "lat": 18,
            "long": 72,
            "from": "09:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "d1de6bc8-73c7-4d87-a7a6-ea8ae2d0a7b6",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "09:00AM-10:00AM",
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 703473,
            "name": "Poonam Darshan Sunder Nagar HP",
            "address": "Poonam Nagar Dispensary At Poonam Darshan B-Wing SVP Road Jogeshwari (E)",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K East Corporation - MH",
            "pincode": 400093,
            "lat": 19,
            "long": 72,
            "from": "12:00:00",
            "to": "17:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "03d6478c-6c82-40da-be94-a808f105139e",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "12:00PM-01:00PM",
                        "01:00PM-02:00PM",
                        "02:00PM-03:00PM",
                        "03:00PM-05:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 704305,
            "name": "SANT NIRANKARI SATSANG BHAVAN",
            "address": "Gandhi ChawlKranti Nagar Beat Chowky Ambedkar Chowk  Kranti Nagar  Kandivali East 400101",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward P North Corporation - MH",
            "pincode": 400101,
            "lat": 19,
            "long": 72,
            "from": "12:00:00",
            "to": "17:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "c7874268-de4b-44c2-b717-fa8f1f6dda01",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "12:00PM-01:00PM",
                        "01:00PM-02:00PM",
                        "02:00PM-03:00PM",
                        "03:00PM-05:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 696381,
            "name": "Shivaji Maidan Vikhroli",
            "address": "Shivaji Maidan Vikroli Parksite",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward N Corporation - MH",
            "pincode": 400079,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "4676be3f-7f6b-44bd-bef5-ff6e8dce427a",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 698811,
            "name": "Joshi Jagir Hall",
            "address": "Joshi Jagir Hall Near Parsiwada Cemetery Andheri East Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K East Corporation - MH",
            "pincode": 400099,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "e7ed4fd1-2563-4dcc-b3a2-d33096e2c17e",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 702026,
            "name": "Municipal School P-173",
            "address": "Pratiksha Nagar Muncipal School near Sundar Vihar opposite Of Ganesh MandirPratiksha Nagar BEST Bus Stop MUM",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward F North Corporation - MH",
            "pincode": 400022,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "1c21759c-9233-4eac-b148-5a80a1b54706",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 697988,
            "name": "Dindoshi Hall CVC",
            "address": "NEAR DINDOSHI BMC SCHOOL  GOREGAON EAST",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward P North Corporation - MH",
            "pincode": 400065,
            "lat": 19,
            "long": 72,
            "from": "09:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "c67a78c6-1a09-41d5-9433-60e2e8cbf759",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "09:00AM-10:00AM",
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 654160,
            "name": "SHIRODKAR MATERNITY HOME PARLE",
            "address": "Paranjape Scheme B Rd Number 1 Vishnu Prasad Society Navpada Vile Parle East Vile Parle Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K East Corporation - MH",
            "pincode": 400057,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "498898a7-1e73-42e3-acdf-129662b92300",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 638374,
            "name": "KEM Hospital MUMBAI",
            "address": "Acharya Donde Marg parel mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward F South Corporation - MH",
            "pincode": 400012,
            "lat": 19,
            "long": 72,
            "from": "09:00:00",
            "to": "17:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "81f5c10b-6add-41a8-b6ee-562f09de2582",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVAXIN",
                    "slots": [
                        "09:00AM-11:00AM",
                        "11:00AM-01:00PM",
                        "01:00PM-03:00PM",
                        "03:00PM-05:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 700216,
            "name": "BABASAHEB GAWDE CHARITABLE HOS",
            "address": "Moghibhai Market M.G.Road Vileparle (East)Mumbai 400057",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K East Corporation - MH",
            "pincode": 400057,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "f3efefa3-f827-4ba3-8a06-12aff7cc4c3d",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 628029,
            "name": "BKC COVID CENTER MUM SUBURBAN",
            "address": "MMRDA GROUND BKC MUMBAI",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward H East Corporation - MH",
            "pincode": 400051,
            "lat": 19,
            "long": 72,
            "from": "09:00:00",
            "to": "18:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "f3c4792c-5f1f-4a99-b487-f59030ec6cd7",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVAXIN",
                    "slots": [
                        "09:00AM-11:00AM",
                        "11:00AM-01:00PM",
                        "01:00PM-03:00PM",
                        "03:00PM-06:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 561797,
            "name": "Cooper Hospital 1",
            "address": "Bhakti Vedanta Swami Marg Andheri West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K West Corporation - MH",
            "pincode": 400058,
            "lat": 19,
            "long": 72,
            "from": "11:00:00",
            "to": "16:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "0f67146b-33aa-46e0-aba9-b17001dfc891",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-02:00PM",
                        "02:00PM-04:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 704347,
            "name": "St Francis Hall",
            "address": "Hall Near St Francis SchoolShani MandirLaxman Nagar Malad East -400097",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward P North Corporation - MH",
            "pincode": 400097,
            "lat": 19,
            "long": 72,
            "from": "12:00:00",
            "to": "17:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "47d6f4d4-4187-4875-8494-17b80f07a7e3",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "12:00PM-01:00PM",
                        "01:00PM-02:00PM",
                        "02:00PM-03:00PM",
                        "03:00PM-05:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 595085,
            "name": "SAIFEE HOSPITAL",
            "address": "15-17 Maharshi Karve Road",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward D Corporation - MH",
            "pincode": 400004,
            "lat": 18,
            "long": 72,
            "from": "09:30:00",
            "to": "11:30:00",
            "fee_type": "Paid",
            "sessions": [
                {
                    "session_id": "9a1722ec-3fac-44f0-9e98-9a0fe148f688",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVAXIN",
                    "slots": [
                        "09:30AM-11:30AM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ],
            "vaccine_fees": [
                {
                    "vaccine": "COVAXIN",
                    "fee": "1250"
                }
            ]
        },
        {
            "center_id": 703631,
            "name": "Siddhivinayak Pinacle",
            "address": "Siddhivinayak Pinacle SRA  Link Road Kandivali West 400067",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward R South Corporation - MH",
            "pincode": 400067,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "6835f7b1-fb7e-4a18-83dc-92b38834904b",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 630244,
            "name": "Cooper Hospital West Zone",
            "address": "Bhakti Vedanta Swami Marg Andheri West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K West Corporation - MH",
            "pincode": 400058,
            "lat": 19,
            "long": 72,
            "from": "11:00:00",
            "to": "16:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "31c18ca8-e160-4321-aa1a-82f16e7fa325",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVAXIN",
                    "slots": [
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-02:00PM",
                        "02:00PM-04:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 27436,
            "name": "Panjarpol HP SAIFEE Ambulence",
            "address": "Panjarpol HP Saifee Ambulance G-38 AI- Saadah Tower Off Ibrahim Rehmatullah Rd Opp Zainabia Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward C Corporation - MH",
            "pincode": 400003,
            "lat": 18,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "cc5037de-100f-4cc6-936f-975eac6f6786",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 696045,
            "name": "GT HOSPITAL",
            "address": "GT Hospital Near Police Commissioners Office Lokmanya Tilak Marg Fort G. P. O Mumbai Maharashtra",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward A Corporation - MH",
            "pincode": 400001,
            "lat": 0,
            "long": 0,
            "from": "10:00:00",
            "to": "17:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "ca6c41ca-fca2-42c3-b950-d7a64dd255fe",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-12:00PM",
                        "12:00PM-02:00PM",
                        "02:00PM-04:00PM",
                        "04:00PM-05:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                },
                {
                    "session_id": "d10b2b2f-8779-4a5b-830e-e1c630a2ea1e",
                    "date": "20-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 700894,
            "name": "Pahadi School",
            "address": "Pahadi Schoolpahadiroad No 1opp Jayas Society off Aarey RoadGoregaon East",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward P South Corporation - MH",
            "pincode": 400063,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "bcd64833-3740-49fa-b74a-a16c40c5b47f",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 562094,
            "name": "V N Desai Hospital 1",
            "address": "V.N. DESAI GENERAL MUNICIPAL HOSPITAL  SANTACRUZ EAST",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward H East Corporation - MH",
            "pincode": 400055,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "02f4c4cc-e3b1-4e4c-b252-1ed23b0d65ce",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 698729,
            "name": "BANANA LEAF DISPENSARY",
            "address": "FIRST FLOOR SHUBHAM CHS JUHU VERSOVA LINK RD OPP BHARAT NAGAR ANDHERI (W)",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K West Corporation - MH",
            "pincode": 400053,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "cdc2f691-b908-40a6-947f-70d0349226e2",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 700892,
            "name": "Aarey Check Naka Gymkhana",
            "address": "Aarey Check Naka Gymkhana Near Western Express Highwaynear Arrey Check Naka goregaon East",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward P South Corporation - MH",
            "pincode": 400065,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "5c45335f-e4fe-401b-88cd-a71c76915bd5",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 691626,
            "name": "Parivar MCGM OFFICE KANJURMARG",
            "address": "BMC BUILDING KANJURMARG",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward S Corporation - MH",
            "pincode": 400042,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "6d488455-654e-463a-9044-621e3d88d1af",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 700174,
            "name": "Sadguru Rahivasi Hitvardhak",
            "address": "Sadguru Rahivasi Hitvardhak Chawl Samiti Jai Hind Nagar Service Rd Khar East",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward H East Corporation - MH",
            "pincode": 400051,
            "lat": 19,
            "long": 72,
            "from": "11:00:00",
            "to": "16:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "50871e06-e97e-427b-945b-42d9b6b272dd",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-02:00PM",
                        "02:00PM-04:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 695695,
            "name": "The World Tower MCGM Parkg",
            "address": "The World Tower MCGM Parking Hanuman Galli Lower Parel",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward G South Corporation - MH",
            "pincode": 400013,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "8c8264f7-1373-4ddf-a348-fc84db559077",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 667305,
            "name": "Mumbai Port Trust",
            "address": "LM Nadkarni Marg Nadkarni Park Wadala East BPT Colony Wadala Mumbai Maharashtra 400037",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward F North Corporation - MH",
            "pincode": 400037,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "3618319e-d5e9-4bba-bcda-a8764d704daf",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 610288,
            "name": "KRANTIJYOTI SAVITRIBAI PHULE 1",
            "address": "Kasturba Cross Road No.02 Borivali East",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward R Central Corporation - MH",
            "pincode": 400066,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "dae6ddb4-bb38-4534-849c-05787428dddf",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 702057,
            "name": "Abhyasika And Toy Library P179",
            "address": "BMC Abhyasika And Toy Library Nadkarni Park Antophill Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward F North Corporation - MH",
            "pincode": 400037,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "6d491118-aba1-4f1d-ac2e-8bd214f877d3",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 701816,
            "name": "Shivaji Colony Hall P-96",
            "address": "Shivaji Nagar BMC Colony Kherwadi Road Bandra East Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward H East Corporation - MH",
            "pincode": 400051,
            "lat": 19,
            "long": 72,
            "from": "11:00:00",
            "to": "16:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "9f5f39cc-e446-4aaf-8091-d77d00c0e770",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-02:00PM",
                        "02:00PM-04:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 696509,
            "name": "K/W HBT URBAN HEALTH CENTER",
            "address": "NEAR MARKS AND SPENCER LOKHANDWALA COMPLEX OPP HIGH LAND PARK ANDHERI WEST MUMBAI",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K West Corporation - MH",
            "pincode": 400053,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "804c9d9b-facd-452d-a86e-97950a32eec7",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 698043,
            "name": "St Micheal Church CVC Mahim",
            "address": "Lady Jamshedji RdMahim West Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward G North Corporation - MH",
            "pincode": 400016,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "a98968fc-1f92-4fa1-aef9-255739000225",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 690032,
            "name": "Deonar Maternity Home",
            "address": "H-3 Block Deonar Municipal Colony DeonarGovandi East",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward M East Corporation - MH",
            "pincode": 400043,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "91f570c3-962e-4045-b0a6-c9472cec7b31",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 700316,
            "name": "Abhuyday Nagar School P 205",
            "address": "Abhuday Nagar Kalachowki Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward F South Corporation - MH",
            "pincode": 400033,
            "lat": 18,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "ec09a1da-71b3-4013-86d7-104257856e13",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 704105,
            "name": "ICCHAPURTI WELFARE 77",
            "address": "WELFARE CENTER ICCHAPURTI GANESH MANDIR JOGESHWARI EASTR",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K East Corporation - MH",
            "pincode": 400060,
            "lat": 19,
            "long": 72,
            "from": "12:30:00",
            "to": "15:30:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "80e43158-2c37-4de6-8b52-c21f3eced2e6",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "12:30PM-02:30PM",
                        "02:30PM-03:30PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 697151,
            "name": "NSCI DRIVE IN VACCINE CENTER",
            "address": "DR ANNIE BESANT ROAD RAJANI PATEL CHOWK HALI ALI",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward G South Corporation - MH",
            "pincode": 400018,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "75bac747-6b20-418e-a3bc-fdcf2a3d663c",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 700884,
            "name": "Sunder Nagar Dispensary",
            "address": "Near Bmc Arogya Kendra Opp Lenest Maternity HomeMalad West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward P South Corporation - MH",
            "pincode": 400064,
            "lat": 19,
            "long": 72,
            "from": "14:00:00",
            "to": "18:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "3bbd88e6-d270-4128-b40f-9a3a9e405c92",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "02:00PM-03:00PM",
                        "03:00PM-04:00PM",
                        "04:00PM-05:00PM",
                        "05:00PM-06:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 574931,
            "name": "SEVEN HIILS 1",
            "address": "Marol Maroshi Road Andheri East Mumbai Maharashtra.",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K East Corporation - MH",
            "pincode": 400059,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "2ce85af4-be88-49c8-a429-a972783eec89",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 698992,
            "name": "Community Hall Library 97",
            "address": "Besant Roadnear Mangal Nursing Homeopposite Sorrento Buildingsantacruz West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward H West Corporation - MH",
            "pincode": 400054,
            "lat": 19,
            "long": 72,
            "from": "10:30:00",
            "to": "15:30:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "35145423-d89d-4953-a722-ab5e912eb9e1",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:30AM-11:30AM",
                        "11:30AM-12:30PM",
                        "12:30PM-01:30PM",
                        "01:30PM-03:30PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 30393,
            "name": "Moti Lal Nagar HP Goregoan W",
            "address": "Haware Bldg Motilal Nagar Trikoni Maidan",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward P South Corporation - MH",
            "pincode": 400097,
            "lat": 0,
            "long": 0,
            "from": "14:00:00",
            "to": "18:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "e5540139-b411-46cb-add4-92f9ad3dbe93",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "02:00PM-03:00PM",
                        "03:00PM-04:00PM",
                        "04:00PM-05:00PM",
                        "05:00PM-06:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 697954,
            "name": "RIDDHI GARDEN MUNICIPAL DISP",
            "address": "RIDDHI GARDENS MALAD EAST",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward P North Corporation - MH",
            "pincode": 400097,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "0712b443-bbb3-4c76-be69-836a4249e1cf",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 701802,
            "name": "Patuck College S.V. Nagar HP",
            "address": "Nehru Road Near Vakola Bridge Santacruz East",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward H East Corporation - MH",
            "pincode": 400055,
            "lat": 19,
            "long": 72,
            "from": "11:00:00",
            "to": "16:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "b970abf4-fccb-4712-8235-f4978910c485",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-02:00PM",
                        "02:00PM-04:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 699535,
            "name": "LEHER LIBRARY HALL",
            "address": "NEAR LEHER BUILDING  MARVE  MALAD WEST",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward P North Corporation - MH",
            "pincode": 400064,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "3b4cf90d-1e8b-490b-8575-fb327ed6bb1d",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 698831,
            "name": "Punjabi Gali Diagnostic Centre",
            "address": "Punjabi Lane Off Lt Road Borivali West Beat No 15",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward R Central Corporation - MH",
            "pincode": 400092,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "1267d13c-866c-41fa-ba59-3cfbee908885",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 699551,
            "name": "MALVANI 2 UPHC",
            "address": "MALVANI 2 UPHC  GATE NO 6  MALVANI MALAD WEST 400095",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward P North Corporation - MH",
            "pincode": 400095,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "cb860d0a-0c12-48ab-bb7b-ce4e3fc08553",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 695248,
            "name": "Sambhaji Nagar HP Eco Heights",
            "address": "Nityanand Nagar Near Gokhale Bridge Opp Vihar Punjab Restaurant Andheri East",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K East Corporation - MH",
            "pincode": 400059,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "2da66006-3ab0-4a15-bf5a-e9449abcb1ed",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 697995,
            "name": "Rajasthan Seva Samiti CVC",
            "address": "Evershine Nagar MALAD WEST",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward P North Corporation - MH",
            "pincode": 400064,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "94586ade-60cf-49a1-8cc5-cf755e2c9dac",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 27427,
            "name": "Chandanwadi Munci School Disp.",
            "address": "Chandanwadi Municipal School Building Ground Floor Chandanwadi Jss Road Mumbai 2",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward C Corporation - MH",
            "pincode": 400002,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "974fc80d-31a6-42d6-b942-e5018117f890",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 698783,
            "name": "R K Mission Khotwadi HP P 98",
            "address": "Twelth Road Khar West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward H West Corporation - MH",
            "pincode": 400052,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "7207f5b1-918c-409a-aaa4-c2a2d75fc01f",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 695849,
            "name": "BANDRA OLD H/WEST WARD OFFICE",
            "address": "ST MARKETING ROAD BANDRA WEST MUMBAI",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward H West Corporation - MH",
            "pincode": 400050,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "37a2540f-e732-40a4-b3c7-097b8e1e627d",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 700718,
            "name": "Harmony Hall Gurunank P 176",
            "address": "Guru Nanak Higher Secondary School G Dardi Marg Guru Teg Bahadur Nagar Sion Mumbai Maharashtra 400022",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward F North Corporation - MH",
            "pincode": 400022,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "d244ee3a-41e1-491f-80e4-b357a1d227d0",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 699430,
            "name": "Madhavbaug Temple P 220",
            "address": "Madhavbaug Temple Marine Line East Gulalwadi Bhuleshwar Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward C Corporation - MH",
            "pincode": 400004,
            "lat": 18,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "1b4748b5-e4f0-4ae0-aede-9d0018e6de57",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 700266,
            "name": "Jio World Garden Drive",
            "address": "Jio World Garden BKC Bandra East",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward H East Corporation - MH",
            "pincode": 400051,
            "lat": 19,
            "long": 72,
            "from": "11:00:00",
            "to": "16:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "3e1fa90e-8bbe-41d3-8795-24216b17d704",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-02:00PM",
                        "02:00PM-04:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 700664,
            "name": "K Star Mall P-153 Chembur",
            "address": "K Star Mall V N Purav MargDiamond Gardenchembur",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward M West Corporation - MH",
            "pincode": 400071,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "aad4fdae-0be9-4438-956c-1e62a4e76ed0",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 700712,
            "name": "Nabar Guruji Hall GNO.14 P177",
            "address": "I.E.S Nabar Guruji Hall Gate No.14 Sir Bhalchandra Road.Hindu Colony Dadar Mumbai 400014",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward F North Corporation - MH",
            "pincode": 400014,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "894fc518-4c61-4a5c-bec7-348330937d1d",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 582415,
            "name": "Shatabdi Hospital-1-Govandi",
            "address": "Vaman Tukram Patil Marg Govandi-E",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward M East Corporation - MH",
            "pincode": 400088,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "20d909ba-d176-419a-ba4d-bf11d3520a3e",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 639071,
            "name": "BDBA Hospital Kandivali",
            "address": "S V ROAD KANDIVALI WEST",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward R South Corporation - MH",
            "pincode": 400067,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "1ec36469-86a1-4a96-881f-260207545953",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVAXIN",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 696510,
            "name": "K/W Andheri Sports Complex",
            "address": "Andheri Sports Complex JP Road Near Azad Nagar Metro Station Andheri West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K West Corporation - MH",
            "pincode": 400069,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "3dde6e64-9a66-4d76-90dd-3eda6f9fb653",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 614382,
            "name": "Jagjivan Ram Hospital",
            "address": "M M Marg RBI Staff Colony Mumbai Central Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward E Corporation - MH",
            "pincode": 400008,
            "lat": 18,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "2058db1a-aeab-4381-8dd5-e25f61ff43ab",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 691628,
            "name": "TEMBIPADA BMC SCHOOL BHANDUP",
            "address": "TEMBIPADA BMC SCHOOL KANJURMARG",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward S Corporation - MH",
            "pincode": 400078,
            "lat": 0,
            "long": 0,
            "from": "09:00:00",
            "to": "18:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "9fe153f7-1ac2-4457-9fd1-440c0a27b592",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "09:00AM-11:00AM",
                        "11:00AM-01:00PM",
                        "01:00PM-03:00PM",
                        "03:00PM-06:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 704537,
            "name": "Wadala Truck Terminals",
            "address": "Shop No. 91011 B-7 Building Shahyadri Wadala Truck Terminal.",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward F North Corporation - MH",
            "pincode": 400037,
            "lat": 19,
            "long": 72,
            "from": "12:00:00",
            "to": "17:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "5162d571-e34d-4035-b390-eefb2dba00df",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "12:00PM-01:00PM",
                        "01:00PM-02:00PM",
                        "02:00PM-03:00PM",
                        "03:00PM-05:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 698800,
            "name": "Swaminarayan Temple P 214",
            "address": "Bhulabai Desai Road Mahalaxmi Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward D Corporation - MH",
            "pincode": 400026,
            "lat": 18,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "b46855a4-b7a7-440b-866a-57edd2fb1840",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 628062,
            "name": "SEVEN HIILS WESTERN ZONE",
            "address": "Marol Maroshi Road Andheri East Mumbai Maharashtra.",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K East Corporation - MH",
            "pincode": 400059,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "9a03147c-344f-4d9b-9cd3-74b7201555d7",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVAXIN",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 698802,
            "name": "Samaj Kalyan Hall Ward No. 2",
            "address": "Samaj Kalyan Hall Near DSF Ground C. S. Main Road Dahisar East Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward R North Corporation - MH",
            "pincode": 400068,
            "lat": 19,
            "long": 19,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "2a720409-49f3-4978-8dcb-3813ecda92ea",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 680082,
            "name": "MT Agarwal Hospital Mulund (W)",
            "address": "Megh Malhar Society Chandraprabha Chs Mulund Mulund West Mumbai Maharashtra 400080",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward T Corporation - MH",
            "pincode": 400080,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "af1738f9-c15c-45ac-ba66-4d2efc96702b",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 696096,
            "name": "Paspoli Municipality SH Powai",
            "address": "Dr Babasaheb Ambedkar Udyan Opp L And T Powai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward S Corporation - MH",
            "pincode": 400087,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "cfddfa08-9a82-4cf0-bdd3-e818e0efe1e0",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 699571,
            "name": "Meenatai Thakre Mkt Ward No. 4",
            "address": "Meenatai Thakre Market Sant Ghadge Maharaj Marg Rawalpada Dahisar East Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward R North Corporation - MH",
            "pincode": 400068,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "54fb15a1-566f-4ea3-87d9-6779f57daf65",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 615806,
            "name": "Dr. Babasaheb Memorial GH",
            "address": "Dr Baba Saheb Ambedkar Road Byculla East Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward E Corporation - MH",
            "pincode": 400027,
            "lat": 18,
            "long": 72,
            "from": "10:00:00",
            "to": "10:30:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "70b00ffd-3d3e-47be-a8b1-fbef7072d7ca",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-10:30AM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 695383,
            "name": "ShastriNagar2 Transit C School",
            "address": "Transit Camp Schoolnearby Dharavi Police Station90 Feet Road Dharavi SionMumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward G North Corporation - MH",
            "pincode": 400017,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "be292f00-4c95-46db-9ad6-eeff2eb82d4d",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 699422,
            "name": "Alica Hall",
            "address": "Lokhandwala Township Kandivali East",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward R South Corporation - MH",
            "pincode": 400101,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "bda2c57a-c505-4aca-8d90-a89f218a5dc7",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 698056,
            "name": "Shahid Bhagat Sing Road Disp",
            "address": "Choksey Mension 1st Floor Sbs Road Fort Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward A Corporation - MH",
            "pincode": 400005,
            "lat": 18,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "c3e14743-23fb-4c91-8b65-5e45e2786b1b",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 704728,
            "name": "Dosti Acres Muncipal Schl 180",
            "address": "Dosti Acres Mahanagarpalika Municipal School Dosti Acres Complex Opp. Ambrosia Building Antophill Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward F North Corporation - MH",
            "pincode": 400037,
            "lat": 19,
            "long": 72,
            "from": "12:00:00",
            "to": "17:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "6f3aa4e2-3ffb-4406-83ad-2db125d55d0e",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "12:00PM-01:00PM",
                        "01:00PM-02:00PM",
                        "02:00PM-03:00PM",
                        "03:00PM-05:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 649050,
            "name": "N Ward Ganesh Nagar HP",
            "address": "Rajaram Bane Marg Opposite Mauli Building Laxmi Nagar Ghatkopar East",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward N Corporation - MH",
            "pincode": 400075,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "16ce44d4-b5d8-4f40-8840-6815ee00cc41",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 699606,
            "name": "Jankibai Hall",
            "address": "Dadabhai Naoraji Road Opp Andheri Recreation Club Mumbai-58",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K West Corporation - MH",
            "pincode": 400058,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "14404cf7-37f0-4869-a050-6a39daffd2b1",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 700887,
            "name": "Maharashtra Hall",
            "address": "Near Rationing Officeunnat Ngr Road No 1goregaon West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward P South Corporation - MH",
            "pincode": 400064,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "b5337eef-8218-475f-a4ac-7a108506341f",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 612041,
            "name": "HBT TRAUMA HOSPITAL",
            "address": "Hrudya Samrat Balasaheb Thakare Trauma Care BMC Hospital Jai Coach Bandekar WadiJogeshwari East",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K East Corporation - MH",
            "pincode": 400102,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "644243be-8d56-4489-9d17-68d79a930e3c",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 694638,
            "name": "APHO MCGM CENTRE",
            "address": "C S I Airport Next To Ambassador Sky Chef Andheri - Kurla Road Sahar Road Sahar Mumbai Maharashtra 400099",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K East Corporation - MH",
            "pincode": 400099,
            "lat": 0,
            "long": 0,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "9ade29ea-5ac8-4772-94c8-bd65e66f2400",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 700684,
            "name": "ParseeGymkhana Dadar E P178",
            "address": "No 606Dr Babasaheb Ambedkar Road Central Railway Colony Dadar East.",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward F North Corporation - MH",
            "pincode": 400014,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "0625a7e1-0078-444d-bef8-b459db0fdcc6",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 702087,
            "name": "Gurjar Bhawan P -152 Chembur",
            "address": "Sumati Gurjar Bhavan12 13 Swastik Parkopposite Shushrut Hospitalnear Swastik Chamberschemburmumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward M West Corporation - MH",
            "pincode": 400071,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "3758fae4-d1ff-46b8-be83-b09e8b98d030",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 699501,
            "name": "MADH DISPENSARY",
            "address": "MADH CHURCH  NEAR ST BONAVENTURE SCHOOL  MADH  MALAD WEST  400061",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward P North Corporation - MH",
            "pincode": 400064,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "4d3052b1-0fb6-4d8b-acdf-148364ce780e",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 589129,
            "name": "Kurla Bhabha Hospital-1",
            "address": "Kurla Babha Munciple Gen .Hos. Belgrami Road Kurla (W)",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward L Corporation - MH",
            "pincode": 400070,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "6d010d40-648b-424d-bac2-c96103ef410f",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 698672,
            "name": "GGS Municipal School Mulund",
            "address": "GGS Municipal School Mulund Colony Mulund",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward T Corporation - MH",
            "pincode": 400082,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "11d8ba6d-74f7-4aa6-bfd4-7ef8382d3070",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 636886,
            "name": "H N Reliance Hosp MUMBAI 1",
            "address": "Raja Rammohan Roy Road Prarthana Samaj Girgaon",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward C Corporation - MH",
            "pincode": 400004,
            "lat": 18,
            "long": 72,
            "from": "09:00:00",
            "to": "13:00:00",
            "fee_type": "Paid",
            "sessions": [
                {
                    "session_id": "9ad09483-59ce-4ebc-8bca-a58875b57ee5",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVAXIN",
                    "slots": [
                        "09:00AM-10:00AM",
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ],
            "vaccine_fees": [
                {
                    "vaccine": "COVAXIN",
                    "fee": "1250"
                }
            ]
        },
        {
            "center_id": 695328,
            "name": "Gadkari Hp Videocon Atithi",
            "address": "Bldg No.2 L. U Gadkari Marg Chemubur",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward M East Corporation - MH",
            "pincode": 400074,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "e8fda5ca-e02f-4d34-ac24-f727c0f3d359",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 701884,
            "name": "Apollo Mill Parking MHSC HP",
            "address": "NM Joshi Marg Lower Parel Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward G South Corporation - MH",
            "pincode": 400013,
            "lat": 19,
            "long": 72,
            "from": "12:00:00",
            "to": "17:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "bdeb208e-0706-4e21-8dfd-0ab453b281be",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "12:00PM-01:00PM",
                        "01:00PM-02:00PM",
                        "02:00PM-03:00PM",
                        "03:00PM-05:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 582993,
            "name": "M W DESAI HOSPITAL 1",
            "address": "Hazi Bapu Road Govind Nagar Malad East",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward P North Corporation - MH",
            "pincode": 400097,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "d3d3d3a3-c524-40e8-90dc-bc8e9cf81700",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 699507,
            "name": "Peru Compound School P 203",
            "address": "Peru Compound School P 203 Dr. B A Road Lalbaug Parel Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward F South Corporation - MH",
            "pincode": 400012,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "0e8a84c7-a324-4926-bb9c-fc882ad2d13e",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 698027,
            "name": "SHARDABEN PATEL GROUND HALL",
            "address": "ADARSH DUGDHALAY LANE MALAD WEST",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward P North Corporation - MH",
            "pincode": 400064,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "3b3906df-aefc-4267-a2a8-3a15157b2182",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 704030,
            "name": "Rotary Club Of Bombay 71",
            "address": "Juhu Tara Road Santacruz West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K West Corporation - MH",
            "pincode": 400054,
            "lat": 19,
            "long": 72,
            "from": "12:00:00",
            "to": "17:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "d0356503-cd76-4b6f-be06-028fcaf2a6fc",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "12:00PM-01:00PM",
                        "01:00PM-02:00PM",
                        "02:00PM-03:00PM",
                        "03:00PM-05:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 609698,
            "name": "BOMBAY HOSPITAL (RV)",
            "address": "12 Vitthaldas Thackersey Marg New Marine Lines Marine Lines Mumbai Maharashtra",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward A Corporation - MH",
            "pincode": 400020,
            "lat": 19,
            "long": 72,
            "from": "09:00:00",
            "to": "18:00:00",
            "fee_type": "Paid",
            "sessions": [
                {
                    "session_id": "6e813e2a-3b0c-4cee-90dd-5fe98ad20221",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVAXIN",
                    "slots": [
                        "09:00AM-11:00AM",
                        "11:00AM-01:00PM",
                        "01:00PM-03:00PM",
                        "03:00PM-06:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ],
            "vaccine_fees": [
                {
                    "vaccine": "COVAXIN",
                    "fee": "250"
                }
            ]
        },
        {
            "center_id": 695994,
            "name": "Bhandup Village BMC School",
            "address": "Near Bhandup Phatak Veer Savarkar Marg Bhandup East",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward S Corporation - MH",
            "pincode": 400042,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "09836e92-6500-4055-b5ca-ed8ffe18397a",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 700367,
            "name": "Adharika Bhawan Gorai",
            "address": "Rsc 28 Gorai 2 Boriwali West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward R Central Corporation - MH",
            "pincode": 400092,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "85d1e0e1-8536-4f3e-8334-a975ca8f9dd1",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 585385,
            "name": "V. D. Savarkar Hospital-1",
            "address": "Mahatma Phule Road Hanuman Chowk Mulund (E)",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward T Corporation - MH",
            "pincode": 400081,
            "lat": 19,
            "long": 72,
            "from": "09:00:00",
            "to": "18:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "af436cf9-dcc8-4100-b06a-b6d35980d0fd",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "09:00AM-11:00AM",
                        "11:00AM-01:00PM",
                        "01:00PM-03:00PM",
                        "03:00PM-06:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 672148,
            "name": "IIT BOMBAY POWAI",
            "address": "Main Gate Rd IIT Area Powai Mumbai Maharashtra 400076",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward S Corporation - MH",
            "pincode": 400076,
            "lat": 19,
            "long": 72,
            "from": "09:00:00",
            "to": "14:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "d6714abc-1e2a-4994-94a7-98ad2df1422d",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "09:00AM-10:00AM",
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-02:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 648946,
            "name": "LBS HOSPITAL MUMBAI",
            "address": "LBS Mat. Home Kukreja Complex Road Bhandup (W)",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward S Corporation - MH",
            "pincode": 400078,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "b18b1319-0a64-473e-b7be-e05aadd2c949",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 598571,
            "name": "Kohinoor Hospital -1",
            "address": "Kohinoor Hospital Kohinoor City Kirol Road Off LBS Marg Kurla (West) Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward L Corporation - MH",
            "pincode": 400070,
            "lat": 19,
            "long": 72,
            "from": "09:00:00",
            "to": "18:00:00",
            "fee_type": "Paid",
            "sessions": [
                {
                    "session_id": "5b965747-c663-44f9-86a3-df5bd8862a13",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "09:00AM-11:00AM",
                        "11:00AM-01:00PM",
                        "01:00PM-03:00PM",
                        "03:00PM-06:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ],
            "vaccine_fees": [
                {
                    "vaccine": "COVISHIELD",
                    "fee": "250"
                }
            ]
        },
        {
            "center_id": 649864,
            "name": "MGM Hospital Parel",
            "address": "Mahatma Gandhi Memorial Hospial Dr. S. S. Rao Road Parel Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward F South Corporation - MH",
            "pincode": 400012,
            "lat": 18,
            "long": 72,
            "from": "09:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "d56adb27-af9c-48ee-88a6-67405f74149f",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "09:00AM-10:00AM",
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 698638,
            "name": "Samaj Kalyan Parshiwadi P 129",
            "address": "Parshiwadi Ghatkopar West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward N Corporation - MH",
            "pincode": 400086,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "604dccda-8935-472f-ae2f-55cd1084199c",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 701212,
            "name": "Tulip Health Post P-158",
            "address": "Tulip Heath Centre And BMC Dispensary Near Sak Vihar Complex  Sakivihar Road  Sakinaka",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward L Corporation - MH",
            "pincode": 400072,
            "lat": 19,
            "long": 72,
            "from": "11:00:00",
            "to": "16:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "71c45f5b-3007-480d-b5d0-cf73803f71a4",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-02:00PM",
                        "02:00PM-04:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 695341,
            "name": "Ayodhyanagar Hp Yoga Kendra",
            "address": "Yoga Kendranear Ayodhyanagar Hp Near Fish Market Vashi Naka Chembure",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward M East Corporation - MH",
            "pincode": 400074,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "d6c968a3-4df9-4711-8f9c-8b541956e807",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 696029,
            "name": "Tarun Bharat HP Welfare Center",
            "address": "Welfare Center CTS Chakala C G Road Beside P G Building",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K East Corporation - MH",
            "pincode": 400099,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "68016c47-29f8-4999-bf38-1a9b91d31f4f",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 699514,
            "name": "HakimAjmalkhan Dawakhana P211",
            "address": "Meghraj Sethi Marg Opposite Zhulamaidan Agripada Byculla West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward E Corporation - MH",
            "pincode": 400011,
            "lat": 18,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "9c1f30f9-dcbc-4df2-9c15-0489f8e4701f",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 688205,
            "name": "MEENATAI THACKREY GOREGOAN",
            "address": "GOREGOAN WEST",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward P South Corporation - MH",
            "pincode": 400104,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "9ceb2af5-d348-44ac-adcf-b3ee31925752",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 700886,
            "name": "Laxmi Nagar Dispensary",
            "address": "Garden Estatelaxmi Nagargoregaon West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward P South Corporation - MH",
            "pincode": 400104,
            "lat": 19,
            "long": 72,
            "from": "14:00:00",
            "to": "18:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "35b5a92a-3f51-470b-92a8-2cc96a823d50",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "02:00PM-03:00PM",
                        "03:00PM-04:00PM",
                        "04:00PM-05:00PM",
                        "05:00PM-06:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 700657,
            "name": "Sant Nirankari Bhavan P-154",
            "address": "Sant Nirankari Bhavanmahul Road chembur Colonymumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward M West Corporation - MH",
            "pincode": 400074,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "3ea5a874-63a6-4b2f-80a4-220b0ecf99bd",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 699765,
            "name": "Mahanagarpalika Mudranalay 207",
            "address": "N.M.Joshi Marg Bakri Adda Byculla West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward E Corporation - MH",
            "pincode": 400011,
            "lat": 18,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "f3595691-ebfc-43fc-b998-353544def01a",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 700151,
            "name": "Jolly Gymkhana VidyaVihar P130",
            "address": "Jolly Gymkhana Kirol Street Jugaldas Mody Marg Ghatkopar W",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward N Corporation - MH",
            "pincode": 400086,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "01003dea-d6f1-4146-928e-c82d45e3cdd0",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 629367,
            "name": "Kohinoor Hospital Kurla Mumbai",
            "address": "Kohinoor Hospital Kohinoor City Kirol Road Off LBS Marg Kurla (West) Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward L Corporation - MH",
            "pincode": 400070,
            "lat": 19,
            "long": 72,
            "from": "09:00:00",
            "to": "18:00:00",
            "fee_type": "Paid",
            "sessions": [
                {
                    "session_id": "ba78635c-f2e4-4168-82ef-b66dfc8d7dfd",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVAXIN",
                    "slots": [
                        "09:00AM-11:00AM",
                        "11:00AM-01:00PM",
                        "01:00PM-03:00PM",
                        "03:00PM-06:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ],
            "vaccine_fees": [
                {
                    "vaccine": "COVAXIN",
                    "fee": "250"
                }
            ]
        },
        {
            "center_id": 617404,
            "name": "R. A. Podar Medical College",
            "address": "Dr Annie Besant Rd B Wing BDD Chawls Worli Worli Mumbai Maharashtra 400018",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward G South Corporation - MH",
            "pincode": 400018,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "997128bd-7ba5-4e29-b768-737071a878d4",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 699522,
            "name": "KHUSHBOO HALL",
            "address": "MHADA MALVANI MALAD WEST",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward P North Corporation - MH",
            "pincode": 400095,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "d8575406-83a3-489c-b71f-347ff4c0f85b",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 700777,
            "name": "Khilafat House P 210",
            "address": "173-175 Motisha Lane Lovelane Mazgaon Byculla",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward E Corporation - MH",
            "pincode": 400027,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "4b127e67-feab-4422-aae2-dd1e0ce9bb0d",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 703434,
            "name": "Trikoni Maidan Natvar Nagar HP",
            "address": "Trikoni Maidan Hindu Freinds Society Road Next Amboli Phatak Ward 72 Jogeshwari (e)",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K East Corporation - MH",
            "pincode": 400060,
            "lat": 19,
            "long": 72,
            "from": "12:00:00",
            "to": "15:30:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "e5e72d99-c8b0-4e45-a914-9b917bbad89d",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "12:00PM-02:00PM",
                        "02:00PM-03:30PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 695865,
            "name": "G A Kulkarni School 17th Road",
            "address": "17th Road Khar West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward H West Corporation - MH",
            "pincode": 400052,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "23a2be13-ac3d-45c4-88ae-57e6a5998e26",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 639018,
            "name": "LBS HOSPITAL BHANDUP",
            "address": "LBS Mat. Home Kukreja Complex Road Bhandup (W)",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward S Corporation - MH",
            "pincode": 400078,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "979f78e3-6d0c-48eb-9a9c-517b7e98e7d2",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVAXIN",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 698007,
            "name": "ST. ISABEL SCHOOL HALL",
            "address": "ANJEERWADI DR. MASCARENHAS RD. MAZGAON MUMBAI",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward E Corporation - MH",
            "pincode": 400010,
            "lat": 18,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "fbe00b95-824d-48ea-b4c1-cd1a461c57eb",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 635958,
            "name": "Matoshri Ramabai Thakare",
            "address": "N Ward Matoshri Ramabai Thakare Maternity Home",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward N Corporation - MH",
            "pincode": 400086,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "3bd1ce0e-d04f-4f92-a3ef-9b3e1d2d951e",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 700366,
            "name": "S K C Parikh Gen Hosp.(JUHU)",
            "address": "Vitthal Nagar NS Road No 11 Vile Parle West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K West Corporation - MH",
            "pincode": 400049,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "f587dc02-0a38-46aa-b8a3-c75926feaf80",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 704759,
            "name": "Children Welfare Center",
            "address": "Dhangarwadi Behind Gillbert Hill Police Chowki Gillbert Hill Andheri",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K West Corporation - MH",
            "pincode": 400058,
            "lat": 19,
            "long": 72,
            "from": "12:00:00",
            "to": "17:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "09f8ae30-d883-47a5-9852-b8d594067d49",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "12:00PM-01:00PM",
                        "01:00PM-02:00PM",
                        "02:00PM-03:00PM",
                        "03:00PM-05:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 641151,
            "name": "V N Desai Hospital Mumbai",
            "address": "V.N. DESAI GENERAL MUNICIPAL HOSPITAL  SANTACRUZ EAST",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward H East Corporation - MH",
            "pincode": 400055,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "78bb6548-c402-46d4-b87b-7cd79f1a4e5b",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVAXIN",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 698779,
            "name": "WOMEN GRADUATES UNION HALL",
            "address": "MCGM WOMEN GRADUATES UNION HALL 1ST FLOOR W. G. UNION ROAD AZAD NAGAR COLABA",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward A Corporation - MH",
            "pincode": 400005,
            "lat": 18,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "8c726c9d-d24c-4186-9786-c1d7286a38eb",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 687268,
            "name": "Acworth Municipal Hosp Wadala",
            "address": "Major R Parameswaran Road Wadala Mumbai Maharashtra",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward F North Corporation - MH",
            "pincode": 400031,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "c48d3dec-9225-4183-8dbe-1f14c3690bfc",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 699558,
            "name": "MIDC Arogya Kendra",
            "address": "MIDC Arogya Kendra Covid -19 Vaccination Center Next To Jyothy Labs Near Apna Dhaba Kondivita MCGM Prabhag No.76 Andheri East Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K East Corporation - MH",
            "pincode": 400059,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "2469508c-dc1e-45cc-bd90-91575a31847b",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 696051,
            "name": "Jain Mandir Tarun Bharat",
            "address": "Jain Mandir At Bhagwan Mahavir Marg. J.B.Nagar Andheri (East)",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K East Corporation - MH",
            "pincode": 400099,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "f891e67c-92c2-49aa-9043-d6e8c87d6115",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 582977,
            "name": "SK PATIL HOSPITAL 1",
            "address": "Daftari Road Near Pushpa Park Malad East",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward P North Corporation - MH",
            "pincode": 400097,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "edac9986-b330-49c8-98b0-fd3c1722644c",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 115907,
            "name": "MAA SAHEB MEENATAI MAT HOME",
            "address": "Chunabhatti Mat Home Tata Nagar Chunabhatti VNPurav Marg Mumbai- 22",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward L Corporation - MH",
            "pincode": 400022,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "8f51272a-a624-49b4-98e3-09f82c03d27f",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 700110,
            "name": "Raje Sambhaji Vidyalay",
            "address": "Patel Nagar Maratha Colony Golibar  Santacruz East",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward H East Corporation - MH",
            "pincode": 400055,
            "lat": 19,
            "long": 72,
            "from": "11:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "7e45d662-997e-4559-8669-5a23666a717e",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-02:00PM",
                        "02:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 698794,
            "name": "Panchayat Hall Ward No.8",
            "address": "Panchayat Hall Ward No. 8 LIC Colony Near Shankar Mandir Vallabh Nagar Dr. Shrungi Marg Dahisar West Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward R North Corporation - MH",
            "pincode": 400103,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "1ff6582d-475d-4ce5-8851-42e950510f1d",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 699597,
            "name": "MCGM WELFARE CENTRE",
            "address": "RAHEJA ESTATE KULUPWADI BORIVALI EAST.400066",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward R Central Corporation - MH",
            "pincode": 400066,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "d97ed554-2e26-416d-8db5-3234916feeb3",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 696386,
            "name": "Manoranjan Hall Ghatkopar West",
            "address": "CSD Vasahat Golibar Road Ghatkopar West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward N Corporation - MH",
            "pincode": 400086,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "cf060fa0-fadd-4fc5-a46d-d22b787c45d2",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 695250,
            "name": "SUNDAR NAGARHP MATOSHRI SPORTS",
            "address": "Meenatai Thackeray Playground Suprimo Activity Center Matoshri Jogeshwari - Vikhroli Link Rd Near Bharat Petrol Pump Andheri East Mumbai Maharashtra 400093",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward K East Corporation - MH",
            "pincode": 400093,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "a0383303-bdc1-4305-8b3f-1b46f252a483",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 701877,
            "name": "Balasaheb Thakare IAS P-194",
            "address": "Beside Samna Press Prabhadevi Mumbai",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward G South Corporation - MH",
            "pincode": 400025,
            "lat": 19,
            "long": 72,
            "from": "12:00:00",
            "to": "17:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "7c59a340-cbae-4284-8785-dd93035128de",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "12:00PM-01:00PM",
                        "01:00PM-02:00PM",
                        "02:00PM-03:00PM",
                        "03:00PM-05:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 698805,
            "name": "Lunava Bhavan (E )P 208",
            "address": "Lunava BhavanDadoji Kondev Margnear Hanuman Mandir Byculla East Mumbai.",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward E Corporation - MH",
            "pincode": 400027,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "9240db6e-5d33-4b5c-81bf-b5d57b2a2e71",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 700373,
            "name": "Seth Ayurvedic Hospital",
            "address": "Ayurvedic Prasarak Mandal Road Sion Railway Colony Sion West",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward F North Corporation - MH",
            "pincode": 400022,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "517c90b5-a84e-44ba-84b4-07a1e263a80c",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        },
        {
            "center_id": 116179,
            "name": "N Ward Sant Mukta Bai Hospital",
            "address": "Sant Muktabai Hospial Barvenagar Ghatkopar W",
            "state_name": "Maharashtra",
            "district_name": "Mumbai",
            "block_name": "Ward N Corporation - MH",
            "pincode": 400086,
            "lat": 19,
            "long": 72,
            "from": "10:00:00",
            "to": "15:00:00",
            "fee_type": "Free",
            "sessions": [
                {
                    "session_id": "d4980371-cb7b-4768-b98e-8ece7cd86070",
                    "date": "19-05-2021",
                    "available_capacity": 0,
                    "min_age_limit": 45,
                    "vaccine": "COVISHIELD",
                    "slots": [
                        "10:00AM-11:00AM",
                        "11:00AM-12:00PM",
                        "12:00PM-01:00PM",
                        "01:00PM-03:00PM"
                    ],
                    "available_capacity_dose1": 0,
                    "available_capacity_dose2": 0
                }
            ]
        }
    ]
}


    def filter_age(centers):
        filtered_center = [];
        for center in centers:
            newSession = []
            flag = False;
            for session in center['sessions']:
                if session['min_age_limit'] == 18 and session['available_capacity'] > 0 :
                    newSession.append(session);
                    flag = True;

            if flag == True :
                center['sessions'] = newSession
                filtered_center.append(center)
               
                    
        return filtered_center;

    res = filter_age(response_text['centers'])
    if len(res):
        ifttt_webhook_url = 'https://maker.ifttt.com/trigger/vaccine/with/key/bMd5VRSXwc7EXXySzbSVR'
        requests.post(ifttt_webhook_url)

    return render_template('index.html', result = res)