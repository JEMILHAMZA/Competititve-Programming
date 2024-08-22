class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        
        a=capacityA
        
        b=capacityB
        i=0
        j=len(plants)-1
        ans=0
        while i<j:
            if plants[i]<=capacityA:
                capacityA-=plants[i]

            else:
                ans+=1
                capacityA=a
                capacityA-=plants[i]
            i+=1


            if plants[j]<=capacityB:
                capacityB-=plants[j]

            else:
                ans += 1
                capacityB = b
                capacityB-=plants[j]
            j-=1
        if i==j:
            if capacityB>capacityA:
                if plants[j] > capacityB:
                    ans += 1

            else:
                if plants[i] > capacityA:
                    ans += 1


        return ans


        