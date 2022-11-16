"""
Time: O(n)
Space: O(n)
"""

from typing import List
from collections import defaultdict


def solve(bookings: List[str]):

    booked_rooms = defaultdict(list)


    for booking in bookings:

        booked = booking[0] == '+'
        room = booking[1:]

        if room not in booked_rooms:
            booked_rooms[room] = [booked, 1]
        else:
            if booked != booked_rooms[room][0]:
                if booked:
                    booked_rooms[room][1] += 1
                
                booked_rooms[room][0] = booked
    
    max_booked = 0
    max_booked_room = ""

    for room, status_and_count in booked_rooms.items():
        
        count = status_and_count[1]
        
        if max_booked < count:
            max_booked_room = room
            max_booked = count
        elif max_booked == count:
            max_booked_room = room if room < max_booked_room else max_booked_room

    return max_booked_room  
