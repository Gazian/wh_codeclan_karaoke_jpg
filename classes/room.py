from classes.guest import Guest
from classes.song import Song
class Room:
    def __init__(self,name,entry_fee,capacity_limit):
        self.name = name
        self.entry_fee = entry_fee
        self.guest_list = []
        self.songs = []
        self.capacity_limit = capacity_limit

    def room_guest_list_count(self):
        return len(self.guest_list)

    def check_in_guest(self,guest_to_check_in): 
        self.guest_list.append(guest_to_check_in)

    def check_out_guest(self,guest_to_check_out):
        self.guest_list.remove(guest_to_check_out)
        

    def clear_guest_list(self):
        self.guest_list.clear()

    def clear_song_list_all(self):
        self.songs.clear()

    def room_song_count(self):
        return len(self.songs)

    def add_song(self,song_to_add):
        self.songs.append(song_to_add)

    def print_guest_list(self):
        for guest in self.guest_list: print (guest.name,guest.money,guest.fave_song)

    def print_song_list(self):
        for song in self.songs: print (song.song_title,song.artist,song.genre)

    def room_capacity_limit_reached(self,room):
        if len(self.guest_list) <= room.capacity_limit: print(f"Welcome to the {self.name} karaoke room!") 
        else: self.guest_list.pop() and print(f"Sorry, the {self.name} karaoke room is at maximum capacity")  

    def take_entry_fee(self,room):
        for guest in self.guest_list:
            guest.money -= room.entry_fee


        
        # else:
        #     self.guest_list.pop()
        #     print (f"Sorry {self.name} karaoke room is at full capacity")  

    

    
