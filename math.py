#FUNctions
from random import randint
import math
def get_operator():
	i=randint(1,4)
	if i == 1:
		return "*"
	elif i == 2:
		return "/"
	elif i == 3:
		return "+"
	elif i == 4:
		return "-"

def find_answer():
	if operator == "*":
		return (x*y)
	elif operator == "/":
		return round((x/y),[2])
	elif operator == "+":
		return (x+y)
	elif operator == "-":
		return (x-y)

#Variables
x = randint(1, 20)
y = randint(1, 20)
operator = get_operator()
real_answer = find_answer()
print(str(x)+operator+str(y))
user_input = input("What is the answer to the question above?")
if user_input == real_answer:
	print("Correct!")
else:
	print("Incorrect")
	print("The correct answer is "+str(real_answer))
