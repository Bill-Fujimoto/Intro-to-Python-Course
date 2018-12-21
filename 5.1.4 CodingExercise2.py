class TodoItem:
    def __init__(self, title, description, completed=False):
        self.title = self.setTitle(title)
        self.description = self.setDescription(description)
        self.completed = self.setCompleted(completed)

    def getTitle(self):
        print("title accessed")
        return self.title

    def getDescription(self):
        print("description accessed")
        return self.description

    def getCompleted(self):
        print("completed accessed")
        return self.completed


    def setTitle(self, newtitle):
        if type(newtitle) == str:
            print("title changed")
            return newtitle
        else:
            print("invalid value title changed")
            return None
            
    def setDescription(self, newdescription):
        if type(newdescription) == str:
            print("description changed")
            return newdescription
        else:
            print("invalid value description changed")
            return None
            
    def setCompleted(self, newcompleted):
        if type(newcompleted) == bool:
            print("completed changed")
            return newcompleted
        else:
            print("invalid value completed changed")
            return None
  
            
#ThisIsaTest=TodoItem(4,5, "str")
ThisIsaTest=TodoItem("Start","Finish", True)
print()
print("self.title:",str(ThisIsaTest.title))
print("self.description:",str(ThisIsaTest.description))
print("self.description:",str(ThisIsaTest.completed))
#print(type(ThisIsaTest.title))
print()
#print(ThisIsaTest.setTitle("A"))
#print(ThisIsaTest.setDescription("B"))
#print(ThisIsaTest.setCompleted(True))
print(ThisIsaTest.getTitle())
print(ThisIsaTest.getDescription())
print(ThisIsaTest.getCompleted())
