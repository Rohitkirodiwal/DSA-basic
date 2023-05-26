str = "Python of Edyoda "
index = -1
non_repeating = ""
for i in str:
    if str.count(i) == 1:
        non_repeating += i
        break
    else:
        index += 1
if index == 1:
    print("Either all characters are repeating or string is empty")
else:
    print("First non-repeating character is", non_repeating)