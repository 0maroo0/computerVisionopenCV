import cv2 as cv
# img = cv.imread('cat.jpg')

# cv.imshow('car',img) cv.waitKey(0)


#read vidro
ved= cv.VideoCapture('cat.mp4')

while True:
    isTrue, frame =ved.read()
    cv.imshow('viedo',frame)
    if cv.waitKey(20) & 0xff==ord('d'):
        break
ved.release()
cv.destroyAllWindows()
