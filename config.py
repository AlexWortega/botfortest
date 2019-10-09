import numpy as np
import cv2

filename = 'exmpl.jpg'
cup = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while True:
    _, frame = cup.read()
# frame = cv2.resize(frame,None,None,0.5,0.5)
    #blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# find Harris corners
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray, 2, 3, 0.04)
    dst = cv2.dilate(dst, None)
    ret, dst = cv2.threshold(dst, 0.01*dst.max(), 255, 0)
    dst = np.uint8(dst)
# find centroids
    ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
# define the criteria to stop and refine the corners
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
    corners = cv2.cornerSubPix(gray, np.float32(centroids), (5, 5), (-1, -1), criteria)
# Now draw them
    res = np.hstack((centroids, corners))
    res = np.int0(res)
    cv2.imshow("Frame", res)
    key = cv2.waitKey(1)
    if key == 27:
        cup.release()
        cv2.destroyAllWindows()
        break


#cv.imwrite('subpixel5.png',img)
