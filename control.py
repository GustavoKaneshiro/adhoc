from view import Viewer
from queries import *
from matplotlib import pyplot
import numpy


class Controller:
    def __init__(self):
        self.view = Viewer()

    def inicio(self):
        option = self.view.inicio()
        while option != 8:
            if option == 1:
                selector = self.view.TwoOptions()
                if selector == 1:
                    username = self.view.getUsername()
                    placements = query_user_placement(username)
                if selector == 2:
                    username = self.view.getUsername()
                    placements = query_avg_user_placement(username)
                option = self.view.inicio()

            if option == 2:
                selector = self.view.ThreeOptions()
                if selector == 1:
                    username = self.view.getUsername()
                    gold = query_user_gold(username)
                if selector == 2:
                    username = self.view.getUsername()
                    gold = query_user_avg_gold(username)
                if selector == 3:
                    limits = self.view.getLimits()
                    gold = query_avg_gold(limits[0], limits[1])
                option = self.view.inicio()

            if option == 3:
                selector = self.view.ThreeOptions()
                if selector == 1:
                    username = self.view.getUsername()
                    level = query_user_level(username)
                if selector == 2:
                    username = self.view.getUsername()
                    level = query_user_avg_level(username)
                if selector == 3:
                    limits = self.view.getLimits()
                    level = query_avg_level(limits[0], limits[1])
                option = self.view.inicio()

            if option == 4:
                selector = self.view.ThreeOptions()
                if selector == 1:
                    username = self.view.getUsername()
                    time = query_user_time_eliminated(username)
                if selector == 2:
                    username = self.view.getUsername()
                    time = query_user_avg_time_eliminated(username)
                if selector == 3:
                    limits = self.view.getLimits()
                    time = query_avg_time_eliminated(limits[0], limits[1])
                option = self.view.inicio()

            if option == 5:
                selector = self.view.ThreeOptions()
                if selector == 1:
                    username = self.view.getUsername()
                    players = query_eliminated_user(username)
                if selector == 2:
                    username = self.view.getUsername()
                    players = query_avg_eliminated_user(username)
                if selector == 3:
                    limits = self.view.getLimits()
                    players = query_avg_eliminated(limits[0], limits[1])
                option = self.view.inicio()

            if option == 6:
                selector = self.view.ThreeOptions()
                if selector == 1:
                    username = self.view.getUsername()
                    damage = query_user_total_damage(username)
                if selector == 2:
                    username = self.view.getUsername()
                    damage = query_user_avg_total_damage(username)
                if selector == 3:
                    limits = self.view.getLimits()
                    damage = query_avg_total_damage(limits[0], limits[1])
                option = self.view.inicio()

            if option == 7:
                selector = self.view.ThreeOptions()
                if selector == 1:
                    username = self.view.getUsername()
                    last_round = query_user_last_round(username)
                if selector == 2:
                    username = self.view.getUsername()
                    last_round = query_user_avg_last_round(username)
                if selector == 3:
                    limits = self.view.getLimits()
                    last_round = query_avg_last_round(limits[0], limits[1])
                option = self.view.inicio()