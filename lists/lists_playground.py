chilli_wishlist = [
    "igloo",
    "chicken",
    "donut toy",
    "cardboard box"
]
print(chilli_wishlist)
print(chilli_wishlist[0])
print(len(chilli_wishlist))
# print(chilli_wishlist[4])
print(chilli_wishlist[-1])
print(chilli_wishlist[0:2])
chilli_wishlist[1] = "carrot"
print(chilli_wishlist)

# Print the sublist of items in positions 2 through to 3.
print(chilli_wishlist[2:4])
# Print the item in the -3 position.
print(chilli_wishlist[-3])
print(chilli_wishlist)
# adding items
chilli_wishlist.append("dig mat")
print(chilli_wishlist)
chilli_wishlist.extend(["kong", "tennis ball", "crocodile toy"])
print(chilli_wishlist)
chilli_wishlist.insert(3, "peanut butter")
print(chilli_wishlist)
print()
# remove items
print(chilli_wishlist.pop())
print(chilli_wishlist)
print(chilli_wishlist.pop(2))
print(chilli_wishlist)
chilli_wishlist.remove("kong")
print(chilli_wishlist)
print()
# Add a new item to position -2
chilli_wishlist.insert(-2, "bone")
print(chilli_wishlist)
# Remove the third item from the list
chilli_wishlist.pop(2)
print(chilli_wishlist)
# Add four new items to the end of the list.
chilli_wishlist.extend(["treats", "milk sticks", "bird", "will"])
# Remove the “igloo” item from the list.
chilli_wishlist.remove("igloo")

print(chilli_wishlist)

print()
chilli_wishlist = [
    ["igloo"],  # bed
    ["donut toy", "tennis ball", "crocodile"],  # toys
    ["chicken", "peanut butter"],  # treats
    ["cardboard box", "kong"]  # puzzles
]

print(chilli_wishlist)
print(chilli_wishlist[0][0])
print(chilli_wishlist[3][0])
