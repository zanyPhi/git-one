class Learning_mate:
    def __init__(self, name, age, mate_name, mate_age):
        self.name = name
        self.age = age
        self.mate_name = mate_name
        self.mate_age = mate_age
    
    def age_gap(self):
        gap = abs(self.age - self.mate_age)
        return gap

    def message(self):
        print(f"{self.name} and {self.mate_name} are learning mates")
mate1 = Learning_mate('Sam', 20, 'Toby', 20)