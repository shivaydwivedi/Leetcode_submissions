import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.userTweets = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.userTweets[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int):
        heap = []

        # user follows themselves
        self.followMap[userId].add(userId)

        for followee in self.followMap[userId]:
            tweets = self.userTweets[followee]
            if tweets:
                time, tweetId = tweets[-1]
                idx = len(tweets) - 1
                heapq.heappush(heap, (-time, tweetId, followee, idx - 1))

        result = []

        while heap and len(result) < 10:
            time, tweetId, followee, idx = heapq.heappop(heap)
            result.append(tweetId)

            if idx >= 0:
                next_time, next_tweet = self.userTweets[followee][idx]
                heapq.heappush(heap, (-next_time, next_tweet, followee, idx - 1))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)