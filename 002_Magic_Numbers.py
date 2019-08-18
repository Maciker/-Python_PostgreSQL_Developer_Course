import random

magic_numbers = [random.randint(0,9),random.randint(0,9)]

def ask_user_and_check_number():
    user_number = int(input("Enter a number between 0 and 9: "))
    if user_number in magic_numbers:
        #print("You got the number right!")
        return"You got the number right!"
    if user_number not in magic_numbers:
        #print("You got the number wrong!")
        return "You got the number wrong!"

def run_program_x_times(chances):
    for attempt in range(chances): #range(chances) is [0,1,2]
        print("This is attempt {}".format(attempt + 1))
        message = ask_user_and_check_number()
        print(message)

        
times = int(input("How many chances do you want?"))
run_program_x_times(times)

# why not us a do... while?


# min =10
#for index in range(10):
#    random_number = random.randint(0,100)
#   print("The random number is {}".format(random_number))
#    if random_number < min:
#    	min = random_number 
