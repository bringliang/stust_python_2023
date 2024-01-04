#test1

class FriedChicken:
    def __init__(self, price, spiciness, size, time, pepper):
        self.price = price  # 價格
        self.spiciness = spiciness  # 辣度
        self.size = size  # 炸雞的大小
        self.time = time  # 等待時間
        self.pepper = pepper  # 要不要胡椒

    # 顯示炸雞資訊
    def display(self):
        print("炸雞資訊:")
        print(f"價格: {self.price}")
        print(f"辣度: {self.spiciness}")
        print(f"炸雞大小: {self.size}")
        print(f"等待時間: {self.time}分鐘")
        print(f"胡椒: {self.pepper}")
        print()

    # 改變辣度
    def ch_pepper(self,spiciness):
        self.spiciness=spiciness
    
    # 改變大小
    def ch_size(self,size):
        self.size=size

# 建立4個物件
c1=FriedChicken(70,"大辣","特大",5,"要")
c2=FriedChicken(60,"中辣","大",5,"不要")
c3=FriedChicken(50,"小辣","中",5,"要")
c4=FriedChicken(40,"微辣","小",5,"不要")

c1.display()
c2.display()
c3.display()
c4.display()

#改變胡椒
c1.ch_pepper("不要")
c2.ch_pepper("要")
c3.ch_pepper("不要")
c4.ch_pepper("要")

#改變大小
c1.ch_size("小")
c2.ch_size("中")
c3.ch_size("大")
c4.ch_size("特大")

print("改變後")
c1.display()
c2.display()
c3.display()
c4.display()