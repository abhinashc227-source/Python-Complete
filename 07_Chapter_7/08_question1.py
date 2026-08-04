# . Write a program to print multiplication table of a given number using for loop.

l = [1,2,3,4,5,6,7,8,9,10]

for i in l:
    print(i*5)
    i+=1             # This is useless here because in for loop First iteration → i = 1
# print → 5
# then i += 1 → i becomes 2 (BUT only temporarily!)
# Next iteration → Python again picks next value from list → i = 2 ❗

# 👉 So your manual i += 1 is ignored by the loop mechanism
# for i in l: means:
# 👉 “Take each value from the list one by one”
# Python controls i, not you

# In while loop we have to give the i+=1

i = 1
while i <= 10:
    print(i * 5)
    i += 1   # ✅ necessary here