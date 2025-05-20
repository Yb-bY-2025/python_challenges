# Create a class named Person
# Create objects of the classe using heritage and polymorphisms

class person:
  def __init__(self , name, age , outfit):
    self.name = name
    self.age = age 
    self.outfit = outfit
  def what_outfit(self):
    return self.outfit + " is cool "

class normal_guy(person):
  def __init__(self , name, age , outfit , sexe):
    super().__init__(name,age,outfit)
    self.sexe = sexe
  def what_outfit(self):
    return  super().what_outfit + " and elegant "

def formating_print(object):
  return  object.name + " is " +  object.age + " by now , and his outfit : " +  object.outfit + " , and finally  is a " +  object.sexe


  
Normal_guys = [ 
              normal_guy("jonathan", 23, "pants" , "male"),
              normal_guy("john", 40, "shorts" , "male"),
              normal_guy("samantha", 37, "T-shirt" , "female"),
              normal_guy("sara", 53, "under_wear" , "female")
              ]

formatted_list = [ formating_print(obj)  for obj in Normal_guys ]
print(formatted_list)
