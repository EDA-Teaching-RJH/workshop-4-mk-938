camel_case = input("Enter a variable in camel case: ")
snake_case = ""
for i in range(0,len(camel_case)):
    if camel_case[i].islower():
        snake_case += (camel_case[i])
    else:
        snake_case += ("_")
        snake_case += (camel_case[i].lower())

print (snake_case)



