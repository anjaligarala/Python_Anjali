import random

random_input = random.randint(1, 20)
print(random_input)
is_correct = False

while True:
    for num_retry in range(3):
        user_input = int(input("Enter the number for guessing - "))
        if user_input == random_input:
            is_correct = True
            print("Entered number is correct on " + str(num_retry + 1) + " try")
            break
        elif user_input > random_input:
            print("Your input is greater than guessing number")
        else:
            print("Your input is smaller than guessing number")

    if is_correct is False:
        print("All your attempt was wrong")

    play_again = input("Do you want to play again, enter yes or no")
    if play_again == "yes":
        continue
    else:
        break
