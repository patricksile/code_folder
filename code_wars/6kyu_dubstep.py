# Problem: Dubstep (6kyu)
"""
Polycarpus works as a DJ in the best Berland nightclub, and he often uses dubstep music in his performance. Recently, he has decided to take a couple of old songs and make dubstep remixes from them.

Let's assume that a song consists of some number of words. To make the dubstep remix of this song, Polycarpus inserts a certain number of words "WUB" before the first word of the song (the number may be zero), after the last word (the number may be zero), and between words (at least one between any pair of neighbouring words), and then the boy glues together all the words, including "WUB", in one string and plays the song at the club.

For example, a song with words "I AM X" can transform into a dubstep remix as "WUBWUBIWUBAMWUBWUBX" and cannot transform into "WUBWUBIAMWUBX".

Recently, Jonny has heard Polycarpus's new dubstep track, but since he isn't into modern music, he decided to find out what was the initial song that Polycarpus remixed. Help Jonny restore the original song.

Input

The input consists of a single non-empty string, consisting only of uppercase English letters, the string's length doesn't exceed 200 characters

Output

Return the words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.

Examples

song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
  # =>  WE ARE THE CHAMPIONS MY FRIEND
"""
# My Solution:

def song_decoder(song):
	return " ".join(i for i in song.split('WUB') if i != '')
# Other Solutions:

# Solution 1: By
# Solution: By isbadawi, richlewis42, chriscannon 
def song_decoder(song):
    return " ".join(song.replace('WUB', ' ').split())

# Solution: By rmobis, bbm, staticor, kavag, js572, vnjogani (plus 178 more warriors)

def song_decoder(song):
    import re
    return re.sub('(WUB)+', ' ', song).strip()

# Solution: By pavel.koshev, Kironide

def song_decoder(song):
    return ' '.join([a for a in song.split('WUB') if a])
