class GridWorld:
    def __init__(self):
        self.state=0
        self.done=False
        self.goal=5
        
        self.states=list(range(self.goal+1))
        
        
    def reset(self):
        self.state=0
        self.done=False
        return self.state

    def step(self,action):
        action=action.lower()
        if self.done:
            raise Exception("Episode has ended. Please reset the environment.")
        if action=="left":
            self.state=max(0, self.state-1)
                
        elif action=="right":
            self.state=min(self.goal, self.state+1)
        elif action=="stay":
                pass
        else:
            raise ValueError("Invalid action. Please choose 'left', 'right', or 'stay'.")
        self.reward=-1
        self.done=False
        if self.state==self.goal:
            self.reward=100
            self.done=True
        return self.state, self.reward, self.done