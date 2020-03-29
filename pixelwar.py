import numpy as np
import cv2, random, hashlib, requests, string

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
    return r.text

def getPixelMap():
    img = cv2.imread('cec-small.jpg')
    [x,y,_] = img.shape
    pixels = []
    for i in range(x):
        for j in range(y):
            pixels.append([i,j,getHex(img[i,j])])
    return pixels

def getProof():
    proof = ''
    hashFound = False
    while not hashFound:
        proof = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
        if hashlib.sha256(('h25'+proof).encode()).hexdigest().startswith('00000'):
            hashFound = True
    return proof

pixels = getPixelMap()
while True:
    imgH25 = getH25img()
    print('Loaded image from H25')
    [x,y,color] = random.choice(pixels)
    while color == getHex(imgH25[x+20,y+60]):
        [x,y,color] = random.choice(pixels)
    print('Processing (',x,',',y,')')
    i = x+20
    j = y+60
    colorH25 = getHex(imgH25[i,j])

    if color != colorH25:
        print('Color is different ! Us ',color,'| Them ',colorH25)
        proof = getProof()
        reqResult = setpixel(j,i,color[1:],proof)
        print('Request result: ', reqResult)