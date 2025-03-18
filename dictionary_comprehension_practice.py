#Consider the following problem where you want to create a new dictionary 
#where the key is a number divisible by 2 in a range of 0-10, 
#and its value is the square of the number.
#Let's see how you can solve the same problem using a for loop and dictionary comprehension:

numbers = range(10)

new_dict_for = {}

# Add values to `new_dict` using for loop
for n in numbers:
    if n%2==0:
        new_dict_for[n] = n**2

print(new_dict_for)

#Dictionary comprehension method:
new_dict_comp = {x:x**2 for x in numbers if x%2 == 0}

print(new_dict_comp)
