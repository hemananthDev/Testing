friend1 = input()
friend2 = input()




common_letters = set(friend1) & set(friend2)
for letter in common_letters:
    friend1 = friend1.replace(letter, "", 1)
    friend2 = friend2.replace(letter, "", 1)




value = len(friend1 + friend2)


relationships = ["friend", "love", "affection", "marriage", "enemies", "sister"]

if value > 0:
    while len(relationships) > 1:
        c = value % len(relationships)
        s_index = c - 1 if c > 0 else len(relationships) - 1
        relationships = relationships[s_index + 1 :] + relationships[:s_index]
    print("You both are", relationships[0])
else:
    print("Enter different names")


print("hello world")
print("Hello test")
print("VS commit")