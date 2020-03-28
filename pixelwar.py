import numpy as np
import cv2
import random, hashlib, requests

img = cv2.imread('cec.jpg')

def setpixel(x,y,color, proof):
    params = {'x':str(x),
                'y':str(y),
                'color':color,
                'proof':proof}
    r = requests.get('http://137.74.47.86/setpixel', params=params)
    return r.text == 'OK'

for x in range(20):
    for y in range(20):
        color = '#%02x%02x%02x' % tuple(reversed(img[x,y]))
        # print(img[x,y])
        # proof = ''
        # hashFound = False
        # while not hashFound:
        #     proof = ''.join([random.choice('h25io') for _ in range(30)])
        #     if hashlib.sha256(('h25'+proof).encode()).hexdigest().startswith('00000'):
        #         hashFound = True
        # sent = False
        # while not sent:
        #     sent = setpixel(x+40,y+40,color[1:],proof)
        print('OK for pixel x ', x, ' and y ', y, ' with color ', color)

# exemple : setpixel(60,60,'ffffff')