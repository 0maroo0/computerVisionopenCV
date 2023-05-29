import cv2 as cv
img = cv.imread('cat.jpg')

# cv.imshow('car',img) 


# in inage frame.shape[i]  if i=>1 that mean width else if 0=> height
# cv.waitKey(0)
#Work in image And video And LiveVideo
def rescale(frame , scale=1):
    width = int(frame.shape[1] *scale)
    height = int(frame.shape[0] *scale)
    dima =(width ,height)


    return  cv.resize(frame,dima,interpolation=cv.INTER_AREA)


ved= cv.VideoCapture('dog.mp4')

while True:
    isTrue, frame =ved.read()
    frame_resized =rescale(frame)
    cv.imshow('viedo',frame_resized)

    if cv.waitKey(20) & 0xff==ord('d'):
        break
ved.release()
cv.destroyAllWindows()


# just in live video
def chamgeres(height,width):
    ved.set(3,width)
    ved.set(4,height)
