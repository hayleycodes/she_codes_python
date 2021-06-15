# boolean
is_raining = False
is_cold = True
# print(type(is_raining))
# print(type(is_cold))

# print(is_raining)
# print(not is_raining)

# print(is_raining and is_cold) # True


# What is the result of the following comparisons
# when both is_raining and is_cold are True:
# is_raining
# not is_raining
# is_raining or is_cold
# is_raining and not is_cold
# is_raining or not is_cold
# not is_raining and not is_cold
print()
# temp = 16
# print(temp < 18)
# print(temp > 18)

# wind_chill = 3
# print(wind_chill > 4)
# print(temp - wind_chill < 16)

# code = "freeticket"
# print(code == "freeticket")
# print(code != "freeticket")


is_raining = True
if is_raining:
    print("Take an umbrella")
else:
    print("Do not take an umbrella")

print("cats")

if not is_raining:
    print("Do not take an umbrella")
else:
    print("Take an umbrella")


temp = 16
wind_chill = 4

if temp - wind_chill < 16:
    print("Take a jumper.")
elif temp - wind_chill > 30:
    print("It is hot. Stay home.")
else:
    print("Wow, what a lovely day!")


if temp < 16:
    if is_raining:
        print("Just stay home.")
    else:
        print("It's ok today.")
else:
    print()


# if a < 12 and b > 20:

# if a > 12 and a < 20:
