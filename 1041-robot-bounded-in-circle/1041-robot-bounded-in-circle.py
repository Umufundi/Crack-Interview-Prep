class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        #should just be able to use instructions to have direction var and compare endpoint to beginning point 
        current_pos = [0,0]

        current_dir = [0,1]


        for i in instructions:
            if i == 'L':
                current_dir[0], current_dir[1] = -1*current_dir[1], current_dir[0]
            elif i == 'R':
                current_dir[0], current_dir[1] = current_dir[1], current_dir[0]*-1
            else:
                current_pos[0]= current_pos[0] + current_dir[0]
                current_pos[1]= current_pos[1] + current_dir[1]
        
        if current_pos == [0,0] or current_dir != [0,1]:
            return True 
        return False