#first search_name_1 is better because it doesn't remove the last like the second one (search_name_2)
def search_name_1():
    infile = open("names.txt","r")
    for s in infile:
        print(s)

# prints each line while removing the last character from each line i.e '/n' from 1st to 2nd last line
# but removes age from last line because it does not have a newline character
def search_name_2():
    infile = open("names.txt","r")
    for s in infile:
        print(s[:-1])

search_name_1()
search_name_2()
