class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        left_max=height[left]
        right_max=height[right]
        max_w=0
        while left<right:
          if left_max<right_max:
            water=left_max-height[left]
            if water>=0:
              left+=1
              left_max = max(left_max, height[left])
              
              max_w+=water
          else:
            water=right_max-height[right]
            if water>=0:
              right-=1
              right_max=max(right_max,height[right])
             
              max_w +=water
        return max_w
              




          

