#test2


# 員工類別
class employee:
    def __init__(self,name,salary,hour):
        self.name=name       #名稱
        self.salary=salary   #年薪
        self.hour=hour       #工時

    # 查詢名字
    def get_name(self):
        print(self.name)

    # 查詢年資
    def get_salary(self):
        print(self.salary)

    # 查詢時數
    def get_hour(self):
        print(self.hour)

    # 計算月薪
    def monthly_salary(self,hour):
        print(180*hour)

    # 增加工時
    def add_hour(self,add_hour):
        self.hour=add_hour

    # 增加年薪
    def add_salary(self,add_salary):
        self.salary=add_salary


# 飲料類別
class drink:
    def __init__(self,name,price,sweet):
        self.name=name      #名稱
        self.price=price    #價格
        self.sweet=sweet    #甜度

    #變更名稱
    def ch_name(self,name):
        self.name=name

    #變更甜度
    def ch_sweet(self,sweet):
        self.sweet=sweet

    #變更價格
    def ch_price(self,price):
        self.price=price

    #顯示內容
    def display(self):
        print(f"品名: {self.name}")
        print(f"價格: {self.price}")
        print(f"甜度: {self.sweet}")
    

# 冷飲
class cold_drink(drink):
    def __init__(self, name, price, sweet, ice):
        super().__init__(name, price, sweet)
        self.ice=ice
    
    #顯示內容
    def display(self):
        print("飲料資訊:")
        print("冷飲")
        super().display()
        print(f"冰塊: {self.ice}")
        print()

# 熱飲
class hot_drink(drink):
    def __init__(self, name, price, sweet):
        super().__init__(name, price, sweet)
    
    #顯示內容
    def display(self):
        print("飲料資訊:")
        print("熱飲")
        super().display()
        print()


# 建立員工物件
emp1=employee("小名",1000000,80)
emp2=employee("小白",5000000,90)
emp3=employee("小黑",2000000,50)

emp1.get_name()             #顯示名稱
emp1.get_salary()           #顯示年薪
emp1.get_hour()             #顯示工時
emp1.monthly_salary(30)     #計算月薪
print()
emp1.add_hour(50)           #增加工時
emp1.add_salary(2000000)    #增加年薪
emp1.get_salary()           #顯示變更後年薪
emp1.get_hour()             #顯示變更後工時

# 建立冷飲物件
cold1=cold_drink(name="綠茶",price=20,sweet="無糖",ice="去冰")
cold2=cold_drink("紅茶",30,"微糖","微冰")
cold3=cold_drink("奶茶",40,"正常","正常")

cold1.display()
cold1.ch_name("烏龍茶")      #更改名稱
cold1.ch_price("100")       #更改價格
cold1.ch_sweet("全糖")      #更改甜度
cold1.display()             #顯示變更後內容

# 建立熱飲物件
hot1=hot_drink("阿華田",50,"無糖")
hot2=hot_drink("巧克力牛奶",50,"微糖")
hot3=hot_drink("奶茶",50,"正常")

hot1.display()
hot1.ch_name("奶綠")      #更改名稱
hot1.ch_price("80")       #更改價格
hot1.ch_sweet("半糖")      #更改甜度
hot1.display()             #顯示變更後內容