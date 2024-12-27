f = open("file.txt")
# line1 = f.readlines()
# print(line1, type(line1))

# line2 = f.readlines()
# print(line2, type(line2))

# line3 = f.readlines()
# print(line3, type(line3))

# line4 = f.readlines()
# print(line4 , type(line4))

# f.close()

# f = open("file.txt")
# data = f.read()
# print(data)
# f.close()

# st = "Hey I am student what was your opinion."
# f = open("file.txt", "w")
# data = f.write(st)
# print(data)
# f.close()

# str = "Hey Alpesh how are you and find the way you are become very good software engineer."

# f = open("file.txt", "w")
# data = f.write(str)
# print(str)
# f.close()

line = f.readlines()
while(line != ""):
    print(line)
    line = f.readlines()
    break
f.close()