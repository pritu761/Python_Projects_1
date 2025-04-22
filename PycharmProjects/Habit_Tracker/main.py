import requests
from datetime import datetime
username = "pritam761"
token = "thisissecret"
website="https://pixe.la/v1/users"
user_parameters={
    "token":token,
    "username":username,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

#response = requests.post(url=website,json=user_parameters)
#print(response.text)
graph_endpont = f"{website}/{username}/graphs"
graph_parameters={
    "id":"test-graph",
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"momiji"  
}
header={
    "X-USER-TOKEN":token
}
#response1 = requests.post(url=graph_endpont,json=graph_parameters,headers=header)
#print(response1.text)
today = datetime.now()

parameters_new={
    "date":today.strftime("%Y%m%d"),
    "quantity":"10.28"
}
url1=f"{graph_endpont}/test-graph"
response2= requests.post(url=url1,json=parameters_new,headers=header)
print(response2.text)
