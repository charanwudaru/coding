def reverse (string):
    
    reversed_string = ""

    for i in string:
        
        reversed_string = i+reversed_string
    print ("reversed string is:", reversed_string)
    
string = input("enter")
reverse(string)

# am = input()
# reveram=am[::-1]
# print(reveram)










input_string = "Hello, World!"

reversed_string = ""
index = len(input_string) - 1

while index >= 0:
    reversed_string = reversed_string+input_string[index]
    index =index-1

print(reversed_string)


# ##reversing string with two pointers
# input_string = "Hello, World!"
# string_list = list(input_string)

# left = 0
# right = len(string_list) - 1

# while left < right:
#     string_list[left], string_list[right] = string_list[right], string_list[left]
#     left += 1
#     right -= 1

# reversed_string = ''.join(string_list)
# print(reversed_string)
