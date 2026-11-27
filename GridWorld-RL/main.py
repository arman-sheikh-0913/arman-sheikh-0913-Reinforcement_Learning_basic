
from environment.grid_world import GridWorld

# Create environment
env = GridWorld()

# Reset environment
state = env.reset()

print("Initial State:", state)

# Agent chooses Right (action 3)
next_state, reward, done = env.step(3)

print("Next State:", next_state)
print("Reward:", reward)
print("Episode Finished:", done)
