#                  =============================|     Rohit Movie ticket center     |======================
#                  ----------------------------------------------------------------------------------------


movies= {
    1:{
        "name":"jawan",
        "time" : "10 : 00 am",
        "seats" : 40,
        "price" : 140
    },
    2:{
        "name":"pathan",
        "time" : "11 : 00 am",
        "seats" : 45,
        "price" : 150
    },
    3:{
        "name":"puspa",
        "time" : "11 : 30 am",
        "seats" : 30,
        "price" : 155
    },
    4:{
        "name":"puspa 2",
        "time" : "10 : 30 am",
        "seats" : 45,
        "price" : 120
    },
    5:{
        "name":"kgf",
        "time" : "12 : 00 am",
        "seats" : 50,
        "price" : 250
    },
    6:{
        "name":"dhurandhar",
        "time" : "9 : 00 am",
        "seats" : 60,
        "price" : 300
    }
}

bookings = []

def show_movies():
    print("=== Available names ===")
    for movie_id,movie in movies.items():
        print(f"    {movie_id} : {movie['name']}")
        print(f"    time : {movie['time']}")
        print(f"    available seats : {movie['seats']}")
        print(f"    price : {movie['price']}")
    


def book_ticket():
    show_movies()
    movie_choice = int(input("enter movie number : "))
    if movie_choice not in movies:
        print("invalid choice .....")
        return
    movie = movies[movie_choice]
    ticket = int(input("enter total number of tickets : "))
    if ticket <=0:
        print("invalid choice .....")
        return
    if ticket > movie['seats']:
        print("seat is not enough for your booking ....")
        return

    ticket_price = ticket * movie['price']
    name = input("enter your name : ")
    movie['seats'] -= ticket

    booking = {
        "name" : name,
        "movie" : movie['name'],
        "time" : movie['time'],
        "tickets" : ticket,
        "ticket-price" : ticket_price 
    }  

    bookings.append(booking)

    print("ticket booked successfully ---")
    print(f"    name : {name}")
    print(f"    movie : {movie['name']}")
    print(f"    time : {movie['time']}")  
    print(f"    tickets : {ticket}")
    print(f"    ticket price : {ticket_price}")


def view_bookings():
    if len(bookings) == 0:
        print("no bookings yet ......")
        return
    print("Booking history ----")
    for i,booking in enumerate(bookings,start=1):
        print(f"booking : {i}")
        print(f"         name : {booking['name']}")
        print(f"         movie : {booking['movie']}")
        print(f"         time : {booking['time']}")  
        print(f"         tickets : {booking['tickets']}")
        print(f"         ticket price : {booking['ticket-price']}")


while True:
    print("welcome our online ticket booking platform ...")
    print("1. show available movies ")
    print("2. book tickets")
    print("3. show booking")
    print("4. exit")
    try:
        choice = int(input("enter your choice : "))
    except ValueError:
        print("Please enter only numbers 1 to 4.")
        continue
    if choice == 1:
        show_movies()
    elif choice == 2:
        book_ticket()
    elif choice == 3:
        view_bookings()
    elif choice == 4:
        print("thanks for visiting our online system ...")
        break
    else:
        print("invalid choice ....")




# try:
#     i = int(input("enter: "))
#     print(i)
# except KeyboardInterrupt:
#     print("\nProgram stopped by Ctrl + C")
# except ValueError:
    # print("Please enter a number only")