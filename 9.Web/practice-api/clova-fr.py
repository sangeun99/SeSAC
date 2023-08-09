import os
import sys
import requests
import cv2
import numpy as np
import json

def cfr_face(filename):
    client_id = 'nI7wUOxDulcubRtSlpzR'
    client_secret = open('secret.txt', 'r').read()

    url = "https://openapi.naver.com/v1/vision/face" # 얼굴감지
    # url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 얼굴인식

    files = {'image': open(filename, 'rb')}
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }

    response = requests.post(url,  files=files, headers=headers)
    rescode = response.status_code
    if(rescode==200):
        print (response.text)
    else:
        print("Error Code:" + rescode)

    data = json.loads(response.text)
    return data

def cfr_celebrity(filename):
    client_id = 'nI7wUOxDulcubRtSlpzR'
    client_secret = open('secret.txt', 'r').read()

    # url = "https://openapi.naver.com/v1/vision/face" # 얼굴감지
    url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 얼굴인식

    files = {'image': open(filename, 'rb')}
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }

    response = requests.post(url,  files=files, headers=headers)
    rescode = response.status_code
    if(rescode==200):
        print (response.text)
    else:
        print("Error Code:" + rescode)

    data = json.loads(response.text)
    return data

def my_opencv(filename):
    face_info = cfr_face(filename)
    print(face_info)
    
    face_info_celeb = cfr_celebrity(filename)
    print(face_info_celeb)

    img_array = np.fromfile(filename, np.int8)
    image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    for i in range(len(face_info['faces'])) :
        face = face_info['faces'][i]
        face_celeb = face_info_celeb['faces'][i]

        celebrity = face_celeb['celebrity']['value']
        print(celebrity)

        roi = face['roi']
        emotion = face['emotion']['value']
        x, y, w, h = roi['x'], roi['y'], roi['width'], roi['height']
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 4)

        cv2.putText(image, emotion, (x,y), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), 1)
        cv2.putText(image, celebrity, (x,y+h), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), 1)

    cv2.imshow('kyooo', image)
    cv2.waitKey(0)
    
if __name__ == "__main__" :
    filename = 'images/kyo4.jpg'
    my_opencv(filename)