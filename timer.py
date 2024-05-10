import time
seconds=int(input("enter time in number of seconds"))
def countdown_timer(seconds):
    while seconds>0:
        minute=int(seconds/60)
        s=int(seconds%60)
        timer=f'{minute}:{s}'
        print(timer)
        time.sleep(1)
        seconds-=1
    print('timeup')
    
countdown_timer(seconds)