from collections import defaultdict
# https://leetcode.com/problems/angle-between-hands-of-a-clock/

def angleClock(hour, minutes):
    hour_hash_map = defaultdict(int)
    hour_val = 30
    for h in range(12):
        hour_hash_map[h+1] = hour_val
        hour_val += 30
    
    minute_hash_map = defaultdict(int)
    min_val = 6
    for m in range(60):
        minute_hash_map[m+1] = min_val
        min_val += 6
    
    hour_hand_move = ( minutes / 60 ) * 30

    if abs( abs( hour_hash_map[hour] - minute_hash_map[minutes] ) - hour_hand_move ) == 360:
        return 0

    
    if hour_hash_map[hour] > minute_hash_map[minutes] and hour_hash_map[hour] != 360:
        return abs( abs( hour_hash_map[hour] - minute_hash_map[minutes] ) + hour_hand_move )

    return min( 360 - abs( abs( hour_hash_map[hour] - minute_hash_map[minutes] ) - hour_hand_move ),
        abs( abs( hour_hash_map[hour] - minute_hash_map[minutes] ) - hour_hand_move ) 
    )


if __name__ == '__main__':
    print( angleClock(12, 30) )
    print( angleClock(3, 30) )
    print( angleClock(3, 15) )
    print( angleClock(12, 0) )
    print( angleClock(6,5) )
    print( angleClock(1,4) )

    print( angleClock(1, 57) )
    print( angleClock(8, 7) )