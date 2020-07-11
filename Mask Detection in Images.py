import cv2

path = 'Resources/haarcascades/haarcascade_mask2.xml'  # PATH OF THE CASCADE
objectName = 'Mask On'  # OBJECT NAME TO DISPLAY
color = (255, 0, 0)

# LOAD THE CLASSIFIERS DOWNLOADED
cv2.namedWindow("Result")
cascade = cv2.CascadeClassifier(path)
img = cv2.imread('Resources/mask.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

objects = cascade.detectMultiScale(imgGray, 1.1, 1)

# DISPLAY THE DETECTED OBJECTS
for (x, y, w, h) in objects:
       cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
       cv2.putText(img, objectName, (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
       roi_color = img[y:y + h, x:x + w]

cv2.imshow("Result", img)
cv2.waitKey(0)