#Leetcode premuim
#Idea start from gate instead of empty rooms

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        
        def isValid(r,c,steps):
            return len(rooms)>r>=0 and len(rooms[0])>c>=0 and rooms[r][c]>steps
        
        def goFill(r,c,steps):
            
            
            stack=[(r,c,steps)]
            while stack:
                r,c,moves=stack.pop()
                for i,j in directions:
                    nR,nC=r+i,c+j
                    if isValid(nR,nC,moves):
                        rooms[nR][nC]=moves
                        stack.append((nR,nC,moves+1))
            
        
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c]==0:
                    goFill(r,c,1)
        return rooms
