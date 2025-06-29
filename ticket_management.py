class Start_cinema:
    # def __init__(self):
    hall_list = []
    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)
        
        
class Hall(Start_cinema):
    def __init__(self,row,col,hall_no):
        Start_cinema.entry_hall(self)
        self.row = row
        self.col = col
        self.hall_no = hall_no
        # self.seats = [['O' for _ in range(col)] for _ in range(row)]
        self.seats =[]
        self.show_list= []
    def entry_show(self,id,movie_name,show_time):
        self.show_list.append((id,movie_name,show_time))
    def entry_seat(self):
        self.seats = [['0' for _ in range(self.col)]  for _ in range(self.row)]
    def book_seats(self,id,c,r):
        found = False
        for show in self.show_list:
            s_id,name,time=show
            if s_id == id:
                found = True
                if self.seats[c-1][r-1] == '0':
                    self.seats[c-1][r-1] = '1'
                    print(f"Seat at row {c}, column {r} booked for show {name}.")
                    break
                else:
                    print(f"Seat at row {c}, column {r} is already booked.")
                break
        if not found:
            print(f"Show ID {id} not found.")
                
    def view_shows(self):
        return self.show_list     
    def view_available_seats(self,id):
        if id not in self.seats:
            print(f"Show ID {id} not found.")
        avable_seats = []
        for i in range(self.row):
            for j in range(self.col):
                if self.seats[i][j] == '0':
                    avable_seats.append((i+1, j+1))
        return avable_seats     

rupkatha_hall = Hall(10, 10, 1)
Start_cinema.entry_hall(rupkatha_hall)
rupkatha_hall.entry_seat()
rupkatha_hall.entry_show(1, "Borbad", "10:00 AM")
rupkatha_hall.entry_show(2, "Tofan", "12:00 PM")
rupkatha_hall.entry_show(3, "Thandob", "02:00 PM")
rupkatha_hall.entry_show(4, "Jawan", "01:00 PM")

# for r in rupkatha_hall.seats:
#     print(r)
# print(rupkatha_hall.show_list[0])
# rupkatha_hall.book_seats(4, 1, 2)
# Book seat at row 1, column 1 for show ID 1

# for i in range(len(rupkatha_hall.seats)):
#     for j in range(len(rupkatha_hall.seats[i])):
#         print(rupkatha_hall.seats[0][0], end=' ')
#     print()

# for show in rupkatha_hall.show_list:
#     print(show)
# print(rupkatha_hall.show_list)
# rupkatha_hall.book_seats(4, 1, 2)

# # print("Available seats after booking:",rupkatha_hall.view_available_seats())
# for seats in rupkatha_hall.view_available_seats():
#     print(f"Available seat at row {seats[0]}, column {seats[1]}")
    
while True:
    print("1. View All Shows Today")
    print("2. View Available Seats")
    print("3. Book tickets")
    print("4. Exit")
    choice = input("Enter your option: ")
    if choice == '1':
        print("Available shows:")
        for show in rupkatha_hall.view_shows():
            print(f"Show ID: {show[0]}, Movie Name: {show[1]}, Show Time: {show[2]}")
    elif choice == '2':
        show_id = int(input("Enter show ID to view available seats: "))
        print("Available seats:")
        for seats in rupkatha_hall.view_available_seats(show_id):
            print(f"Row: {seats[0]}, Column: {seats[1]}")
        for seat in rupkatha_hall.seats:
            print(seat)    
    elif choice == '3':
        show_id = int(input("Enter show ID to book: "))
        row = int(input("Enter row number: "))
        col = int(input("Enter column number: "))
        rupkatha_hall.book_seats(show_id, row, col)
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid option. Please try again.")
    
   
    
    
    
    