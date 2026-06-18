# =====  N1 RAILWAY SIMULATION =====


import datetime

trains = { "12301": {"name": "Kolkata Express", "source": "Kolkata", "dest": "Howrah", "seats": 50, "fare": 150}, "12302": {"name": "Darjeeling Mail", "source": "Kolkata", "dest": "darjeeling", "seats": 40, "fare": 450}, "22311": {"name": "Local Passenger", "source": "Howrah", "dest": "Burdwan", "seats": 30, "fare": 60}, }


bookings = {}
pnr_counter = 1000

def list_trains():
    print("\nAvailable trains:\n")
    print("{:<8} {:<20} {:<12} {:<12} {:<8} {:<8}".format("trainno","name","source","dest","seats","fare"))
    for tn,info in trains.items():
        print("{:<8} {:<20} {:<12} {:<12} {:<8} {:<8}".format(tn,info["name"],info["source"],info["dest"],info["seats"],info["fare"]))



def search_trains():
    found = False
    src = input("enter source : ")
    dst = input("enter dest : ")
    print("\nsearch results:\n")
    for tn,info in trains.items():
        if info["source"].lower() == src.lower() and info["dest"] == dst.lower():
            print(f"{tn}: {info['name']} ({info['seats']} seats ,fare : {info['fare']})")
            found = True
    if not found:
        print("no trains ound for that route...")


def book_ticket():
    global pnr_counter
    list_trains()
    train_no = input("enter train no to book : ").strip()
    if train_no not in trains:
        print("invalid train no please enter train no as per the trai list..")
        return
    try:
        seats = int(input("enter no of seats to book : "))
    except ValueError:
        print("invali input....")
        return
    if seats <= 0 or seats > trains[train_no]["seats"]:
        print("not enoug seats available")
        return
    name = input("enter passenger name : ")
    age = input("enter age : ")
    gender = input("passenger gender(M/F/O) : ")
    total_fee = trains[train_no]["fare"] * seats
    trains[train_no]["seats"] -= seats
    pnr_counter += 1
    pnr = f"RAIL{pnr_counter}"
    bookings[pnr] = {
        "train_no":train_no,
        "name":name,
        "age":age,
        "gender":gender,
        "seats":seats,
        "fare":total_fee,
        "time":datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    }
    print(f"\nbooking successful ! PNR : {pnr}")
    print(f"train : {train_no} -> {trains[train_no]['name']}")
    print(f"seats : {seats} | total fee : {total_fee}")


def view_booking():
    pnr = input("enter pnr to view booking : ").strip()
    if pnr not in bookings:
        print("PNR not found...")
        return
    rec = bookings[pnr]
    print("\nbook deatials -->> \n")
    for key,val in rec.items():
        print(f"{key.capitalize()}:{val}")


def calcel_ticket():
    pnr = input("enter PNR to calcel booking : ")
    if pnr not in bookings:
        print("PNR not found ...")
        return
    train_no = bookings[pnr]['train_no']
    seats = bookings[pnr]['seats']
    trains[train_no]["seats"] += seats
    del bookings[pnr]
    print(f"\n Booking {pnr} cancelled successfully . {seats} seats(s) realeased..")


def view_all_bookings():
    if not bookings:
        print("no bookins found ....")
        return
    print("\n all bookings :\n")
    for pnr,rec in bookings.items():
        print(f"{pnr} -> {rec['name']} | Train {rec['train_no']} | seats : {rec['seats']} | Fare : {rec['fare']}")


while True:
    print("\n----- N1 RAILWAY SIMULATION -----")
    print("1. LIst trains")
    print("2. search trains")
    print("3. book trains")
    print("4. view booking")
    print("5. calcel ticket")
    print("6. view all bookings")
    print("7. Exit")
    choice = int(input("enter our choice : "))
    if choice == 1:
        list_trains()
    elif choice == 2:
        search_trains()
    elif choice == 3:
        book_ticket()
    elif choice == 4:
        view_booking()
    elif choice == 5:
        calcel_ticket()
    elif choice == 6:
        view_all_bookings()
    elif choice == 7:
        print("THANK YOU FOR VISITING N1 RAILWAY SIMULATION .....")
        break
    else:
        print("invalid choice please try again...")




