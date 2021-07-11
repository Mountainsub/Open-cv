import cv2


img = cv2.imread("Resources/lena.png")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 画像を灰色で出力する
imgBlur = cv2.GaussianBlur(img, (7, 7), 0)　#画像をぼかして出力する
imgCanny = cv2.Canny(img, 150, 200)　#白黒写真として出力する

cv2.imshow("Gray Image", imgGray)

cv2.imshow("Blur Image", imgBlur)


cv2.imshow("Canny Image", imgCanny)
cv2.waitKey(0)
