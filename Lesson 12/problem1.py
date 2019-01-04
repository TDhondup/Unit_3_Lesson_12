import time
import random

print('*'*65)
print('Hullo, hullo. I am Magic Eight Ball. Ask me anything!')
print()

question = input('What would you like to know? ')
time.sleep(0.7)
print('Shaking!')
time.sleep(0.7)
print("I'm thinking...")
time.sleep(0.7)
print("I'm still thinking...")
time.sleep(0.7)

choice = random.randint(1,6)

if choice == 1:
	print('Why are you asking me?')

elif choice == 2:
	print('Just google it.')

elif choice == 3:
	print('No u.')

elif choice == 4:
	print("I don't know, figure it out yourself.")

elif choice == 5:
	print("Eh, maybe. Don't ask me, I don't know everything.")

else:
	print('Ye.')

print('-'*65)

