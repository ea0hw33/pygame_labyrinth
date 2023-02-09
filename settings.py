class Settings:
    def __init__(self, width=400, height=400, fps=60, speed=5):
        self.speed = speed
        self.resolution = 0
        self.fps = fps
        self.height = height
        self.width = width

    def resolution_setter(self, level):
        if self.width/len(level[0]) == self.height/len(level):
            self.resolution = self.height/len(level) #заменить на целочисленное деление при ошибке
