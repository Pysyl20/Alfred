import pyttsx3


class Speech:
    def __init__(self):
        self.speacking = False
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 130)
        self.voices = self.engine.getProperty("voices")
        # self.voice = self.voices[26]
        self.engine.setProperty("voice", 'fr')
