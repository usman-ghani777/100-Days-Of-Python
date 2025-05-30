name = "Usman"
Friend = "Khan"
print("Hello "+name)

apple = "He said,  \"I wants to eat an Apple" # without forward sclash its gives an Error 
                                            # becouse of double quotes re use in middle
print(apple)


banana = 'He said," I wants to eat banana'# No error in single quotes

print(banana)

# to handle multiple lines we use tripple quotes for this purpose

st = '''"This is multi line string" hi my name is usman i am from peshwer, i am studying
computer science from uet jallozai'''
print(st)

# indexing in strings

index = "usman"

print(index[0]) # indexing will starts from 0
print(index[1])
print(index[2])
print(index[3])
print(index[4])
#pirnt(index[5]) this through an error 

print("Lets use a for loop")

for i in index:
    print(i) # this will print same as indexing