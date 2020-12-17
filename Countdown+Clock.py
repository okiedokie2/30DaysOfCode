import time

#create a clock
now = time.ctime()
print (now)

# define the countdown function
def countdown(t):
    while t:
        mins, secs = divmod(t, 60) #if the number is over 60 seconds it becomes a min
        timer = '{:02d}:{:02d}'.format(mins, secs) #02d formats an integer (d) to a field of minimum width 2
        print(timer, end="\r") #Used as a new line character
        time.sleep(1) #make the code wait for one sec.
        t -= 1 #Counts down to zero from t

    print('Lift Off!!')


# input time in seconds
t = input("Enter the time in seconds: ")

# function call
countdown(int(t))