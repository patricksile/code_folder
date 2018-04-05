#Project: Take a music break

"""
Do you know a friend who works too many hours? We will write a program that schedules breaks throughout the day -- reminding your friend to listen to his favorite music in the web browser, get up and dance to it or just walk away from the computer if he wants to, then go back to work when his favorite music finishes to play.

NB: 
We will assume that his day is 8 hours long and that he can have 4 breaks of music time (of 5 minutes 42 seconds which is the duration of his favorite music).

"""


# My Solution:

import time
import webbrowser

def music_break_time(music_link):
	
	count = 0	# initialize the count at 0
	
	while count < 4: # loop 4 times
	  
		time.sleep(10) # Wait for 10 seconds (time delay or working time)
	 
		webbrowser.open(music_link) # open the music link in a web browser

		count += 1 #incrementation of count by 1


music_link = "https://www.youtube.com/watch?v=DXDGE_lRI0E" # music link
music_break_time(music_link) # calling music_break_time function


"""
I think the problem description is clear, but not having some key informations which might be relevant. like how many hours he works a day, how many time he should take a break and how long and which process he use to play the music.
"""

"""
My version Instructions:

Do you have a friend who works too many hours?
Write a program that will schedule breaks throughout the day(we will assume that a day is 8 hours) of your friend at work, reminding your friend that he can take break(s)(nb_of_break) of a certain duration(break_duration in minute), by listening to music on a website (link) and dancing too if he wish too.
If the number of break and the duration of breaks are more that the time he can be at work (8 hours) return None.


Format of the function:
breakTime(friend_name, nb_of_break, break_duration, link) => "My friend took (nb_of_break) break(s) of (break_duration) minutes and played music from: (link) today."

Examples:

break_time('Patrick', 2,30,"www.deezer.com/charlotte_dipanda-longue=DXXXEW") => "Patrick took 2 break(s) of 30 minutes and played music from: www.deezer.com/charlotte_dipanda-longue=DXXXEW today."
"""