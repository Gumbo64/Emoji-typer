import pyautogui
import time

input = input('what would you like to emoji type?')
time.sleep(5)
counter = 0
typelist = []
for letter in input:
     counter = counter + 1
     if counter != 90:
          if letter == " " or letter == "," or letter == '.' or letter == '(' or letter == ')' or letter == '-':
               typelist.append(letter)
               counter = counter + 1
          else:
               typelist.append(':regional_indicator_{}:'.format(letter))
               counter = counter + 1
     else:
          typelist.append('enter')
          counter = 0
     typelist.append(' ')
for letter in typelist:
     if letter == 'enter':
          time.sleep(5)
     else:
          pyautogui.typewrite(letter)
     time.sleep(0.1)
     
