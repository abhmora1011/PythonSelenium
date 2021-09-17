file = open('test.txt')

# READ ALL CONTENTS OF FILE

#print(file.read())
#print(file.read(5)) # Read specific character

#print(file.readline())

# Print line by line using readline method

'''line = file.readline()
while line != "":
    print(line)
    line = file.readline()'''

for line in file.readlines():
    print(line)


file.close()

