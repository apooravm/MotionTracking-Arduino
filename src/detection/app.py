import cv2 as cv
import handTrackingModule as handTrack
import time
import serial
from pynput.mouse import Button, Controller

try:
    ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)
except:
    print("Port Unavailable!")
serial_COMM = True

def writeToSerial(inp):
    if serial_COMM:
        ser.write((str(inp) + '\n').encode())
        # delay for arduino => 20ms
        time.sleep(0.04)

def getMousePos():
    mouse = Controller()
    mx, my = mouse.position
    return [int(mx), int(my)]


pxRange = 1900
pyRange = 600

detector = handTrack.HandDetector()
capture = cv.VideoCapture(0)

prevTime = 0
currTime = 0

servoValue = 0

trackFingerIndex = 9

def drawCoordsOnImage(image, coords_ALL, drawLine=False, drawPoint=True):
    if drawPoint:
        for ALL_hands in coords_ALL:
            for coords in ALL_hands:
                # coords of all landmarks
                if coords[0] == trackFingerIndex:
                    fingerPoint = (coords[1], coords[2])     
        try:
            writeToSerial(int(fingerPoint[0]))
            cv.circle(image, fingerPoint, 5, (0, 255, 255))
            print(fingerPoint, end="                          \r")
        except:
            pass
        return image

    if drawLine:
        pts1 = []
        pts2 = []
        for ALL_hands in coords_ALL:
            for coords in ALL_hands:
                # coords of all landmarks
                if coords[0] == 0:
                    pts1.append((coords[1], coords[2]))
                if coords[0] == 12:
                    pts1.append((coords[1], coords[2]))

                    print(coords[1], end="                          \r")
                    writeToSerial(int(coords[1]))
        try:
            cv.line(image, pts1[0], pts1[1], (0, 255, 255), 1)
        except:
            pass
        return image

    for ALL_hands in coords_ALL:
        for coords in ALL_hands:
            # coords of all landmarks
            if coords[0] == 12:

                print(coords[1], end="                          \r")
                writeToSerial(int(coords[1]))
            cv.circle(image, (coords[1], coords[2]), 2, (255, 255, 0), -1)
    return image

while True:
    success, img = capture.read()
    coords = detector.getHandCoords(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    img = drawCoordsOnImage(img, coords, drawLine=True)

    currTime = time.time()
    fps = 1/(currTime-prevTime)
    prevTime = currTime
    kl = f"FPS: {str(int(fps))}"

    cv.putText(img, kl, (10, 60), cv.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)

    # posValue = int(getMousePos()[0])
    posValue = servoValue
    # writeToSerial(posValue)

    # print(posValue, end="                          \r")

    cv.imshow("img", img)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
