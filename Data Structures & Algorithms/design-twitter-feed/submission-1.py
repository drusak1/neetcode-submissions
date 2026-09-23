class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.time = 0
        self.posts = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time,tweetId))
        self.time +=1 

    def getNewsFeed(self, userId: int) -> List[int]:
        follows  = self.follows[userId].copy()
        follows.add(userId)

        all_posts = []

        for follow in follows:
            all_posts.extend(self.posts[follow][-10:])

        res = []
        for post in all_posts:
            if len(res) == 10:
                heapq.heappushpop(res,post)
            else:
                heapq.heappush(res, post)
        res.sort(key = lambda x: x[0], reverse=True)
        return [post for time,post in res]
            

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
