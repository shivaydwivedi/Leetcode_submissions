class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))

        S = []
        
        for start, end in intervals:
            # Count how many from S fall inside this interval
            cnt = 0
            if len(S) >= 1 and S[-1] >= start:
                cnt += 1
            if len(S) >= 2 and S[-2] >= start:
                cnt += 1

            # Need to add elements
            if cnt == 2:
                continue
            elif cnt == 1:
                # Add the largest possible element
                S.append(end if S[-1] != end else end - 1)
            else:  # cnt == 0
                S.append(end - 1)
                S.append(end)

        return len(S)