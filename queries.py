from DAO import *



def query_user_placement(username):
    daocrud = DAOCrud()
    session = daocrud.getSession()
    puuid = daocrud.checkUserPuuid(session, username)
    print(puuid)
    if puuid:
        placements = daocrud.checkMatchesPlacement(session, puuid)
    else:
        placements = 'User not found'
    print(placements)
    session.commit()
    session.close()
    return placements

def query_avg_user_placement(username):
    daocrud = DAOCrud()
    session = daocrud.getSession()
    puuid = daocrud.checkUserPuuid(session, username)
    print(puuid)
    if puuid:
        avg_placement = daocrud.checkUserAvgPlacement(session, puuid)
    else:
        avg_placement = 'User not found'
    print(avg_placement)
    session.commit()
    session.close()
    return avg_placement

def query_user_gold(username):
    daocrud = DAOCrud()
    session = daocrud.getSession()
    puuid = daocrud.checkUserPuuid(session, username)
    print(puuid)
    if puuid:
        gold = daocrud.checkUserGold(session, puuid)
    else:
        gold = "User not found"
    print(gold)
    session.commit()
    session.close()
    return gold

def query_user_avg_gold(username):
    daocrud = DAOCrud()
    session = daocrud.getSession()
    puuid = daocrud.checkUserPuuid(session, username)
    print(puuid)
    if puuid:
        avg_gold = daocrud.checkUserAvgGold(session, puuid)
    else:
        avg_gold = "User not found"
    print(avg_gold)
    session.commit()
    session.close()
    return avg_gold

def query_avg_gold(upper_limit, lower_limit):
    if upper_limit < 1 or lower_limit > 8 or lower_limit< upper_limit:
        return 'Incorrect parameters'

    daocrud = DAOCrud()
    session = daocrud.getSession()
    avg_gold = daocrud.checkAvgGold(session, upper_limit, lower_limit)
    print(avg_gold)
    session.commit()
    session.close()
    return avg_gold

def query_user_last_round(username):
    daocrud = DAOCrud()
    session = daocrud.getSession()
    puuid = daocrud.checkUserPuuid(session, username)
    print(puuid)
    if puuid:
        last_round = daocrud.checkUserLastRound(session, puuid)
    else:
        last_round = 'User not found'
    print(last_round)
    session.commit()
    session.close()
    return last_round

def query_user_avg_last_round(username):
    daocrud = DAOCrud()
    session = daocrud.getSession()
    puuid = daocrud.checkUserPuuid(session, username)
    print(puuid)
    if puuid:
        avg_last_round = daocrud.checkUserAvgLastRound(session, puuid)
    else:
        avg_last_round = 'User not found'
    print(avg_last_round)
    session.commit()
    session.close()
    return avg_last_round

def query_avg_last_round(upper_limit, lower_limit):
    if upper_limit < 1 or lower_limit > 8 or lower_limit<upper_limit:
        return 'Incorrect parameters'

    daocrud = DAOCrud()
    session = daocrud.getSession()
    avg_last_round = daocrud.checkAvgLastRound(session, upper_limit, lower_limit)
    print(avg_last_round)
    session.commit()
    session.close()
    return avg_last_round

def query_eliminated_user(username):
    daocrud = DAOCrud()
    session = daocrud.getSession()
    puuid = daocrud.checkUserPuuid(session, username)
    if puuid:
        eliminated_user = daocrud.checkEliminatedUser(session, puuid)
    else:
        eliminated_user = 'User not found'
    print(eliminated_user)

    session.commit()
    session.close()
    return eliminated_user

def query_avg_eliminated_user(username):
    daocrud = DAOCrud()
    session = daocrud.getSession()
    puuid = daocrud.checkUserPuuid(session, username)
    if puuid:
        avg_eliminated_user = daocrud.checkAvgEliminatedUser(session, puuid)
    else:
        avg_eliminated_user = 'User not found'
    print(avg_eliminated_user)
    session.commit()
    session.close()
    return avg_eliminated_user

def query_avg_eliminated(upper_limit, lower_limit):
    if upper_limit < 1 or lower_limit > 8 or lower_limit<upper_limit:
        return 'Incorrect parameters'

    daocrud = DAOCrud()
    session = daocrud.getSession()
    avg_eliminated = daocrud.checkAvgEliminated(session, upper_limit, lower_limit)
    print(avg_eliminated)
    session.commit()
    session.close()
    return avg_eliminated

def query_user_level(username):
    daocrud = DAOCrud()
    session = daocrud.getSession()
    puuid = daocrud.checkUserPuuid(session, username)
    if puuid:
        level = daocrud.checkUserLevel(session, puuid)
    else:
        level = 'User not found'
    print(level)
    session.commit()
    session.close()
    return level

def query_user_avg_level(username):
    daocrud = DAOCrud()
    session = daocrud.getSession()
    puuid = daocrud.checkUserPuuid(session, username)
    if puuid:
        avg_user_level = daocrud.checkUserAvgLevel(session, puuid)
    else:
        avg_user_level = 'User not found'
    print(avg_user_level)
    session.commit()
    session.close()
    return avg_user_level

def query_avg_level(upper_limit, lower_limit):
    if upper_limit < 1 or lower_limit > 8 or lower_limit<upper_limit:
        return 'Incorrect parameters'

    daocrud = DAOCrud()
    session = daocrud.getSession()
    avg_level = daocrud.checkAvgLevel(session, upper_limit, lower_limit)
    print(avg_level)
    session.commit()
    session.close()
    return avg_level


def query_user_time_eliminated(username):
    daocrud = DAOCrud()
    session = daocrud.getSession()
    puuid = daocrud.checkUserPuuid(session, username)
    if puuid:
        time_eliminated = daocrud.checkUserTimeEliminated(session, puuid)
    else:
        time_eliminated = 'User not found'
    print(time_eliminated)
    session.commit()
    session.close()
    return time_eliminated

def query_user_avg_time_eliminated(username):
    daocrud = DAOCrud()
    session = daocrud.getSession()
    puuid = daocrud.checkUserPuuid(session, username)
    if puuid:
        avg_time_eliminated = daocrud.checkUserAvgTimeEliminated(session, puuid)
    else:
        avg_time_eliminated = 'User not found'
    print(avg_time_eliminated)
    session.commit()
    session.close()
    return avg_time_eliminated

def query_avg_time_eliminated(upper_limit, lower_limit):
    if upper_limit < 1 or lower_limit > 8 or lower_limit<upper_limit:
        return 'Incorrect parameters'

    daocrud = DAOCrud()
    session = daocrud.getSession()
    avg_time_eliminated = daocrud.checkAvgTimeEliminated(session, upper_limit, lower_limit)
    print(avg_time_eliminated)
    session.commit()
    session.close()
    return avg_time_eliminated

def query_user_total_damage(username):
    daocrud = DAOCrud()
    session = daocrud.getSession()
    puuid = daocrud.checkUserPuuid(session, username)
    if puuid:
        total_damage = daocrud.checkUserTotalDamage(session, puuid)
    else:
        total_damage = 'User not found'
    print(total_damage)
    session.commit()
    session.close()
    return total_damage

def query_user_avg_total_damage(username):
    daocrud = DAOCrud()
    session = daocrud.getSession()
    puuid = daocrud.checkUserPuuid(session, username)
    if puuid:
        avg_total_damage = daocrud.checkUserAvgTotalDamage(session, puuid)
    else:
        avg_total_damage = 'User not found'
    print(avg_total_damage)
    session.commit()
    session.close()
    return avg_total_damage

def query_avg_total_damage(upper_limit, lower_limit):
    if upper_limit < 1 or lower_limit > 8 or lower_limit<upper_limit:
        return 'Incorrect parameters'

    daocrud = DAOCrud()
    session = daocrud.getSession()
    avg_total_damage = daocrud.checkAvgTotalDamage(session, upper_limit, lower_limit)
    print(avg_total_damage)
    session.commit()
    session.close()
    return avg_total_damage


