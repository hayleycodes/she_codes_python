def create_greeting(name):
    greeting = f"Hello, {name}!"
    # print(greeting)
    return greeting


chilli_greeting = create_greeting("Chilli")
# print(chilli_greeting)
# print(create_greeting("Chilli"))
# print(create_greeting("Ivy"))
# print(create_greeting("Tedric"))
# print(create_greeting("Princi"))
# print(create_greeting("Remus"))
# print(create_greeting("Fleur"))


def convert_cm_to_in(length_cm):
    length_in_inches = round(length_cm / 2.54, 2)
    return length_in_inches


print(convert_cm_to_in(20))
# print(length_in_inches)

# define a function to convert inches to cms


def convert_in_to_cms(length_in):
    length_in_cms = length_in * 2.54
    return length_in_cms


print(convert_in_to_cms(2))


def calculate_mean(a, b):
    total = a + b
    mean = total / 2
    return mean


print(calculate_mean(2, 4))
print(calculate_mean(3, 4))
print(calculate_mean(5, 10))
