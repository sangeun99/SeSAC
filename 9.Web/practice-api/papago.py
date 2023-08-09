import os
import sys
import json
import urllib.request

client_id = 'nI7wUOxDulcubRtSlpzR'
client_secret = open('secret.txt', 'r').read()

encText = urllib.parse.quote("반갑습니다")
data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
    data = json.loads(response_body)
    print(data)
    print(data['message']['result']['translatedText'])
else:
    print("Error Code:" + rescode)