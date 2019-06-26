

class Person:
    def __init__(self, fn, n):
        self.firstname = fn
        self.surname = n
        
    def name(self):
        return self.firstname + " " + self.surname

        
    #def firstname(self):
    #    return self.firstname
    
    #def surname(self):
    #    return self.surname
        
 
class Knight(Person):
    def __init__(self, fn, n, affiliation):
        super().__init__(fn, n)
        self.affiliation = affiliation
        
    def name(self):
        return self.firstname + " " + self.surname + " of " + self.affiliation
        
    
    
p = Person("Jean", "Marne")
k = Knight("Pierre", "Hovelin", "the Gray Tower")

print(p.name())
print(k.name())