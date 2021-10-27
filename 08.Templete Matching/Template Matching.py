import cv2

image = cv2.imread('image.jpg')
template = cv2.imread('template.jpg')

convertToGrayscale = lambda img : cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imageGray = convertToGrayscale(image)
templateGray= convertToGrayscale(template)

# =============================================================================
# cv2.imshow("image", imageGray)
# cv2.waitKey(0)
# 
# cv2.imshow("image", templateGray)
# cv2.waitKey(0)
# =============================================================================

result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)

minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)

startX, startY = maxLoc

endX, endY = startX + template.shape[0], startY + template.shape[1]

cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 9)

cv2.imshow("Template Matching", image)
cv2.waitKey(0)