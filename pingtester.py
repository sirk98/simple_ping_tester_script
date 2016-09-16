"""Simple Network Tester
"""

import os
import socket
import subprocess
import termcolor

default_host = 'ping.ggrapes.uk'

try:
    print (termcolor.colored(
        "Script Started",
        'red',attrs=['bold']
        ))

    ip = input(termcolor.colored(
        'Insert IP Address To Ping Or Live Blank To Use Default IP : ', 
        'red',attrs=['bold']
        ))

    if not ip == '':
        socket.gethostbyname(ip)
        print (termcolor.colored(
            "Host Found",
            'blue',attrs=['bold']
            ))

    
    else:
        ip = socket.gethostbyname(default_host)
        print (termcolor.colored(
            "Default IP Was Used",
            'blue',attrs=['bold']
            ))

        print (ip)

    x = subprocess.call([
        "ping", "-c 10", "-t 10", "{}".format(ip)
        ])

except KeyboardInterrupt:
    print("\n")
    exit(0)

finally:
    print (termcolor.colored(
        "Finish!",
        'green', attrs=['bold']
        ))