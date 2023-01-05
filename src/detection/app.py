import cv2 as cv
import handTrackingModule as handTrack
import time

detector = handTrack.HandDetector()
capture = cv.VideoCapture(0)

prevTime = 0
currTime = 0

def drawCoordsOnImage(image, coords_ALL):
    for ALL_hands in coords_ALL:
        for coords in ALL_hands:
            # coords of all landmarks
            cv.circle(image, (coords[1], coords[2]), 2, (255, 255, 0), -1)
    return image

while True:
    success, img = capture.read()
    coords = detector.getHandCoords(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    img = drawCoordsOnImage(img, coords)

    currTime = time.time()
    fps = 1/(currTime-prevTime)
    prevTime = currTime
    kl = f"FPS: {str(int(fps))}"

    cv.putText(img, kl, (10, 60), cv.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)

    cv.imshow("img", img)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()