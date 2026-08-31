import cv2
import numpy as np


def normalize_document(img):

    img=cv2.resize(img,(1200,1600))

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    clahe=cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8,8)
    )

    gray=clahe.apply(gray)

    gray=cv2.GaussianBlur(gray,(3,3),0)

    kernel=np.array([
        [0,-1,0],
        [-1,5,-1],
        [0,-1,0]
    ])

    gray=cv2.filter2D(gray,-1,kernel)

    return gray