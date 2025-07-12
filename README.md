# Random-Number-Guessing-Game
1. The game begins by generating a random number between 1 and 100 using the generate_random_number(min_num, max_num) function.

2. A loop is used to repeatedly prompt the user to guess the number until they guess correctly.

3. For each guess:
   - The user's input is converted to an integer.
   - The number of attempts is tracked and incremented.
   - The guess is passed to check_guess(random_num, user_guess), which returns True if it matches the target number.

4. If the guess is incorrect:
   - A hint is printed telling the user to guess higher or lower.
   - After exactly 2 incorrect attempts, an additional hint is given. The hint is chosen randomly from:
     • Whether the number is even or odd.
     • Whether it is a multiple of 5.
     • Whether its square is greater, less than, or equal to 1000.

5. Once the guess is correct, the program displays the number of attempts taken.

6. The game then asks the user if they would like to try again.

7. The user responds with Yes or No. 

8. If yes, the game starts over again (step 1). If no, the console prints "Alright, see you next time!" and the application ends. 


The following functions were utilized in this application:

1. generate_random_number(min_num, max_num):
   • Returns a random integer in the range [min_num, max_num].

2. check_guess(random_num, user_guess):
   • Returns True if the guess is correct, otherwise False.

3. get_additional_hint(random_num):
   • Randomly selects and returns one of three possible hints to help the player.

*The program handles invalid inputs (e.g., letters or special characters) using a try-except block to avoid crashing.

 
