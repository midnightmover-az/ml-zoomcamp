import requests

url = "http://localhost:9696/predict"
#client1 = {"job": "unknown", "duration": 270, "poutcome": "failure"}
#client2 = {"job": "retired", "duration": 445, "poutcome": "success"}
client_docker = {"job": "retired", "duration": 445, "poutcome": "success"}
client = client_docker

response = requests.post(url, json=client).json()

print( 'request=', client )
print( 'response=', response )
