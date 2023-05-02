class Student: 
  def __init__(self, name, year, enrolled, gpa):
    self.name = name
    self.year = year
    self.enrolled = enrolled
    self.gpa = gpa
  
  def say_name_and_gpa(self):
    print('The student ' + self.name + '\'s is ' + str(self.gpa) + '!')
sheldon = Student('Sheldon', 2012, True, 4.0)
leonard = Student('Leonard', 2012, True, 3.9)

sheldon.say_name_and_gpa()
leonard.say_name_and_gpa()