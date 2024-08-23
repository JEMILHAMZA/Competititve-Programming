class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1:
            return 0
        nums=[True]*n
        nums[0]=False
        nums[1]=False
        h=n**(0.5)
        i=2
        while i<=h:
            if nums[i]==True:
                for j in range(i,n,i):
                    nums[j]=False
                nums[i]=True
            i+=1
        ans=0
        for i in nums:
            if i==True:
                ans+=1
        return ans



        