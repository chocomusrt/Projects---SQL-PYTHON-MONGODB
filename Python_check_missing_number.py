# Method 1 - Create a list with a missing number 1 - 100
# Using summationg of two sets
########################################################
check_list = []
for i in range(1,100):
	check_list.append(i)
print(check_list)

#Create a list from 1 - 100
full_list = []
for n in range(1,101):
	full_list.append(n)
print(full_list)

## compare the list and print the missing value
answer = sum(full_list) - sum(check_list)

print('The missing number is : ' + str(answer))


# Method 2 for loop and if statement
#######################################################
difference = [i for i in check_list + full_list if i not in check_list or i not in full_list]
print(difference)
        
