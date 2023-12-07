class student:
    def __init__(self,name):
        self.name=name

    @property
    def student_name(self):
        print(f'"{self.name}" was accessed')
        return self.name

    @student_name.setter
    def student_name(self, val):
        print(f'"{self.name}" is now "{val}"')
        self.name=val

    @student_name.deleter
    def student_name(self):
        print(f'"{self.name}" was deleted')
        del self.name


if __name__ == "__main__":

    s1=student("kk")
    print(s1.student_name)
    s1.student_name="qq"
    del s1.student_name
    print(s1.student_name)