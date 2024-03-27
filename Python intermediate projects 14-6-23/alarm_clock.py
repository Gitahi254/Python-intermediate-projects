#create an alarm clock timer, make a sound effect with it
# the library we are using is called playsound

from playsound import playsound
import time


#The clear and clear_and return parts are used to clear the terminal and display only the countdown
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        
        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")
        #(:02d) is used to add a digit in front of the ones there so that it can look like a normal timer
    playsound("Alarm-Fast-A1-www.fesliyanstudios.com.mp3")

minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds

alarm(10)