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
    
