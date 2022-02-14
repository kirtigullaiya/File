my_file=open("kirti","r")
# print(my_file.read(5))
count=0
for i in my_file:
    for j in i:
        count+=1
        print(count)
my_file.close()