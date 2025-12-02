from collections import deque 
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # initiate empty queues
        queue_r = deque()
        queue_d = deque()
        # length of string 
        n = len(senate)
        # filling queues with initial inidces
        for i in range(n):
            if senate[i] == 'R':
                queue_r.append(i)
            else:
                queue_d.append(i)
        # start rounds
        while queue_r and queue_d:
            r_index = queue_r.popleft()
            d_index = queue_d.popleft()
            # compare indices
            if r_index < d_index:
                # ban D
                queue_r.append(r_index+n)
            else:
                # ban R
                queue_d.append(d_index+n)
        # Return  winner
        if queue_r:
            return "Radiant"
        else:
            return "Dire"
