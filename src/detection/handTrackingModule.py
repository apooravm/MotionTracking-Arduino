import mediapipe as mp

class HandDetector():
    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils
        self.drawLines = False

    def getHandCoords(self, image):
        # imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        retArray = []

        results = self.hands.process(image)
        if results.multi_hand_landmarks:
            for singleHand in results.multi_hand_landmarks:
                if self.drawLines:
                    self.mpDraw.draw_landmarks(img, singleHand, self.mpHands.HAND_CONNECTIONS)
                # for handLms in singleHand:
                singleHandArray = []
                for id, lm in enumerate(singleHand.landmark):
                    # lm => [x, y, z] of the current landmark; index finger, pointer finger, thumb etc
                    h, w, c = image.shape #height, width, channel
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    singleHandArray.append([id, cx, cy])
                retArray.append(singleHandArray)
        return retArray

if __name__ == "__main__":
    import cv2 as cv
    cap = cv.VideoCapture(0)
    detector = HandDetector()
    detector.drawLines = True
    while True:
        success, img = cap.read()

        results = detector.hands.process(cv.cvtColor(img, cv.COLOR_BGR2RGB))
        if results.multi_hand_landmarks:
            for hand in results.multi_hand_landmarks:
                detector.mpDraw.draw_landmarks(img, hand, detector.mpHands.HAND_CONNECTIONS)

        cv.imshow("image", img)
        cv.waitKey(1)