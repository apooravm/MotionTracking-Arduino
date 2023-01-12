import cv2 as cv
import time

prevTime = 0
currTime = 0

capture = cv.VideoCapture(0)

while True:
    success, image = capture.read()

    currTime = time.time()

    fps = 1/(currTime-prevTime)
    prevTime = currTime

    cv.putText(image, f"fps: {int(fps)}", (10, 60), cv.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1);

    cv.imshow("img", image)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()