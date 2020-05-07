class Settings:
    def __init__(self, color="Grey", size="Normal", resolution="Medium", fps=60):
        self.color = color
        self.size = size
        self.resolution = resolution
        self.fps = fps

    def change(self):
        self.color = input("Enter a new color")
        self.size = input("Enter the size")
        self.resolution = input("Enter the resolution")
        self.fps = input("Enter the FPS")
        print()

s1 = Settings()
print(s1.color)
print(s1.change())




"""settings = {"Color": "Grey", "Size": "Normal", "Resolution": "Medium", "FPS": "60"}
    print("The current settings are", settings)"""


