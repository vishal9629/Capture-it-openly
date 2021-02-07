import numpy as np
import cv2
import sys

flooded=None
img=None
seed_pt=None
mask = None
h,w=None,None

def update(dummy=None):
    global flooded
    global img
    flooded = img.copy()
    if seed_pt is None:
        cv2.imshow('floodfill', img)
        return
    flooded = img.copy()
    mask[:] = 0
    cv2.floodFill(flooded, mask, seed_pt, (0, 0, 0))
    cv2.circle(flooded, seed_pt, 2, (0, 0, 255), -1)
    cv2.imshow('floodfill', flooded)

def onmouse(event, x, y, flags, param):
    global seed_pt
    if flags & cv2.EVENT_FLAG_LBUTTON:
        seed_pt = x, y
        update()


def flood_fill(img_path,main_path):
    global img
    global mask
    global h,w
    global flooded
    img=cv2.imread(img_path,0)
    main_image=cv2.imread(main_path)
    h, w = img.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
    seed_pt = None
    fixed_range = True


    update()
    cv2.setMouseCallback('floodfill', onmouse)

    while True:
        ch = cv2.waitKey()
        if ch == 27:
            break
        if ch == ord('f'):
            main_image=cv2.resize(main_image,(flooded.shape[1],flooded.shape[0]))
            print(flooded.shape)
            cv2.resize(flooded,(flooded.shape[1],flooded.shape[0]))
            #b,g,r = cv2.split(main_image)           
            #main_image= cv2.merge([r,g,b])
            for i in range(flooded.shape[0]):
                for j in range(flooded.shape[1]):
                    if flooded[i][j]==255:
                        main_image[i][j][0]=0
                        main_image[i][j][1]=0
                        main_image[i][j][2]=0
            cv2.imshow('masked image',main_image,)
            cv2.imwrite(r'C:\Users\kanishkaditya\Desktop\newDataset\flooded1.jpg',flooded)
            cv2.imwrite(r'C:\Users\kanishkaditya\Desktop\newDataset\filledImage1.jpg',main_image)
            cv2.waitKey(0)
            break
            
    cv2.destroyAllWindows()
    return flooded

flood_fill(img_path=r'C:\Users\kanishkaditya\Desktop\newDataset\247.png',main_path=r'C:\Users\kanishkaditya\Desktop\newDataset\main247.jpg')
