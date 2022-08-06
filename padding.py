#Code to add Padding to one Image
import cv2 as cv

path ="image.jpg" # Path of the Image

# The Result can be seen in the Readme File Provided with this Repository

img = cv.imread(path) #Image is Read here 

ht, wd, cc = img.shape #Calculating the Dimensions of the Image Array

Padding_Color = [255,255,255] #Color of the Padding in RGB Format

#Type in the Amount of Padding you need on all Four Sides in pixels
top  = 150
bottom = 150
left = 150
right = 150


new_img = cv.copyMakeBorder(img.copy(),top,bottom,left,right,cv.BORDER_CONSTANT,value=Padding_Color)
type(new_img)

# save result
padded_image = "image_padded.jpg" #Name of the Padded Image
cv.imwrite(padded_image,new_img )

