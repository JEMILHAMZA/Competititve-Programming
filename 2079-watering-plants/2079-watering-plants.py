class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        c=capacity
        ans=0
        step=0
        for i in range(len(plants)):
            if plants[i]<=capacity:
                capacity-=plants[i]
                step+=1
                ans+=1
            else:
                ans+=step
                capacity=c
                capacity -= plants[i]
                step += 1
                ans+=step
        return ans
        