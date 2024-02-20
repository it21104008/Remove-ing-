print("*"*10)
print("------ I HATE \"ING\"------- ")

word = input("Enter Your Word:")
lastWord = word[-3:]

if "ing" == lastWord:
    print(word[:-3])
else:
    print(word)