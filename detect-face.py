
import requests
import json
import numpy as np
import os

# set to your own subscription key value
subscription_key = 'ad8433203b0a44aa803094e2eb780b21'
assert subscription_key

# replace <My Endpoint String> with the string from your endpoint URL
face_api_url = 'https://kpmgfaceapi.cognitiveservices.azure.com/face/v1.0/detect'

image_url = 'https://qfqewfegqe.blob.core.windows.net/abc/C:/Users/kkang/Documents/GitHub/faceapi/images/0.jpg'

headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}

response = requests.post(face_api_url, params=params,
                         headers=headers, json={"url": image_url})
print(json.dumps(response.json()))
