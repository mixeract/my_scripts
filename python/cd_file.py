my_list = [i**2 for i in range(1,11)]

my_file = open("temp/output.txt", "r+")

# Add your code below!
for i in my_list:
    my_file.write(str(i)+'\n')

my_file.close()