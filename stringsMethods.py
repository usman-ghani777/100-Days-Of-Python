# strings are immutable
a = "usman"

print(len(a)) # Finding the length of the strings

print(a.upper()) # upper is a function use to convert string to upper case

b = "USMAN"
print(b.lower()) # lower function is to convert the string into lower case

c = "!!!Hi usman!!!!!!!!!!!!!!!"

print(c.rstrip("!")) # rtrip function remove the ending marks does not remove starting marks

print(a.replace("usman","khan")) # replace function will replace the string by other which you are enters

d = "hi usman how are you"
print(d.split(" "))#split function will make a list of string which are separable by space

blogheading = "introductiOn to PytHon"

print(blogheading.capitalize()) # captalize function convert  the stings to correct the form

friend = "how are you bro"

print(len(friend.center(20))) # move text into center
print(len(friend))

count = "usman khan, usman ghani"
print(count.count("usman")) # usman is two times in strings the count function will prints 2 

x = "usmanGhani!"
print(x.endswith("!")) #endswith function prints Ture if the stings are ends with given mark"!"
                        # other wise false
        
y = "HeyDanWhatAreYouDoing"

print(y.find("dan"))# find function prints 4 becouse dan is starting from forth string 
                    # other wise it returns -1

print(y.isalnum()) # if string contains alpha numeric values its prints true
                    #other wise it returns false

z = "hiIamusman"

print(z.isalpha()) # its print ture if and only if string conatains aphabets upper lower both can
                    # other wise it returns false

print(z.islower())# if all stings are in lower case prints true otherwise false    

k = "wish you best \n luck"
print(k.isprintable())   # black sklash n is not printable so gives false
print(k)

g= "        "
print(g.isspace()) # contains spaces prints true

i = "!! usman"
print(i.startswith("!")) # prints ture

print(i.swapcase())# convert upper to lower and lower to upper case in given stings

j = "my name is khan"
print(j.title()) # convert first character of each string into uppercase



