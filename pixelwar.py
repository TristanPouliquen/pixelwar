import numpy as np
import cv2, random, hashlib, requests

img = cv2.imread('cec-small.jpg')

def getHex(bgr):
    return '#%02x%02x%02x' % tuple(reversed(bgr))

def getH25img():
    url = r'http://pixelwar.h25.io/image'
    resp = requests.get(url, stream=True).raw
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    return cv2.imdecode(image, cv2.IMREAD_COLOR)

def setpixel(x,y,color, proof):
    params = {'x':str(x),
                'y':str(y),
                'color':color,
                'proof':proof}
    r = requests.get('http://137.74.47.86/setpixel', params=params)
    return r.text == 'OK'

while True:
    imgH25 = getH25img()
    print('Loaded image from H25')
    for x in range(20):
        for y in range(30):
            print('Processing (',x,',',y,')')
            i = x+20
            j = y+60
            color = getHex(img[abs(19-x),abs(29-y)])
            colorH25 = getHex(imgH25[i,j])

            if color != colorH25:
                print('Color is different ! Us ',color,'| Them ',colorH25)
                proof = ''
                hashFound = False
                while not hashFound:
                    proof = ''.join([random.choice('h25io') for _ in range(30)])
                    if hashlib.sha256(('h25'+proof).encode()).hexdigest().startswith('00000'):
                        hashFound = True
                sent = False
                while not sent:
                    sent = setpixel(i,j,color[1:],proof)
                print('Corrected')