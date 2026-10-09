class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # I want to store (p, mph)
        # sort asc order based on their position
        sorted_cars = sorted(list(zip(position, speed))) # sorts based on position (p, s)

        # calculate their time to reach target (target - position / mph)
        reach_time = []
        for position, speed in sorted_cars:
            reach_time.append((target - position) / speed)
        
        print(reach_time[::-1])

        bottle_neck = 0
        longest_time = None
        for time in reach_time[::-1]:
            if not longest_time:
                longest_time = time # 3
                bottle_neck += 1
            else:
                if time > longest_time:
                    longest_time = time
                    bottle_neck += 1
 
        # Who gets bottle necked?
        # Our current car will get bottlenecked if we loop through the reach_time and there is an element
        # that is equal or less than our current reach time

        print(bottle_neck)

        return bottle_neck