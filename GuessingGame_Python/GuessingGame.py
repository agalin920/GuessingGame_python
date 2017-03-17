import random

number = random.randint(1,100);
guess = "";
name = input("Hello!, What is your name?");
tryNum=0;

print("Lets play a game "+ name + " :)");
print("I am thinking of a number between 1 and 100. Can you guess what it is? ");

while True : 
	while True:
		#Value Error Detection
		try:
			guess = int(input("What's your guess?"));
			break
		except ValueError:
			print("Oops! That was not a valid guess, Try again...");
	tryNum+=1;		
		

	if(guess==number):
		print("Wow, you got it on try number "+str(tryNum)+" you're good at this");
		break;
	else:
		print("Thats not it :(. Keep trying your only on try number "+str(tryNum)+" good luck!");

	


