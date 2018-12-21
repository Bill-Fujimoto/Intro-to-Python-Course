#We've given you a class called "Song" that represents
#some basic information about a song. We also wrote a 
#class called "Artist" which contains some basic 
#information about an artist. Your job is to do the
#following:
#
# 1. Create a song object with the following attributes:
#       name = "You Belong With Me"
#       album = "Fearless"
#       year = 2008
#       artist.name = "Taylor Swift"
#       artist.label = "Big Machine Records, LLC"
# Store this song object in a variable named "song_1"
# Hint: You'll first need to make an Artist object
#
# 2. Create another song object with the following 
#    attributes:
#       name = "All Too Well"
#       album = "Red"
#       year = 2012
#       artist = the same artist instance as song_1
# Store this song object in a variable named "song_2"
#
# 3. Finally, create another song object with the following
#    attributes:
#       name = "Up We Go"
#       album = "Midnight Machines"
#       year = 2016
#       artist.name = "LIGHTS"
#       artist.label = "Warner Bros. Records Inc."
# Store this song object in a variable named "song_3"
#
#When your code is done running, there should exist three
#variables: song_1, song_2, and song_3, according to the
#requirements above.

class Artist:
    def __init__(self, name, label):
        self.name = name
        self.label = label

class Song:
    def __init__(self, name, album, year, artist):
        self.name = name
        self.album = album
        self.year = year
        self.artist = artist
        

#Write your code here!
artist_taylor = Artist("Taylor Swift","Big Machine Records, LLC")
artist_lights = Artist("LIGHTS","Warner Bros. Records Inc.")
song_1=Song("You Belong With Me", "Fearless",2008, artist_taylor)
song_2=Song("All Too Well", "Red", 2012, artist_taylor)
song_3=Song("Up We Go","Midnight Machines",2016,artist_lights)

print("Song: "+song_1.name+"\nAlbum: "+song_1.album +"\nArtist: "+song_1.artist.name+ "\nLabel: " +song_1.artist.label+"\n")
print("Song: "+song_3.name+"\nAlbum: "+song_3.album +"\nArtist: "+song_3.artist.name+ "\nLabel: " +song_3.artist.label+"\n")
