class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        if height[i] <= height[j]:
            h = height[i]
        else:
            h = height[j]
        area=(j-i)*h
        while i<j:
            if height[i]<=height[j]:
                i+=1
            else:
                j-=1
            if height[i]<=height[j]:
                h=height[i]
            else:
                h=height[j]
            areaN=(j-i)*h
            if areaN>area:
                area=areaN
        return area
        