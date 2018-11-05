#if you want to have the input at the end of the question
#use, end=' '
#if you want it on a new line just get rid of the 
#end=' '
print("How old are you?")
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()
#regular interpolation
print(f"So, you're {age} old, {height} tall and {weight} heavy.")