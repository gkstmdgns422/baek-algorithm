text = input()

acronym = ["U","C","P","C"]
count = 0
i = 0
for letter in text:
    if letter.isupper() and letter == acronym[i]:
        count += 1
        i += 1
        if count == 4:
            break
if count == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")
