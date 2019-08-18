age = input("Enter your age: ")
# printYou have lived for '+str(int(age)*365*24*60*60)+' seconds. '+str(age)+" Years.")
# print("You have lived for {} seconds".format(str(int(age)*365*24*60*60)))
print("You have lived for {} seconds. This corresponds to {} years".format(int(age)*365*24*60*60, age))
