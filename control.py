from view import Viewer
from queries import *
from matplotlib import pyplot
import numpy



class Controller:
    def __init__(self):
        self.view = Viewer()

    def inicio(self):
        option = self.view.inicio()

        while option != 3:
            if option == 1:

                selected_list = self.view.userMenu()
                username = selected_list[0]
                selected_list.remove(username)
                name_list = []
                info_list = []

                for item in selected_list:
                    item = int(item)
                    if item == 1:
                        name_list.append("User Placements")
                        info_list.append(query_user_placement(username))
                    if item == 2:
                        name_list.append("User Average Placement")
                        info_list.append([query_avg_user_placement(username)])
                    if item == 3:
                        name_list.append("User Gold Left")
                        info_list.append(query_user_gold(username))
                    if item == 4:
                        name_list.append("User Average Gold Left")
                        info_list.append([query_user_avg_gold(username)])
                    if item == 5:
                        name_list.append("User Level")
                        info_list.append(query_user_level(username))
                    if item == 6:
                        name_list.append("User Average Level")
                        info_list.append([query_user_avg_level(username)])
                    if item == 7:
                        name_list.append("User Time Eliminated")
                        info_list.append(query_user_time_eliminated(username))
                    if item == 8:
                        name_list.append("User Average Time Eliminated")
                        info_list.append([query_user_avg_time_eliminated(username)])
                    if item == 9:
                        name_list.append("User Players Eliminated")
                        info_list.append(query_eliminated_user(username))
                    if item == 10:
                        name_list.append("User Average Players Eliminated")
                        info_list.append([query_avg_eliminated_user(username)])
                    if item == 11:
                        name_list.append("User Total Damage to Players")
                        info_list.append(query_user_total_damage(username))
                    if item == 12:
                        name_list.append("User Average Total Damage to Players")
                        info_list.append([query_user_avg_total_damage(username)])
                    if item == 13:
                        name_list.append("User Last Round ")
                        info_list.append(query_user_last_round(username))
                    if item == 14:
                        name_list.append("User Average Last Round")
                        info_list.append([query_user_avg_last_round(username)])

                print("")
                i = 0
                for item in name_list:
                    print(item, " - ", username)
                    for info in info_list[i]:
                        print(info)
                    print("")
                    i += 1

            if option == 2:

                selected_list = self.view.avgMenu()
                limits = selected_list[0]
                selected_list.remove(limits)
                name_list = []
                info_list = []

                for item in selected_list:
                    item = int(item) - 8
                    if item == 1:
                        name_list.append("Average Gold")
                        info_list.append([query_avg_gold(limits[0], limits[1])])
                    if item == 2:
                        name_list.append("Average Level")
                        info_list.append([query_avg_level(limits[0], limits[1])])
                    if item == 3:
                        name_list.append("Average Time Eliminated")
                        info_list.append([query_avg_time_eliminated(limits[0], limits[1])])
                    if item == 4:
                        name_list.append("Average Players Eliminated")
                        info_list.append([query_avg_eliminated(limits[0], limits[1])])
                    if item == 5:
                        name_list.append("Average Total Damage to Players")
                        info_list.append([query_avg_total_damage(limits[0], limits[1])])
                    if item == 6:
                        name_list.append("Average Last Round")
                        info_list.append([query_avg_last_round(limits[0], limits[1])])

                i = 0
                print("")
                for name in name_list:
                    print(name, " : ", limits[0], "-", limits[1])
                    for info in info_list[i]:
                        print(info)
                    print("")
                    i += 1

            option = self.view.inicio()


