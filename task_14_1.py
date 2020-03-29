from datetime import datetime
import argparse
import functions as fun

parser = argparse.ArgumentParser(description="Timer")
parser.add_argument('Name')
parser.add_argument('Surname')
parser.add_argument('hours', type=int)
parser.add_argument('minutes', type=int)
parser.add_argument('seconds', type=int)
args = parser.parse_args()
with open('timer log-file.txt', 'a') as log_file:
    log_file.write(f'Name: {args.Name}, '
                   f'Surname: {args.Surname}, '
                   f'Timer: {args.hours}:{args.minutes}:{args.seconds}, '
                   f'Date: {datetime.now()}\n')
try:
    timer = datetime.strptime(f'{args.hours}:{args.minutes}:{args.seconds}', '%H:%M:%S')
except ValueError:
    args.hours, args.minutes, args.seconds = fun.convert(args.hours, args.minutes, args.seconds)
    timer = datetime.strptime(f'{args.hours}:{args.minutes}:{args.seconds}', '%H:%M:%S')
generator = fun.countdown(timer)
try:
    for i in generator:
        print(i.time())
    print('Alarm!')
except KeyboardInterrupt:
    print('Stopping the timer.')
