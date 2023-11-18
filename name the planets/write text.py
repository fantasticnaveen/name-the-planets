import cv2

img = cv2.imread("solar-system.jpg")

sunText = "sun"

mercuryText = "mercury"

venusText = "venus"

earthText = "earth"

marsText = "mars"

jupiterText = "jupiter"

saturnText = "saturn"

uranusText = "uranus"

neptuneText = "neptune"
cv2.putText(img,
            sunText,
            (100,100),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=2,
            color=(255,255,255)
            )

cv2.putText(img,
            mercuryText,
            (125,200),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5,
            color=(255,255,255)
            )

cv2.putText(img,
            venusText,
            (225,200),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5,
            color=(255,255,255)
            )

cv2.putText(img,
            earthText,
            (325,200),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5,
            color=(255,255,255)
            )

cv2.putText(img,
            marsText,
            (425,200),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5,
            color=(255,255,255)
            )

cv2.putText(img,
            jupiterText,
            (625,200),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5,
            color=(255,255,255)
            )

cv2.putText(img,
            saturnText,
            (825,200),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5,
            color=(255,255,255)
            )

cv2.putText(img,
            uranusText,
            (1025,200),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5,
            color=(255,255,255)
            )

cv2.putText(img,
            neptuneText,
            (1125,200),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5,
            color=(255,255,255)
            )


cv2.imshow("solar system",img)

cv2.imwrite("Poster.jpg",img)

cv2.waitKey(0)