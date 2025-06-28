class Start_cinema:
    def __init__(self):
        self.hall_list = []
    @classmethod
    def entry_hall(self, hall):
        self.hall_list.append(hall)
        
        
class Hall(Start_cinema):
    def __init__(self,row,col,hall_no):
        super().entry_hall(hall_no)
        self.row = row
        self.col = col
        self.hall_no = hall_no
        # self.seats = [['O' for _ in range(col)] for _ in range(row)]
        self.seats =[]
        self.show_list= []
    def entry_show(self,id,movie_name,show_time):
        self.show_list.append((id,movie_name,show_time))
    def entry_seat(self):
        self.seats = [['O' for _ in range(self.col)] for _ in range(self.row)]

rupkatha_hall = Hall(10, 10, 1)
rupkatha_hall.entry_seat()
rupkatha_hall.entry_show(1, "Movie A", "10:00 AM")
rupkatha_hall.entry_show(2, "Movie B", "12:00 PM")
Start_cinema.entry_hall(rupkatha_hall)
    
   
    
    
    
    