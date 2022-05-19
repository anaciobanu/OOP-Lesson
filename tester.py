class Tester():

    def __init__(self, name, title) -> None:
        self.name = name
        self.title = title

    def get_emloyee_details(self):
       return(f"My name is {self.name} and I'm {self.title}" )

          
James = Tester('James', 'CEO')
David = Tester('David', 'Web Designer')    
Arianna = Tester('Arianna', 'Business Analyst') 
  
