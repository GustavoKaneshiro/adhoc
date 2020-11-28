class Viewer():

    def inicio(self):
        return self.menu()

    def menu(self):
        while 1:
            print("Menu")
            print("1 - User Info")
            print("2 - Average Info Between Placements")
            print("3 - Quit")
            option = int(input("Insert Option Number: "))
            if 3 >= option >= 1:
                return option
            else:
                print("Invalid Option")

    def userMenu(self):
        selected = []
        exit_func = 1
        while exit_func == 1:
            print("Menu")
            print("1 - Placement Info")
            print("2 - Average Placement Info")
            print("3 - Gold Info")
            print("4 - Average Gold Info")
            print("5 - Level Info")
            print("6 - Average Level Info")
            print("7 - Time Eliminated Info")
            print("8 - Average Time Eliminated Info")
            print("9 - Players Eliminated Info")
            print("10 - Average Players Eliminated Info")
            print("11 - Total Damage to Players Info")
            print("12 - Average Total Damage to Players Info")
            print("13 - Last Round Info")
            print("14 - Average Last Round Info")
            print("15 - CONFIRM")
            print("16 - QUIT")
            for item in selected:
                print("Selected: ", item)

            option = int(input("Insert Option Number: "))

            if 14 >= option >= 1:
                if option in selected:
                    selected.remove(option)
                else:
                    selected.append(option)
            if option == 15:
                exit_func = 2
            if option == 16:
                exit_func = -1
            if option > 16 or option < 1:
                print("Invalid Option")

        if exit_func == 2:
            return selected
        else:
            return []

    def avgMenu(self):
        selected = []
        exit_func = 1
        while exit_func == 1:
            print("Menu")
            print("1 - Average Gold Info")
            print("2 - Average Level Info")
            print("3 - Average Time Eliminated Info")
            print("4 - Average Players Eliminated Info")
            print("5 - Average Total Damage to Players Info")
            print("6 - Average Last Round Info")
            print("7 - CONFIRM")
            print("8 - QUIT")
            for item in selected:
                print("Selected : ", item)
            option = int(input("Insert Option Number: "))
            if 6 >= option >= 1:
                if option in selected:
                    selected.remove(option)
                else:
                    selected.append(option)
            if option == 7:
                exit_func = 2
            if option == 8:
                exit_func = -1
            if option > 8 or option < 1:
                print("Invalid Option")

        if exit_func == 2:
            return selected
        else:
            return []

    def getUsername(self):
        username = input("Type the Username: ")
        return username

    def getLimits(self):
        print("Select the Placement Range: Ex.:1 4 will show the average of people between the first and fourth place")
        upper_limit = int(input("Type the upper range: "))
        lower_limit = int(input("Type the lower range: "))
        limits = [upper_limit, lower_limit]
        return limits
