import cv2
img=cv2.imread('solar-system.jpg')




cv2.putText(img,
            "Sun",
            (20,220),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5,
            color=(255,255,255))
cv2.putText(img,
            "Mercury",
            (80,220),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5,
            color=(255,255,255))
cv2.putText(img,
            "Venus",
            (180,220),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5,
            color=(255,255,255))
cv2.putText(img,
            "Earth",
            (200,220),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5,
            color=(255,255,255))
cv2.putText(img,
            "Mars",
            (260,220),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5,
            color=(255,255,255))
cv2.putText(img,
            "Jupiter",
            (320,220),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5,
            color=(255,255,255))
cv2.putText(img,
            "Saturn",
            (380,220),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(255,255,255))
cv2.putText(img,
            "Uranus",
            (440,220),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(255,255,255))
cv2.putText(img,
            "Neptune",
            (500,220),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(255,255,255))
cv2.imshow('Display Image', img)
cv2.waitKey(0)