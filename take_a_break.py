# This program is meant for people who constantly have work on computer.
# After running this program, user will get a video running in browser after every hour.

import time
import webbrowser

counter = 0
while counter <= 24:
    # print("It's time to take a break!!!", time.ctime())
    webbrowser.open_new("https://youtu.be/ac7xsFCzvxw")
    time.sleep(1*60*60)
counter += 1
