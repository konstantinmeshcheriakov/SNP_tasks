class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass

def rps_game_winner(arr):
    action = 'PRS'
    if len(arr) > 2:
        raise WrongNumberOfPlayersError('Количество игроков должно быть не больше двух')
    if not arr[0][1] in action or not arr[1][1] in action:
        raise NoSuchStrategyError('Был использован неправильный ход игрока')
    if len(arr) <= 2 and arr[0][1] in action or arr[1][1] in action:
        if arr[0][1] == 'P' and arr[1][1] == 'R':
            return f"{arr[0][0]} {arr[0][1]}"
        elif arr[0][1] == 'R' and arr[1][1] == 'P':
            return f"{arr[1][0]} {arr[1][1]}"
        elif arr[0][1] == 'S' and arr[1][1] == 'P':
            return f"{arr[0][0]} {arr[0][1]}"
        elif arr[0][1] == 'P' and arr[1][1] == 'S':
            return f"{arr[1][0]} {arr[1][1]}"
        elif arr[0][1] == 'R' and arr[1][1] == 'S':
            return f"{arr[0][0]} {arr[0][1]}"
        elif arr[0][1] == 'S' and arr[1][1] == 'R':
            return f"{arr[1][0]} {arr[1][1]}"    
        else:
            return f"{arr[0][0]} {arr[0][1]}"
        

