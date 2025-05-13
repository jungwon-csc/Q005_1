def Yellow_Red_YN(card, number, n_list):
    if card == 1:
        return True
    elif card == 2:
        return True
    else:
        if n_list[number] < 2:
            return print('No')
        else:
            return print('Yes')
    

def match_of_rugby():
    N, Q = map(int, input().split())
    N_list = [0]*N
    for _ in range(Q):
        card, temp_N = map(int, input().split())
        result = Yellow_Red_YN(card, temp_N-1, N_list)
        if result == True:
            N_list[temp_N-1] += card
    return 0

match_of_rugby()