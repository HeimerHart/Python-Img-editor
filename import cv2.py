import cv2
image = cv2.imread(r"D:\PROJECTS\PROGRAMMING\PYTHON\image editor\img.jpg", 1)
#bigger = cv2.resize(image, (5*1200, 5*1600))
for i in range(2,500):
 for j in range(2,500):
    print(image[i+1,j+1])
    b=image[i-1,j-1]
'''  image[i,j]=((a[0]+b[0])/2 , (a[1]+b[1])/2 , (a[2]+b[2])/2 )
cv2.imshow('Resized Down by defining height and width', image)
cv2.waitKey() '''
