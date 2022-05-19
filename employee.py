class Employee:
    vacation_days = 20

class Tester(Employee):

    def __init__(self, name, title) -> None:
        self.name = name
        self.title = title

    def get_emloyee_details(self):
       return(f"My name is {self.name} and I have {self.vacation_days} vacation days" )

          
James = Tester('James', 'CEO')
David = Tester('David', 'Web Designer')    
Arianna = Tester('Arianna', 'Business Analyst') 