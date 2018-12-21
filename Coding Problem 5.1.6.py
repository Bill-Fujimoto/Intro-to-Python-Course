#Copy both your code and ours from the previous exercise.
#You should copy your Burrito class and our Meat, Rice, and
#Beans classes into this exercise.
#
#In this exercise, you won't edit any of your code from the
#Burrito class. Instead, you're just going to write a
#function to use instances of the Burrito class.
#
#Write a function called total_cost. total_cost should take
#as input a list of instances of Burrito, and return the
#total cost of all those burritos together as a float.
#
#Hint: Don't reinvent the wheel. Use the work that you've
#already done. The function can be written in only five
#lines, including the function declaration.
#
#Hint 2: The exercise here is to write a function, not a
#method. That means this function should *not* be part of
#the Burrito class.


#Paste your previous code here.
class Meat:
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["chicken", "pork", "steak", "tofu"]:
            self.value = value
        else:
            self.value = False

class Rice:
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["brown", "white"]:
            self.value = value
        else:
            self.value = False
    
class Beans:
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["black", "pinto"]:
            self.value = value
        else:
            self.value = False

#Write your code here!
class Burrito:

	def __init__(self, meat, to_go, rice, beans, extra_meat=False, guacamole=False,
	cheese=False, pico=False, corn=False):
		self.set_to_go(to_go)
		self.meat = Meat(meat)
		#print(self.meat)
#Apparently, the preferred way is to assign the new object to the variable without
#combining the use of the methods from that object.  So "self.meat" when printed will
#be a strange looking string of results but this is OK.  The methods can be added later
#where specific use of the variable occur.
		self.rice = Rice(rice)
		#print(self.rice)
		self.beans = Beans(beans)
		#print(self.beans)
		self.set_extra_meat(extra_meat)
		self.set_guacamole(guacamole)
		self.set_cheese(cheese)
		self.set_pico(pico)
		self.set_corn(corn)
		
	def set_to_go(self, to_go):
		if type(to_go) == bool:
			self.to_go = to_go
		else:
			self.to_go = False
	
	def set_meat(self, meat):
		self.meat = Meat(meat)
    		
	def set_rice(self, rice):
		self.rice = Rice(rice)
    
	def set_beans(self, beans):
		self.beans = Beans(beans)
			
	def set_extra_meat(self, extra_meat):
		if type(extra_meat) == bool:
			self.extra_meat = extra_meat
		else:
			self.extra_meat = False
		
	def set_guacamole(self, guacamole):
		if type(guacamole) == bool:
			self.guacamole = guacamole
		else:
			self.guacamole = False
		
	def set_cheese(self, cheese):
		if type(cheese) == bool:
			self.cheese = cheese
		else:
			self.cheese = False

	def set_pico(self, pico):
		if type(pico) == bool:
			self.pico = pico
		else:
			self.pico = False
		
	def set_corn(self, corn):
		if type(corn) == bool:
			self.corn = corn
		else:
			self.corn = False
		
	def get_to_go(self):
		return self.to_go
	def get_meat(self):
		return self.meat.get_value()
	def get_rice(self):
		return self.rice.get_value()
	def get_beans(self):
		return self.beans.get_value()
	def get_extra_meat(self):
		return self.extra_meat
	def get_guacamole(self):
		return self.guacamole
	def get_cheese(self):
		return self.cheese
	def get_pico(self):
		return self.pico
	def get_corn(self):
		return self.corn
	def get_cost(self):
		self.cost=5
		if self.meat.get_value() in ["chicken","pork","tofu"]:
			self.cost = self.cost + 1 + 1*self.extra_meat
		elif self.meat.get_value() == "steak":
			self.cost = self.cost + 1.5 +1*self.extra_meat
		self.cost = self.cost + 0.75*self.guacamole
		return self.cost


#Write your new function here.
def total_cost(burrito_list):
	total=0
	for burrito in burrito_list:
		total += burrito.get_cost()
	return total



#You can add code below to test your function. We'd suggest
#creating a couple instances of Burrito, adding them to a
#list, then passing that list to total_cost and printing the
#result.
burrito1 = Burrito("steak", True, True, True, False, True)
burrito2 = Burrito("pork", True, True, True, False, True)
burrito3 = Burrito("chicken", True, True, True, False, True)
burritos = [burrito1, burrito2, burrito3]
print(total_cost(burritos))
