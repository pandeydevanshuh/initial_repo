#just testing out classes in python

class Dog:

  def bark(self):
    print "Bow-wow"

  def __init__(self, name):
    self.name = name

def main():
  zorro = Dog("Zorro")
  zorro.bark()

main()
