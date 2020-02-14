
import requests
import json
import cv2
import numpy as np
import os
import urllib.parse as urlparse
import urllib





# set video file path of input video with name and extension
vid = cv2.VideoCapture('C:/Users/kkang/Documents/GitHub/faceapi/test.mp4')


if not os.path.exists('images'):
    os.makedirs('images')

#for frame identity
index = 0
while(True):
    # Extract images
    ret, frame = vid.read()
    # end of frames
    if not ret:
        break
    # Saves images
    name = './images/frame' + str(index) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # next frame
    index += 100
    if index >5000:
        break




# set to your own subscription key value
subscription_key = 'ad8433203b0a44aa803094e2eb780b21'
assert subscription_key

# replace <My Endpoint String> with the string from your endpoint URL
face_api_url = 'https://kpmgfaceapi.cognitiveservices.azure.com/face/v1.0/detect'

image_url = 'file:///C:/Users/kkang/Documents/GitHub/faceapi/images/frame0.jpg'

headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}

response = requests.post(face_api_url, params=params,
                         headers=headers, json={"url": image_url})
print(json.dumps(response.json()))
