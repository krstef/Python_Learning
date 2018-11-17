import cv2

img_read = cv2.imread("smallgray.png", 0)

x = img_read[0:2, 2:4]

#iterate trought the list
for i in img_read.T:
    print(i)

#iterate trought the list and output the flat list
for j in img_read.flat:
    print(j)

#create stack array with tiple
arrayX = numpy.hstack((img_read, img_read, img_read))
print(x)
print(img_read)
