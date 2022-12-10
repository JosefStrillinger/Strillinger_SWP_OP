from enum import Enum

class Gender(Enum):
    male = 1
    female = 2
    
class Role(Enum):
    mitarbeiter = 1
    leiter = 2
    
class Person:
    
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
   
    def get_name(self):
        return self.name
    
    def get_gender(self):
        return self.gender

class Mitarbeiter(Person):
    
    def __init__(self, name, gender):
        super().__init__(name, gender)
        self.role = Role.mitarbeiter
        
    def get_department(self):
        return self.department
    
    def get_role(self):
        return self.role
        
class Department_Head(Mitarbeiter):
    
    def __init__(self, name, gender):
        super().__init__(name, gender)
        self.role = Role.leiter

class Firma:
    
    def __init__(self, name):
        self.name = name
        self.departments = []     
        
    def count_department(self):
        print("\nAmount of Departments: ")
        return len(self.departments)
    
    def add_department(self, department):
        self.departments.append(department)
        
    def get_mitarbeiter_in_firma(self):
        print("\nMitarbeiter in Firma: ")
        people_count = 0
        for department in self.departments:
            people_count += len(department.dept_mitarbeiter)
        return people_count
    
    def get_dept_heads_in_firma(self):
        print("\nDepartment Heads in Firma: ")
        people_count = 0
        for department in self.departments:
            people_count += len(department.dept_head)
        return people_count
    
    def get_biggest_department(self):
        print("\nBiggest Department in Firma: ")
        dept_people_count = []
        for department in self.departments:
            dept_people_count.append(len(department.dept_mitarbeiter) + len(department.dept_head))       
        index = dept_people_count.index(max(dept_people_count))
        return self.departments[index].name
    
    def get_gender_precentages(self):
        people_count = 0
        male_count = 0
        female_count = 0
        for department in self.departments:
            people_count += (len(department.dept_mitarbeiter) + len(department.dept_head))
            for mitarbeiter in department.dept_mitarbeiter:
                if mitarbeiter.get_gender() == Gender.male:
                    male_count += 1
                else:
                    female_count +=1
            for mitarbeiter in department.dept_head:
                if mitarbeiter.get_gender() == Gender.male:
                    male_count += 1
                else:
                    female_count +=1
        female_precentage = (female_count/people_count)*100
        male_precentage = (male_count/people_count)*100
        return female_precentage, male_precentage
         
class Department:
    def __init__(self, name, dept_head):
        self.name = name
        self.dept_head = []
        self.dept_head.append(dept_head)
        self.dept_mitarbeiter = []
        
    def add_dept_head(self, dept_head):
        self.dept_head.append(dept_head)
        
    def add_dept_mitarbeiter(self, dept_mitarbeiter):
        self.dept_mitarbeiter.append(dept_mitarbeiter)
        
    def get_dept_name(self):
        return self.name
    
    def get_mitarbeiter_count(self):
        return len(self.dept_mitarbeiter)
    
    def get_dept_head_count(self):
        return len(self.dept_head)
    
def main():
    andi = Department_Head("GabeN", Gender.male)
    jessi = Department_Head("Jessi", Gender.female)
    m1 = Mitarbeiter("Josef", Gender.male)
    m2 = Mitarbeiter("Guiseppi", Gender.male)
    ei = Department("EI", andi)
    e2 = Department("EI2", jessi) 
    ei.add_dept_mitarbeiter(m1)
    ei.add_dept_mitarbeiter(m2)
    print(ei.get_dept_head_count)
    print(ei.get_mitarbeiter_count)
    htl = Firma("HTL")
    htl.add_department(ei)
    htl.add_department(e2)
    print(htl.get_mitarbeiter_in_firma())
    print(htl.get_dept_heads_in_firma())
    print(htl.count_department())
    print(htl.get_biggest_department())
    precentage_female, precentage_male = htl.get_gender_precentages()
    print("\nFemale Precentage: " + str(precentage_female))
    print("\nMale Precentage: "+ str(precentage_male))

if __name__ == "__main__":
    main()