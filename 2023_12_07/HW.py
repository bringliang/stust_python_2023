class sports:
    def __init__(self,name):
        self._name=name
    
    @property
    def sports_name(self):
        return self._name

    @sports_name.setter
    def sports_name(self, val):
        self._name=val


class landsports(sports):
    def __init__(self, name, field):
        super().__init__(name)
        self.field=field

    @property
    def landsports_field(self):
        return self.field

    def practice(self):
        print("Doing Land Sports practice") 

class watersports(sports):
    def __init__(self, name, act):
        super().__init__(name)
        self.act=act

    @property
    def watersports_act(self):
        return self.act

    def practice(self):
        print("Doing Water Sports practice")

if __name__ == "__main__":
    baseball=landsports("baseball", "baseball field")
    print(baseball.sports_name)
    print(baseball.landsports_field)
    print(baseball.practice()) 

    
    swim=watersports("swim", "strap on your skills")
    print(swim.sports_name)
    print(swim.watersports_act)
    print(swim.practice())

    sports = sports("Softball")
    print(sports.sports_name)
    print(sports.practice())