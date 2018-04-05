import time
import webbrowser
 
def music_break_time():
 
    # initialize the count at 0
    count = 0
    
    # loop 4 times
    while count < 4:
      
         # Wait for 10 seconds (time delay or working time)
        time.sleep(10)
    
         # open the music link in a web browser
        webbrowser.open("https://www.youtube.com/watch?v=DXDGE_lRI0E")
 
        #incrementation of count by 1
        count += 1
 
 
# calling music_break_time function
music_break_time()