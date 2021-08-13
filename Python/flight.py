class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passangers = []
    
    
    def add_passangers(self, name):
        if not self.open_seats():
            return False
        else:
            self.passangers.append(name)
            return True

    def open_seats(self):
        return self.capacity - len(self.passangers)
    

flight = Flight(3)
people = ['Aragorn','Legolas','Gimli','Boromir']

for person in people:
    if flight.add_passangers(person):
        print(f'Added {person} to flight sucessufully.')
    else:
        print(f'No available seats for {person}')
