class ParkingGarage:
    def __init__(self, total_tickets, total_parking_spaces):
        self.tickets = list(range(1, total_tickets + 1))
        self.parkingSpaces = list(range(1, total_parking_spaces + 1))
        self.currentTicket = {}  # Initialize an empty dictionary to store ticket information

    def takeTicket(self):
        if self.tickets:
            ticket = self.tickets.pop(0)
            parking_space = self.parkingSpaces.pop(0)
            self.currentTicket[ticket] = {'paid': False, 'parking_space': parking_space}
            print(f"Please take ticket {ticket}. Your parking space is {parking_space}.")

    def payForParking(self, ticket):
        if ticket in self.currentTicket and not self.currentTicket[ticket]['paid']:
            payment = input("Enter the amount to pay for parking: ")
            if payment:
                self.currentTicket[ticket]['paid'] = True
                print(f"Ticket {ticket} has been paid. You have 15 minutes to leave.")
            else:
                print("Payment not received. Please pay for parking within 15 minutes.")
        else:
            print("Invalid ticket or ticket has already been paid.")

    def leaveGarage(self, ticket):
        if ticket in self.currentTicket:
            if self.currentTicket[ticket]['paid']:
                print("Thank you, have a nice day!")
                self.parkingSpaces.append(self.currentTicket[ticket]['parking_space'])
                self.tickets.append(ticket)
                del self.currentTicket[ticket]
            else:
                print("Please pay for parking before leaving.")
        else:
            print("Invalid ticket. Please take a valid ticket.")


garage = ParkingGarage(10, 10)

while True:
    print("Options:")
    print("1. Take a ticket")
    print("2. Pay for parking")
    print("3. Leave the garage")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        garage.takeTicket()
    elif choice == '2':
        ticket = int(input("Enter your ticket number: "))
        garage.payForParking(ticket)
    elif choice == '3':
        ticket = int(input("Enter your ticket number: "))
        garage.leaveGarage(ticket)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please select a valid option.")

        
