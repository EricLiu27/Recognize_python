num1 = 42 #variable declaration, interger numbers
num2 = 2.3 #variable declaration, float numbers
boolean = True #variable declaration, boolean
string = 'Hello World' #variable declaration, strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, strings, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, boolean, interger number, strings, initialize dictionaries
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, strings, intialize tuples
print(type(fruit)) #log statement, type check, tuples access value
print(pizza_toppings[1]) #log statement, list access value
pizza_toppings.append('Mushrooms') # list add value
print(person['name']) #log statement, dictionary access value 
person['name'] = 'George' #dictionary change value 
person['eye_color'] = 'blue' #dictionary add value
print(fruit[2]) #log statemen, tuples acess value

if num1 > 45: #conditional if
    print("It's greater") #log statement
else: #conditional else
    print("It's lower") #log statement

if len(string) < 5: #length check, conditional if 
    print("It's a short word!") #log statement
elif len(string) > 15: #length check, conditional else if
    print("It's a long word!") #log statement
else: #conditional else
    print("Just right!") #log statement

for x in range(5): #for start
    print(x) #log statement, stop
for x in range(2,5): #for start
    print(x) #log statement, stop
for x in range(2,10,3): #for start, increment
    print(x) #log statement, stop
x = 0 #variable declaration, Numbers,
while(x < 5): #while start
    print(x) #log statement, while stop,
    x += 1 #while increment

pizza_toppings.pop() #list delete value
pizza_toppings.pop(1) #list delete value

print(person) #log statement, dictionary access values
person.pop('eye_color') #dictionary delete value
print(person) #log statement, dictionary access values

for topping in pizza_toppings: #for loop start, increment
    if topping == 'Pepperoni': #if, 
        continue #for loop continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': #if, 
        break #for loop stop, for loop break 

def print_hello_ten_times(): #function
    for num in range(10): #for loop start
        print('Hello') #log statement, for loop stop

print_hello_ten_times() # calling the function

def print_hello_x_times(x):# function paramenters
    for num in range(x):#for loop start
        print('Hello') #log statement, for loop stop

print_hello_x_times(4) # function argument

def print_hello_x_or_ten_times(x = 10): # function paramenters
    for num in range(x): #for loop start
        print('Hello') #log statement, for loop stop

print_hello_x_or_ten_times()  # calling the function
print_hello_x_or_ten_times(4) # function argument


"""
Bonus section # multiline comment 
"""

# print(num3) # single line comment, NameError: name <variable name> is not defined
# num3 = 72 # single line comment, NameError: name <variable name> is not defined
# fruit[0] = 'cranberry' # single line comment, TypeError: 'tuple' object does not support item assignment, Tuples change value
# print(person['favorite_team']) # single line comment, KeyError: 'favorite_team'
# print(pizza_toppings[7]) # single line comment, IndexError: list index out of range
#   print(boolean) # single line comment, IndentationError: unexpected indent
# fruit.append('raspberry') # single line comment, AttributeError: 'tuple' object has no attribute 'append', Tuples add value
# fruit.pop(1) # single line comment, AttributeError: 'tuple' object has no attribute 'pop', Tuples delete value