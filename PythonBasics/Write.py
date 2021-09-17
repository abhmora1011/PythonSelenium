with open('test.txt', 'r') as reader:  # with open('test.txt','w') as writer: (WRITE MODE)
    content = reader.readlines()
    reversed(content)
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
