

class Concessionaire:

    def __init__(self, name):

        self.name = name
        self.cars = []

    def get_cars(self):

        return self.cars


    def get_name(self):

        return

    def add_car(self, car):

        self.cars.append(car)


    def save_car(self):

        file = open('LIBRARY', 'w')

        for line in self.cars:

            file.write(str(line.get_data()))
            file.write('\n')
        file.close()


    def recover(self):

        for i in self.cars:
            print(str(i))