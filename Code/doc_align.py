import cv2
import numpy as np


def align_document(path):

    img=cv2.imread(path)

    img=cv2.resize(
        img,
        (1200,1600)
    )

    return img



def register_images(reference,test):

    gray1=cv2.cvtColor(
        reference,
        cv2.COLOR_BGR2GRAY
    )

    gray2=cv2.cvtColor(
        test,
        cv2.COLOR_BGR2GRAY
    )


    orb=cv2.ORB_create(5000)

    kp1,des1=orb.detectAndCompute(
        gray1,None
    )

    kp2,des2=orb.detectAndCompute(
        gray2,None
    )


    matcher=cv2.BFMatcher(
        cv2.NORM_HAMMING,
        crossCheck=True
    )

    matches=matcher.match(
        des1,
        des2
    )

    matches=sorted(
       matches,
       key=lambda x:x.distance
    )[:500]


    pts1=np.float32(
       [kp1[m.queryIdx].pt for m in matches]
    ).reshape(-1,1,2)


    pts2=np.float32(
       [kp2[m.trainIdx].pt for m in matches]
    ).reshape(-1,1,2)


    H,_=cv2.findHomography(
       pts2,
       pts1,
       cv2.RANSAC
    )


    aligned=cv2.warpPerspective(
       test,
       H,
       (
        reference.shape[1],
        reference.shape[0]
       )
    )

    return aligned