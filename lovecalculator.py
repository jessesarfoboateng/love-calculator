print("Welcome to the Love Calculator! ")
user_name = input("What is your name? \n")
crush_name = input("What is their name? \n")
user_name = user_name.lower()
crush_name = crush_name.lower()
love_name = user_name + crush_name
t = love_name.count("t")
r = love_name.count("r")
u = love_name.count("u")
e = love_name.count("e")
true_total = t + r + u + e

l = love_name.count("l")
o = love_name.count("o")
v = love_name.count("v")
love_total = l + o + v + e

true_total = str(true_total)
love_total = str(love_total)
love_score = int(true_total + love_total)

if (love_score < 10) or (love_score) > 90:
    print(f"Your score is {love_score},you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score},you are alright together.")
else:
    print(f"Your score is {love_score}.")