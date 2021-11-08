highestnum = 0

for i in range(0, 4):
    userinput = input("Number please...")
    usernum = int(userinput)
    print("user entered: " + str(usernum))
    if usernum > highestnum:
        highestnum = usernum
        print("Updating highest number...")
    else:
        print("This is not highest number...")
print("The highest numbered is" + str(highestnum))
