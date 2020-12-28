import math
import random
import shlex

def check_argument(args):
    if (len(args)>0) and (args[0].isdigit() == True) and (int(args[0]) > 0):
        return int(args[0])
    else:
        return -1

### place your code below this line ###

str_menu = '''
Dice Simulation Commands

1) Dice number from (2 to 5) for simulation, i.e., Dice 5
2) Confirm number of dice used in simulation, i.e., Confirm  
3) Roll simulation dice a number of times, i.e., Roll 10
4) Report the simulation results, i.e., Report
5) Help menu, i.e., Help
6) Quit menu, i.e., Quit

Enter command (Dice N, Confirm, Roll N, Report, Help, Quit) below:'''

print(str_menu)

### place your code above this line ###

while True:
    try:
        cmd, *args = shlex.split(input('> '))
        if len(args) == 0:
            args = []
    except ValueError:
        cmd = -1
        
    console_argument = check_argument(args)

    ### place your code below this line ###
    
    if cmd.lower() == 'Dice'.lower():
        if (console_argument > 1):
            if (console_argument < 6):
                x = console_argument
                print('You have selected', x, 'dice.')
            else:
                print('Error: You must input an integer from 2 to 5, i.e. Dice 4.')
        else:
            print('Error: You must input an integer from 2 to 5, i.e. Dice 4.')
            
    elif cmd.lower() == 'Confirm'.lower():
        print('You are currently playing with', x, 'dice.')
 
    elif cmd.lower() == 'Roll'.lower():
        if (console_argument > 0):
            report = []
            for i in range(console_argument):
                dice_numbers = []
                for j in range(x):
                    dice_numbers.append(random.randint(1,6))
                total = sum(dice_numbers)
                run = i + 1
                report.append([run, total, dice_numbers])
            print('Rolling completed', console_argument, 'simulations.')
        else:
            print('Error: You must input a positive integer number of simulations. (i.e. Roll 10)')
                
        
    elif cmd.lower() == 'Report'.lower():
        for i in range(len(report)):
            print('run:', report[i][0], '; sum:', report[i][1], '; dice numbers', report[i][2])

    elif cmd.lower() == 'Help'.lower():
        print(str_menu)
    
    elif cmd.lower() == 'Quit'.lower():
        print('Thank you for using the Dice Simulation Commands. Have a wonderful day.')
        break

    else:
        print('Error: You entered an unknown command:', cmd) 

    ### place your code above this line ###


