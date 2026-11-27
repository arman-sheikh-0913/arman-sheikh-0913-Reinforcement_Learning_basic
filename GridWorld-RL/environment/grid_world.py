class GridWorld:
    def __init__(self):
        self.row=5
        self.column=5
        
        self.start=(0,0)
        self.goal=(4,4)
        
        self.obstacles=[(1,1),
                        (1,2),
                        (2,1),
                        (3,3)]
        self.actions={0: (-1,0),  # up
                     1: (1,0),   # down
                     2: (0,-1),  # left
                     3: (0,1)  # right
        }  
        
        self.state=self.start
        self.done=False
        
    def reset(self):
        self.state=self.start
        self.done=False
        return self.state
    
    def step(self, action):
        if self.done:
            raise Exception("Episode has ended. Please reset the environment.")
        if action not in self.actions:
            raise ValueError("Invalid action. Action must be one of [0, 1, 2, 3].")
        
        row,col=self.actions[action]
        
        new_row= self.state[0]+row
        new_col=self.state[1]+col
        
        new_state=(new_row,new_col)
        
        reward=-1
        if not (0<=new_row<self.row and 0<=new_col<self.column) or new_state in self.obstacles:
            new_state=self.state
        elif new_state in self.obstacles:
            new_state=self.state
            reward=-10
        self.state=new_state
        
        if self.state==self.goal:
            reward=100
            self.done=True
        return self.state, reward, self.done