import random
print("Welcome player\n")
total_rounds = 0
rounds_won = 0
total_score = 0
play_again = "y"
while play_again.lower() == "y":
    total_rounds += 1
    secret_number = random.randint(1, 100)
    won_round = False
    
    print("I'm thinking of a number between 1 and 100.")
    print("You have 6 attempts to guess it.\n")
    
    for attempt in range(1, 7):
        print(f"Attempt {attempt}/6")
        guess = int(input("Enter your guess: "))
        
        if guess == secret_number:
            print("Congratulations!")
            print("You guessed the number\n")
            
            guesses_remaining = 6 - attempt
            multiplier = guesses_remaining + 1
            points = multiplier
            
            print(f"Guesses remaining: {guesses_remaining}")
            print(f"Multiplier: x{multiplier}")
            print(f"Points earned: {points}\n")
            
            total_score += points
            rounds_won += 1
            won_round = True
            break
        else:
            diff = abs(secret_number - guess)
            if guess < secret_number:
                if diff > 10:
                    print("Too low\n")
                else:
                    print("Higher\n")
            else:
                if diff > 10:
                    print("Too high\n")
                else:
                    print("Lower\n")
    
    if not won_round:
        print(f"Game Over! The secret number was {secret_number}.\n")
        
    print(f"Current Score: {total_score}\n")
    play_again = input("Play another round? (y/n): ")
    print()

print(f"Rounds Played: {total_rounds}")
print(f"Rounds Won: {rounds_won}")
print(f"Final Score: {total_score}")