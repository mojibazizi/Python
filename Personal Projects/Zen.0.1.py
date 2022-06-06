
''' Zen is the first bot Im going to build. through time will improve Zen's knwoledge'''
print('Hello! My name is Zen.')
print('I was created in 2021. By my  Mojib Azizi')
print('Please, remind me your name.')

 #reading a name
your_name = input('name : ')
print('What a great name you have, ' + your_name) 
#lets play a game
game = input('Please type in "Game" if you like to play a game! ')
if game == str("Game"):
    remainder3 = int(input("remainder of your age/3 : "))
    remainder5 = int(input("remainder of your age/5 : "))
    remainder7 = int(input("remainder of your age/7 : "))
    age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    print('Your age is ' + str(age) + "; that's a good time to start programming! ")
else:
    print('What would you like to do ? burnnn?')

##Counting game
print("Now I am going to prove to you my counting abilities!")
number = int(input('What number would you like me to count to ?: '))
to_count = -1
while to_count < number:
    to_count += 1
    
    print(to_count, '!')


##Guessing game 
#Ask the user the question
question = print('Who is the king of the jungle ?')
#prints out few options for the user
options = ["1.Lion", "2.Cheetah", "3.Elephant", "4.Rhino"]
print(options[0])
print(options[1])
print(options[2])
print(options[3])
ans = input()
#the algorithm
correct_ans = '1'
while ans != correct_ans:
    ans = input("Incorrect Please, try again! : ")

if ans == correct_ans :
    print("Congratulations, have a nice day!")

print("I will meet you again", your_name , "till next time Zen!")