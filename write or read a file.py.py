s="saad is a good boy"

# Writing to a file
fp=open("test.txt", "w")
fp.write(s)
fp.close()

# Reading to a file

with open("saad.txt", "r") as f:

    s = f.read()
    print(s)

