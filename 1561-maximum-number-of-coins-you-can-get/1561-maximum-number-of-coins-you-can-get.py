class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        round=len(piles)//3
        sum=0
        for i in range(len(piles)-2,0,-2):
            if round > 0:
                sum+=piles[i]
                round-=1
        return sum


        