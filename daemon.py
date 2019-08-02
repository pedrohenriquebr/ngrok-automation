import subprocess
import sys
import os


def help_print():
    print('{} <start,stop>'.format(sys.argv[0]))
    exit(1)

def main():

    if len(sys.argv) != 2:
        help_print()

    if sys.argv[1] not in ['start','stop']:
        help_print()
    
    option = sys.argv[1]

    if option == 'start':

        p = subprocess.Popen(
            ['/usr/bin/env','bash','-c','python3 telegram_bot.py'],
            stdout=open('bot.log','w'),
            stderr=open('bot.err','w'))
        
        print(p.pid)
        with open('.pid','w') as f:
            f.write(str(p.pid))

    elif option == 'stop':

        with open('.pid','r') as f:
            pid =  int(f.read())
            print(pid)
            os.system('kill {}'.format(pid))

main()