import subprocess
subprocess.Popen(
    ['/usr/bin/env','bash','-c','python3 telegram_bot.py'],
    stdout=open('bot.log','w'),
    stderr=open('bot.err','w'))
