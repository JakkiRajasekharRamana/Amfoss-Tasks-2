import random
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program')
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if(toss==1):
    toss='heads'
else:
    toss='tails'
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    logging.debug(str(toss)+' same as '+str(guess))
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
logging.debug('End of program')