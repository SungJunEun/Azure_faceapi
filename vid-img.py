import cv2
# set video file path of input video with name and extension
vid = cv2.VideoCapture('C:/Users/kkang/Documents/GitHub/faceapi/test.mp4')



#for frame identity
index = 0
while(True):
    # Extract images
    ret, frame = vid.read()
    # end of frames
    if not ret:
        break
    # Saves images
    name = 'C:/Users/kkang/Documents/GitHub/faceapi/images/' + str(index) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # next frame
    index += 100
    if index >5000:
        break
