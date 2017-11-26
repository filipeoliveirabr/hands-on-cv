import cv2

coordinates = []
status = False
WINDOWS_NAME = "CROP"
NEW_WINDOWS_NAME = "ROI"

def lets_crop( event, x, y, flags = None, parameters = None ):
    
    global coordinates, status, WINDOWS_NAME
    
    if event == cv2.EVENT_LBUTTONDOWN:
        status = True
        coordinates = [(x,y)]
        
    if event == cv2.EVENT_LBUTTONUP:    
        status = False
        coordinates.append((x,y))
        
        cv2.rectangle(image, coordinates[0], coordinates[1], (255, 0, 0), 1)
        cv2.imshow(WINDOWS_NAME, image)


def check_open_windows():
    if len(coordinates) == 2:
        x1 = coordinates[0][0]
        y1 = coordinates[0][1]
        
        x2 = coordinates[1][0]
        y2 = coordinates[1][1]
        
        print('x1('+repr(x1)+') y1('+repr(y1)+') x2('+repr(x2)+') y2('+repr(y2)+')')
        
        roi = copied_image[ y1 : y2 , x1 : x2 ]        
        height, width = roi.shape[:2]
        cv2.namedWindow(NEW_WINDOWS_NAME, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(NEW_WINDOWS_NAME, width, height)
        
        cv2.imshow(NEW_WINDOWS_NAME, roi)
    
    
image        = cv2.imread("../resource/coffee.jpg")
copied_image = image.copy()

cv2.namedWindow(WINDOWS_NAME, cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback(WINDOWS_NAME, lets_crop)

while True:    
    cv2.imshow(WINDOWS_NAME, image)
    keypress = cv2.waitKey(1)
    
    if keypress == ord('r'):
        image = copied_image.copy()

    if keypress == ord('c'):
        break
    
check_open_windows()
cv2.waitKey(0)
cv2.destroyAllWindows()