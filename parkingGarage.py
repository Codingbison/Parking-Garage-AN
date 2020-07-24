class ParkingGarage():
    def __init__(self, tickets, parkingSpaces, currentTickets):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTickets = currentTickets

    # Creating the takeTicket method.
    def takeTicket(self):
        # Sets the ticket and parking space amount to 10. 
        self.tickets = list(range(1, 11))
        self.parkingSpaces = list(range(1, 11))   

        # If there is at least 1 parking space a ticket will be printed. 
        if len(self.parkingSpaces) > 0:
            # Provides a ticket number and removes the parking space. 
            self.ticket_number = self.tickets.pop()
            print (f"Your ticket number is {self.ticket_number}")
            self.space_left = self.parkingSpaces.pop()   

    # Creating the payForParking method.
    def payForParking(self):
        self.currentTickets.update({'paid':False})
        while True:
            havePaid = input("Have you entered payment?")
            if havePaid.lower() == 'yes':
                self.currentTickets.update({'paid':True})
                print("Ticket has been paid. You have 15 minutes to leave.")
                print("Thank you, have a nice day!")
                break
            else:
                print("You must pay before departing.")

    #Creating the leaveGarage method.
    def leaveGarage(self):
        self.tickets = self.tickets.append(self.ticket_number)
        self.parkingSpaces.append(self.space_left)
        print (f"There are currently {len(self.parkingSpaces)} parking spaces left.")

# Instantialting the parkInGarage class with the parkInGarage method.
def parkInTheGarage():
    car_1 = ParkingGarage([], [], {})
    while True:
        response = input("Would you like to get a parking ticket? Yes or No. ")
        # If user inputs 'Yes' the functions in the class will run.
        if response.lower() == "yes":
            car_1.takeTicket()
            car_1.payForParking()
            car_1.leaveGarage()
            break

        # If user inputs 'No' the user will leave the program.
        if response.lower() == "no":
            print("No ticket. No parking. You must leave, security on the way.")
            break

        # If user inputs anything but yes or no they will be re-prompted. 
        elif response.lower() != 'yes' or response.lower() != 'no':
            print("You need to enter yes or no.")

# Run the parkInGarage function
parkInTheGarage()
