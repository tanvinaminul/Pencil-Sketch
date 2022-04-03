import cv2
image= cv2.imread("img.jpg")
#Convert into grayscale image

gray_image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Invert grayscale image
inverted_image= 255- gray_image

#Blurred image
blured_image= cv2.GaussianBlur(inverted_image, (21,21), 0)
inverted_blurred= 255- blured_image

#Pencil Sketch
pencil_sketch= cv2.divide(gray_image, inverted_blurred, scale= 256.0)

#Show the image
cv2.imshow("Original Image", image)
#cv2.imshow("Gray Image", gray_image)
#cv2.imshow("Inverted Image", inverted_image)
#cv2.imshow("Blurred Image", blured_image)
#cv2.imshow("Inverted Blurred Image", inverted_blurred)
cv2.imshow("Pencil Sketch of the Image", pencil_sketch)
cv2.waitKey(0)

