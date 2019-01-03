class Home:
    def __init__(self,area):
        self.area = area
        self.containsItem = []
    def __str__(self):
        msg = "当前房间可用面积为:" + str(self.area)