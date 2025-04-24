# Insted of student dict we will have student object
# represent a class as a list of objects---> process that

class Student:
    def __init__(self,name,regid):
        self.name = name
        self.regid = regid
        self.details = {"age" : 0}
        self.marks = {"physics" :0,"chemistry" : 0,"maths" : 0,"biology" : 0}
        self.average = 0
        self.rank = 0

    def __repr__(self):
        return str(self.name), str(self.regid)
    
    def __str__(self):
        return ','.join([str(self.name)])
        '''
        return ','.join(str(self.name) , str(self.age),str(self.regid),','.join(self.marks.values()))

        '''
        
    

    
    def calculate_average(self):
        self.average = sum((self.marks.values() )/ len(self.marks.values()))
    
    def set_rank(self, rank):
        self.rank = rank
    
    def set_marks(self,**marks_list): # set_marks("phy",99)
        
        pass

    def get_marks(self):
        return self.marks
    


# ----------------------------------------------------------------------
if __name__ == "__main__":
    s = Student("Anil",12)
    s.set_marks(phy = 90,chem = 80, math = 90, bio =77)
    s.calculate_average()
    print(s)



