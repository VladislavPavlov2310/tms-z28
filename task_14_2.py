from datetime import datetime
import argparse
import functions as fun

parser = argparse.ArgumentParser(description="Work in focus time, chill in break time, repeat!")
parser.add_argument('Name')
parser.add_argument('Surname')
parser.add_argument('Task')
parser.add_argument('-f', '--focus-time', default=25, type=int, help="Input time to work")
parser.add_argument('-b', '--break_time', default=5, type=int, help="Input time to chill")
parser.add_argument('-c', '--cycle', default=4, type=int, help="Input amount of cycles")
args = parser.parse_args()
with open('pomadora log-file.txt', 'a') as log_file:
    log_file.write(f'Name: {args.Name}, '
                   f'Surname: {args.Surname}, '
                   f'Task: {args.Task}'
                   f'Time: (focus: {args.focus_time} min, break: {args.break_time} min) x {args.cycle}, '
                   f'Date: {datetime.now()}\n')
focus_time = datetime.today().strptime(f'{args.focus_time}', '%M')
break_time = datetime.today().strptime(f'{args.break_time}', '%M')
for i in range(args.cycle):
    print(f'{i + 1} cycle starts: ')
    generator = fun.countdown(focus_time)
    try:
        for j in generator:
            print(j.time())
        print('Ending focus time!')
    except KeyboardInterrupt:
        print('Stopping the timer.')
    generator = fun.countdown(break_time)
    try:
        for j in generator:
            print(j.time())
        print('Ending of break time!')
    except KeyboardInterrupt:
        print('Stopping the timer.')
