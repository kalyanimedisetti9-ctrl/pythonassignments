class Room:
    def __init__(self, room_no, room_type, price):
        self.room_no = room_no
        self.room_type = room_type
        self.price = price
        self.booked = False


class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Booking:
    def __init__(self, customer, room):
        self.customer = customer
        self.room = room
        self.room.booked = True

    def display(self):
        print("Customer:", self.customer.name)
        print("Phone:", self.customer.phone)
        print("Room:", self.room.room_no)
        print("Room Type:", self.room.room_type)


class Billing:
    def calculate_bill(self, room, days):
        return room.price * days


room = Room(101, "AC Deluxe", 2500)
customer = Customer("Kalyani", "9876543210")

booking = Booking(customer, room)
billing = Billing()

booking.display()

days = 3
print("Days:", days)
print("Total Bill:", billing.calculate_bill(room, days))