# Create a list with a missing number 1 - 100
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

print(answer)
