class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_op=k
        for left in range(len(blocks)-k+1):
            right=left+k
            se=0
            for i in blocks[left:right]:
                if i!='B':
                    se+=1
            min_op=min(min_op,se)
        return min_op



        