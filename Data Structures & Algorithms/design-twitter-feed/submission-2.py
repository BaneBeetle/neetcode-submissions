from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.count = 0
        self.following = defaultdict(set)
        self.posts = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        self.posts[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        ret = []
        heap = []
        followed_accounts = self.following[userId]

        for account in followed_accounts:
            if self.posts[account]:
                time = self.posts[account][-1][0]
                tweet = self.posts[account][-1][1]
                # (Time, Tweet, Index, AccountID)
                heapq.heappush(heap, (time, tweet, -1, account))
        
        if self.posts[userId]:
            time = self.posts[userId][-1][0]
            tweet = self.posts[userId][-1][1]
            heapq.heappush(heap, (time, tweet, -1, userId))
            

        while heap and len(ret) < 10:
            time, tweet, i, accountId = heapq.heappop(heap)
            ret.append(tweet)

            if i - 1 >= -len(self.posts[accountId]):
                time = self.posts[accountId][i-1][0]
                tweet = self.posts[accountId][i-1][1]
                heapq.heappush(heap, (time, tweet, i-1, accountId))
                
        
        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
