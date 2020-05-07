class Settings:
    def __init__(self, color="Grey", size="Normal", resolution="Medium", fps=60):
        self.color = color
        self.size = size
        self.resolution = resolution
        self.fps = fps

    def currentcolor(self):
        print("The current color is " + self.color)

s1 = Settings()
print(s1.resolution)
print(s1.currentcolor())




"""settings = {"Color": "Grey", "Size": "Normal", "Resolution": "Medium", "FPS": "60"}
    print("The current settings are", settings)"""


