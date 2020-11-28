class Viewer():

    def inicio(self):
        return self.menu()

    def menu(self):
        print("Menu")
        print("1 - Placement Info")
        print("2 - Gold Info")
        print("3 - Level Info")
        print("4 - Time Eliminated Info")
        print("5 - Players Eliminated Info")
        print("6 - Total Damage to Players Info")
        print("7 - Last Round Info")
        print("8 - Quit")
        option = int(input("Insert Option Number: "))
        return option

    def getUsername(self):
        username = input("Type the Username: ")
        return username

    def getLimits(self):
        print("Select the Placement Range: Ex.:1 4 will show the average of people between the first and fourth place")
        upper_limit = int(input("Type the upper range: "))
        lower_limit = int(input("Type the lower range: "))
        limits = [upper_limit, lower_limit]
        return limits

    def ThreeOptions(self):
        while 1:
            print("Menu")
            print("1 - User Stats")
            print("2 - User Average")
            print("3 - Average of Users Between Placement Range")
            print("4 - Return to Menu")
            option = int(input("Insert Option Number: "))
            if 4 >= option >= 1:
                return option
            else:
                print("Invalid Option")

    def TwoOptions(self):
        while 1:
            print("Menu")
            print("1 - User Stats")
            print("2 - User Average")
            print("3 - Return to Menu")
            option = int(input("Insert Option Number: "))
            if 3 >= option >= 1:
                return option
            else:
                print("Invalid Option")