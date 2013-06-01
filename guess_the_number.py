import random

name = raw_input('Hi, please enter your name: ')
number = random.randint(1, 100)
guess_number = 0

while guess_number < 8:
	guess = int(raw_input('Please enter your guess: '));
	guess_number += 1
	
	print 'Your guess is {0}'.format(guess)

	if guess > number:
		print 'Your number is too big'
	elif guess < number:
		print 'Your number is too small'
	elif guess == number:
		print 'Congrats, {0}!'.format(name)
		print 'You find {0} in {1} moves. Good game'.format(number, guess_number)
		break

if guess != number:
	print 'Too bad, you didn`t made it'

# end program 
