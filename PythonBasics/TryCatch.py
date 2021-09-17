try:
    with open('test.txt', "r") as reader:
        reader.readlines()
except Exception as e:  # equivalent to catch in other language
    # print("try is fail in execution")
    print(e)

finally:
    print("This is always triggered")
