import random 
name = "Mojib"
question = "Are we alive?"
answer = ''
random_number = random.randint(1, 12)

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "You can do anything!"
elif random_number == 11:
  answer = "Failure is almost as important as success."
elif random_number == 12:
  answer = "Yesss!!!"
else:
  answer = "Error"
if question == "":
  print("I need a question to answer!")
else:
  print("Magic 8-Ball's answer: ", answer)