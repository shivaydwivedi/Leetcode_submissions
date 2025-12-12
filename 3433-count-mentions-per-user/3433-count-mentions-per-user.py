from collections import defaultdict

class Solution:
    def countMentions(self, numberOfUsers, events):
        # Parse events with timestamp and original index
        packed = []
        for idx, ev in enumerate(events):
            etype, ts_str, data = ev
            t = int(ts_str)
            # type priority: OFFLINE before MESSAGE at same timestamp
            typ_pr = 0 if etype == "OFFLINE" else 1
            packed.append((t, typ_pr, idx, etype, data))

        # sort by (timestamp, type_priority, original_index)
        packed.sort(key=lambda x: (x[0], x[1], x[2]))

        online = [True] * numberOfUsers
        restore = [0] * numberOfUsers    # restore time (when user becomes online)
        mentions = [0] * numberOfUsers

        cur_time = -1
        # Iterate sorted events
        for t, typ_pr, idx, etype, data in packed:
            # If we moved to a new timestamp t, restore all users whose restore_time <= t
            if t != cur_time:
                # restore all eligible users
                for u in range(numberOfUsers):
                    if not online[u] and restore[u] <= t:
                        online[u] = True
                cur_time = t

            if etype == "OFFLINE":
                uid = int(data)
                online[uid] = False
                restore[uid] = t + 60
            else:  # MESSAGE
                tokens = data.split()
                for tok in tokens:
                    if tok == "ALL":
                        for u in range(numberOfUsers):
                            mentions[u] += 1
                    elif tok == "HERE":
                        for u in range(numberOfUsers):
                            if online[u]:
                                mentions[u] += 1
                    else:
                        # tok is id<number>
                        uid = int(tok[2:])
                        mentions[uid] += 1

        return mentions
