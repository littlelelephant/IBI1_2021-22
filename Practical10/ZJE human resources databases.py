class Staff(object):
  def __init__(self, name, location, role):
    self.name=name
    self.location=location
    self.role=role
  def information(self):
    print("Name:",self.name,"Location:",self.location,"Role:",self.role)#show thw information
staff=Staff("ZhangShuping","Haining","Leadship")#give an example
staff.information()