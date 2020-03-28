import cv2, requests, numpy as np

url = r'http://pixelwar.h25.io/image'
resp = requests.get(url, stream=True).raw
imgH25 = np.asarray(bytearray(resp.read()), dtype="uint8")
imgH25 = cv2.imdecode(imgH25, cv2.IMREAD_COLOR)

img = cv2.imread('cec-small.jpg')

def getHex(bgr):
    return '#%02x%02x%02x' % tuple(reversed(img[x,y]))
print(img.shape)
print(imgH25.shape)
for x in range(20):
    for y in range(30):
        print(img[abs(19-x), abs(29-y)])
        print(imgH25[x+35, y+40])
        # color = getHex(img[abs(19-x),abs(29-y)])
        # colorH25 = getHex(imgH25[x+35,y+40])
        # print('us ',color,' | them ',colorH25, ' | different ', color != colorH25)