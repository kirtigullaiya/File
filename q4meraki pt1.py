file=open("places.txt","r")
for i in file:
    if "delhi" in i:
        a=open("delhi.txt","a")
        a.write(i)
    elif "shimla" in i:
        a=open("shimla.txt","a")
        a.write(i)
    else:
        a=open("other.txt","a")
        a.write(i)
# file.close()
