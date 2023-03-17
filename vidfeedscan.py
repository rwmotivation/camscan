from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
import cv2

kv = '''
Screen:

    MDToolbar:
        title: "Car Number Plate Scanner"
        pos_hint: {"top": 1}
        elevation: 10

    MDLabel:
        text: "Scan car number plates from a video feed"
        halign: "center"

BoxLayout:
    orientation: "vertical"

    Image:
        id: video_feed
        source: ""
        allow_stretch: True

    MDLabel:
        id: number_plate_label
        text: "Number plate will appear here"
        halign: "center"
        font_style: "H6"
'''

class MyApp(MDApp):
    def build(self):
        self.screen_manager = ScreenManager()
        self.video_feed_screen = Screen(name="video_feed_screen")
        self.video_feed_screen.add_widget(Builder.load_string(kv))
        self.screen_manager.add_widget(self.video_feed_screen)
        return self.screen_manager

    def on_start(self):
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0 / 33.0)

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (5, 5), 0)
            edged = cv2.Canny(gray, 50, 200)
            contours, hierarchy = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
            screenCnt = None
            for c in contours:
                peri = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 0.018 * peri, True)
                if len(approx) == 4:
                    screenCnt = approx
                    break
            if screenCnt is not None:
                mask = np.zeros(gray.shape, np.uint8)
                new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1, )
                new_image = cv2.bitwise_and(frame, frame, mask=mask)
                (x, y) = np.where(mask == 255)
                (x1, y1) = (np.min(x), np
