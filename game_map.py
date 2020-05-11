from collections import deque 


def solution(maps):
    short = deque([1])                             
    loc_list = deque([(0,0)])
    end = (len(maps)-1, len(maps[0])-1)
    print(end)
    can_move = [(0,1), (1,0), (0,-1), (-1,0)]
    maps[0][0] = 0
    finish = False
    while not finish:
        loc_list, short, end, can_move, maps, finish = move( loc_list, short, end, can_move, maps, finish)
        print(loc_list, short, maps)
        if not loc_list:
            break
    if finish:
        return short.pop()
    else:
        return -1


def move(loc_list, short, end, can_move, maps, finish):
    now = loc_list.popleft()
    dist = short.popleft()
    for i in can_move:
        next_loc = (now[0]+i[0], now[1]+i[1])
        if next_loc == end:
            finish = True
            short.append(dist+1)
            return loc_list, short, end, can_move, maps, finish
        elif -1 < next_loc[0] and next_loc[0] <= end[0] and -1 < next_loc[1] and next_loc[1] <= end[1] and maps[next_loc[0]][next_loc[1]] == 1:
            loc_list.append(next_loc)
            short.append(dist+1)
            maps[next_loc[0]][next_loc[1]] = 0
    return loc_list, short, end, can_move, maps, finish


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1],[0,0,0,0,1]]))
