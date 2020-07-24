# This Parking Garage Project is handled by Asia and Nibras. 

# Step One:
- We need to create the parking garage class.
- In the parking garage class, we create the attributes: tickets, parkingSpaces and currentTicket by using __init__method.
- Initiate the attributes, tickets and parkingSpaces should be a list and currentTicket should be a dictionary.
- Create the takeTicket, payForParking and leaveGarage methods inside the ParkingGarage class.

# Step Two:
- We create the takeTicket method, it should have access to the tickets and parkingSpace attributes.
- We will use the remove method to decrease by 1 each attribute by 1 when the user is given a ticket. 

- Create the payForParking method, it should get an input and store that in a variable, havePaid. 
- Use an if statement and check if the havePaid variable is empty or not. 
- This will also update the dictionary and change the key within from paid:False, to paid:true

# Step Three:
- Create the leaveGarage method - If paid then the ticket will state, "Ticket has been paid, you have to leave in 15 minutes."
- If havePaid is false then the program will ask for payment continuosly until havePaid is true.
- Use the append method to increase the parkingSpaces and tickets lists by one.  