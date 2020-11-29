from model import *
from sqlalchemy import *
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

class DAOCrud:

    def getSession(self):
        engine = create_engine("postgres+psycopg2://postgres:root@localhost:5432/tft_bd2")
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

    def checkUser(self, session, puuid):
        user = session.query(User).filter(User.puuid == puuid).first()
        return user

    def checkUserPuuid(self, session, name):
        puuid = session.query(User).filter(User.name == name).first()
        if puuid:
            puuid = puuid.puuid
        return puuid

    def checkMatchesPlacement(self, session, puuid):
        matches = session.query(MatchUserDetail).filter(MatchUserDetail.puuid == puuid).all()
        matches_placement = []
        for match in matches:
            matches_placement.append(match.placement)

        return matches_placement

    def checkUserAvgPlacement(self, session, puuid):
        matches = session.query(MatchUserDetail).filter(MatchUserDetail.puuid == puuid).all()
        matches_placement = 0
        i = 0
        for match in matches:
            i += 1
            matches_placement += match.placement

        avg_placement = matches_placement/i
        return avg_placement

    def checkUserGold(self, session, puuid):
        matches = session.query(MatchUserDetail).filter(MatchUserDetail.puuid == puuid).all()
        matches_gold = []
        for match in matches:
            matches_gold.append(match.gold_left)

        return matches_gold

    def checkUserAvgGold(self, session, puuid):
        matches = session.query(MatchUserDetail).filter(MatchUserDetail.puuid == puuid).all()
        matches_gold = 0
        i = 0
        for match in matches:
            matches_gold += match.gold_left
            i += 1

        avg_gold = matches_gold/ i
        return avg_gold

    def checkAvgGold(self, session, upper_limit, lower_limit):
        matches = session.query(MatchUserDetail).filter(MatchUserDetail.placement <= lower_limit, MatchUserDetail.placement >= upper_limit).all()
        matches_gold = 0
        i = 0
        for match in matches:
            matches_gold += match.gold_left
            i += 1

        avg_gold = matches_gold/i
        return avg_gold

    def checkUserLastRound(self, session, puuid):
        matches = session.query(MatchUserDetail).filter(MatchUserDetail.puuid == puuid).all()
        matches_last_round = []
        for match in matches:
            matches_last_round.append(match.last_round)

        return matches_last_round

    def checkUserAvgLastRound(self, session, puuid):
        matches = session.query(MatchUserDetail).filter(MatchUserDetail.puuid == puuid).all()
        matches_last_round = 0
        i = 0
        for match in matches:
            matches_last_round += match.last_round
            i += 1

        avg_last_round = matches_last_round / i
        return avg_last_round

    def checkAvgLastRound(self, session, upper_limit, lower_limit):
        matches = session.query(MatchUserDetail).filter(MatchUserDetail.placement <= lower_limit, MatchUserDetail.placement >= upper_limit).all()
        matches_last_round = 0
        i = 0
        for match in matches:
            matches_last_round += match.last_round
            i += 1

        avg_last_round = matches_last_round/i
        return avg_last_round

    def checkEliminatedUser(self, session, puuid):
        matches = session.query(MatchUserDetail).filter(MatchUserDetail.puuid == puuid).all()
        matches_eliminated = []
        for match in matches:
            matches_eliminated.append(match.players_eliminated)

        return matches_eliminated

    def checkAvgEliminatedUser(self, session, puuid):
        matches = session.query(MatchUserDetail).filter(MatchUserDetail.puuid == puuid).all()
        matches_eliminated = 0
        i = 0
        for match in matches:
            matches_eliminated += match.players_eliminated
            i += 1

        avg_eliminated = matches_eliminated / i
        return avg_eliminated

    def checkAvgEliminated(self, session, upper_limit, lower_limit):
        matches = session.query(MatchUserDetail).filter(MatchUserDetail.placement <= lower_limit, MatchUserDetail.placement >= upper_limit).all()
        matches_eliminated = 0
        i = 0
        for match in matches:
            matches_eliminated += match.players_eliminated
            i += 1

        avg_eliminated = matches_eliminated/i
        return avg_eliminated

    def checkUserLevel(self, session, puuid):
        matches = session.query(MatchUserDetail).filter(MatchUserDetail.puuid == puuid).all()
        matches_level = []
        for match in matches:
            matches_level.append(match.level)

        return matches_level

    def checkUserAvgLevel(self, session, puuid):
        matches = session.query(MatchUserDetail).filter(MatchUserDetail.puuid == puuid).all()
        matches_level = 0
        i = 0
        for match in matches:
            matches_level += match.level
            i += 1

        avg_level = matches_level / i
        return avg_level

    def checkAvgLevel(self, session, upper_limit, lower_limit):
        matches = session.query(MatchUserDetail).filter(MatchUserDetail.placement <= lower_limit, MatchUserDetail.placement >= upper_limit).all()
        matches_level = 0
        i = 0
        for match in matches:
            matches_level += match.level
            i += 1

        avg_level = matches_level/i
        return avg_level

    def checkUserTimeEliminated(self, session, puuid):
        matches = session.query(MatchUserDetail).filter(MatchUserDetail.puuid == puuid).all()
        matches_time = []
        for match in matches:
            matches_time.append(match.time_eliminated)

        return matches_time

    def checkUserAvgTimeEliminated(self, session, puuid):
        matches = session.query(MatchUserDetail).filter(MatchUserDetail.puuid == puuid).all()
        matches_time = 0
        i = 0
        for match in matches:
            matches_time += match.time_eliminated
            i += 1

        avg_time = matches_time / i
        return avg_time

    def checkAvgTimeEliminated(self, session, upper_limit, lower_limit):
        matches = session.query(MatchUserDetail).filter(MatchUserDetail.placement <= lower_limit, MatchUserDetail.placement >= upper_limit).all()
        matches_time = 0
        i = 0
        for match in matches:
            matches_time += match.time_eliminated
            i += 1

        avg_time = matches_time/i
        return avg_time

    def checkUserTotalDamage(self, session, puuid):
        matches = session.query(MatchUserDetail).filter(MatchUserDetail.puuid == puuid).all()
        matches_damage = []
        for match in matches:
            matches_damage.append(match.total_damage_to_players)

        return matches_damage

    def checkUserAvgTotalDamage(self, session, puuid):
        matches = session.query(MatchUserDetail).filter(MatchUserDetail.puuid == puuid).all()
        matches_damage = 0
        i = 0
        for match in matches:
            matches_damage += match.total_damage_to_players
            i += 1

        avg_damage = matches_damage / i
        return avg_damage

    def checkAvgTotalDamage(self, session, upper_limit, lower_limit):
        matches = session.query(MatchUserDetail).filter(MatchUserDetail.placement <= lower_limit, MatchUserDetail.placement >= upper_limit).all()
        matches_damage = 0
        i = 0
        for match in matches:
            matches_damage += match.total_damage_to_players
            i += 1

        avg_damage = matches_damage/i
        return avg_damage

    def checkMatch(self, session, matchid):
        match = session.query(Match).filter(Match.matchid == matchid).first()
        return match

    def checkMatchUserDetails(self, session, puuid, matchid):
        match_user_details = session.query(MatchUserDetail).filter(MatchUserDetail.matchid == matchid & MatchUserDetail.puuid == puuid).first()
        return match_user_details
