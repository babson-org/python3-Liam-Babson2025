#%%
# print 'hello' 5 times using an arithmetic operator

print("hello " *5)

#%%
# print 'hello' 5 times using a loop
for i in range(5):
    print("hello")
#%%
# print 'hello' 5 times on the same line using a loop
txt = "hello "
for i in range(5):
    txt += "hello "
print(txt)

#%%
for i in range(3):
    for j in range(3):
        print(f"{i}{j}", end=" ")
    print()

''' using nested loops print the following:

00 01 02
10 11 12
20 21 22

'''
#%%
# define txt and input some text from the keyboard into it
txt = input("Enter Name: ")
print(txt)

#%%
# print each letter in txt 
txt = input("Enter Name: ")
for i in range(len(txt)):
    print(txt[i])
#%%
# assign the variable letter to the first letter in txt
txt = input("Enter Name: ")
letter = txt[0]
print(letter)
#%%
# print out all the letters in txt that are equal to the first letter
txt = input("Enter Name: ")
letter = txt[0]
for first in txt:
    if first == letter:
      print(first)


'''
say txt = 'the cat in the hat was read today'
't' is the first letter

result: tttt
'''

#%%
myList = ['apple', 'orange', 'pear', 'blueberry', 'peach']
length = len(myList)
Shifted_list = [None] * length
for i, element in enumerate(myList):
    new_position = (i +3) % length
    Shifted_list[new_position] = element
print(Shifted_list)



'''
# suppose we had a list of n elements. create a new list that
  shifts the elements by 3

      myList = ['apple', 'orange', 'pear', 'blueberry', 'peach']
            shifted_list = ['pear', 'blueberry', 'peach', 'apple', 'orange']

                    Hints:
                                 1) use len(), %, enumerate
                                                   2) also assign shifted_list = [None] * length  (you'll need to determine 
                                                                             the length variable)
                                                                                                            3) shift inside the for loop
                                                                                                                                                4) print out the printed list outside the for loop
                                                                                                                                                                                    '''



                                    # %%
                                    