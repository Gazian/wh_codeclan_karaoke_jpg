class Room:
    def __init__(self,name,entry_fee):
        self.name = name
        self.entry_fee = entry_fee
        self.guest_list = []
        self.songs = []

    def room_guest_list_count(self):
        return len(self.guest_list)

    def check_in_guest(self,guest_to_check_in):
        self.guest_list.append(guest_to_check_in)

    def check_out_guest(self,guest_to_check_out):
        self.guest_list.remove(guest_to_check_out)

    def room_song_count(self):
        return len(self.songs)

    def add_song(self,song_to_add):
        self.songs.append(song_to_add)
    
