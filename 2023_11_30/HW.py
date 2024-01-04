class Student:
    def __init__(self,schoolname,name,address,id,departmentname,departmentchairname,credit,gpa):
        self.schoolname=schoolname
        self.name=name
        self.address=address
        self.id=id
        self.departmentname=departmentname
        self.departmentname=departmentchairname
        self.credit=credit
        self.gpa=gpa
    
    def get_schoolname(self):
        return self.schoolname
    
    def set_schoolname(self,value):
        self.schoolname=value

    def get_name(self):
        return self.name
    
    def set_name(self,value):
        self.name=value

    def get_address(self):
        return self.address
    
    def set_address(self,value):
        self.address=value

    def get_id(self):
        return self.id
    
    def set_id(self,value):
        self.id=value

    def get_departmentname(self):
        return self.departmentname
    
    def set_departmentname(self,value):
        self.departmentname=value

    def get_departmentchairname(self):
        return self.departmentchairname
    
    def set_departmentchairname(self,value):
        self.departmentchairname=value

    def get_credit(self):
        return self.credit
    
    def set_credit(self,value):
        self.credit=value

    def get_gpa(self):
        return self.gpa
    
    def set_gpa(self,value):
        self.gpa=value

s1=Student()
s1.set_address('11')
print(s1.get_address())
s1.set_address('gg')
print(s1.get_address())