file = open("byron.txt", mode="r")

# text = file.read()
# text = file.readlines()
# text = file.readline()



# print(text)


file.close()


file2 = open("new_file.txt", mode="w", encoding="utf-8")

# file2.write('Я первая строка\n')
# file2.write('Я вторая строка')
# lines = [f'{i} строка\n' for i in range(1, 11)]
# file2.writelines(lines)
#
#
#
# file2.close()

# img = open("photo_2023-10-02_17-12-50.jpg", mode="rb")
# content = img.read()
# print(content)
# img.close()

with open("photo_2023-10-02_17-12-50.jpg", mode = "rb") as img:
    content = img.read()
    for i in range(10):
        new_img = open(f'{i}.jpg', mode = "wb")
        new_img.write(content)
        new_img.close()




print(img.closed)


















