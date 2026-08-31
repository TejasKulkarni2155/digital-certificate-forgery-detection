import cv2
import os
import numpy as np

from doc_align import align_document,register_images


original=align_document(
"templates/original.png"
)


for file in os.listdir("test_images"):

    print("\nTesting:",file)

    test=align_document(
       f"test_images/{file}"
    )

    test=register_images(
       original,
       test
    )


    g1=cv2.cvtColor(
      original,
      cv2.COLOR_BGR2GRAY
    )

    g2=cv2.cvtColor(
      test,
      cv2.COLOR_BGR2GRAY
    )


    output=test.copy()

    g1[0:250,:]=255
    g2[0:250,:]=255


    _,b1=cv2.threshold(
       g1,180,255,
       cv2.THRESH_BINARY_INV
    )

    _,b2=cv2.threshold(
       g2,180,255,
       cv2.THRESH_BINARY_INV
    )


    diff=cv2.bitwise_xor(
       b1,b2
    )


    kernel=np.ones(
      (2,2),
      np.uint8
    )

    diff=cv2.morphologyEx(
       diff,
       cv2.MORPH_OPEN,
       kernel
    )

    diff=cv2.dilate(
       diff,
       kernel,
       iterations=1
    )


    changed=cv2.countNonZero(diff)

    total=diff.shape[0]*diff.shape[1]

    tamper=(changed/total)*100

    tamper*=6

    if tamper>100:
       tamper=100

    score=100-tamper


    if score>90:
       status="AUTHENTIC"

    elif score>70:
       status="MINOR TAMPERING"

    else:
       status="HIGH TAMPERING"


    print(
      f"Authenticity Score: {score:.2f}%"
    )

    print(
      "Status:",
      status
    )


    contours,_=cv2.findContours(
      diff,
      cv2.RETR_EXTERNAL,
      cv2.CHAIN_APPROX_SIMPLE
    )

    for c in contours:

        x,y,w,h=cv2.boundingRect(c)

        area=w*h

        if area<120:
           continue

        if area>2500:
           continue

        if w>4*h:
           continue

        cv2.rectangle(
           output,
           (x,y),
           (x+w,y+h),
           (0,0,255),
           2
        )


    cv2.putText(
      output,
      f"{score:.1f}%",
      (40,80),
      cv2.FONT_HERSHEY_SIMPLEX,
      1,
      (0,0,255),
      3
    )


    cv2.imshow(
      file,
      output
    )

    cv2.waitKey(0)

    cv2.destroyAllWindows()