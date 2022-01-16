#Code to add Padding to one Image
import cv2 as cv

path ="image.png" # Path of the Image

img = cv.imread(path) #Image is Read here 

ht, wd, cc = img.shape #Calculating the Dimensions of the Image Array

Padding_Color = [255,255,255] #Color of the Padding in RGB Format

top  = 10
bottom = 10
left = 10
right = 10


new_img = cv.copyMakeBorder(img.copy(),top,bottom,left,right,cv.BORDER_CONSTANT,value=Padding_Color)


# save result
new_path = "Padded/" #Path to Store Padded Images
cv.imwrite(new_path, new_img)
