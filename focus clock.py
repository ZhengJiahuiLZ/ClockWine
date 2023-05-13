import time
import os


def count_down(minutes):
    seconds = minutes * 60
    while seconds > 0:
        min, sec = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(min, sec)
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1


def ring_bell():
    for i in range(3):
        os.system('afplay /System/Library/Sounds/Glass.aiff')  # MacOS
        time.sleep(1)


if __name__ == '__main__':
    print('Set your work time in minutes (Default: 25 minutes):')
    work_time = input() or '25'
    print(f'Starting {work_time} minutes focus timer...')
    count_down(int(work_time))
    ring_bell()
    print('Time to take a break!')
