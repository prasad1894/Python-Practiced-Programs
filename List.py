food = ["Biryani", "Icecream", "DalRice", "PaniPuri"]
food[0] = "Samosa"
food.append("Noodles")
food.remove("DalRice")
food.pop()
food.insert(1, "Chocolates")
food.sort()
#food.clear()
for i in food:
    print(i)