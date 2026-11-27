
from environment import GridWorld
from first_agent import RandomAgent

# Create objects
env = GridWorld()
agent = RandomAgent()

# Number of episodes
episodes = 5

for episode in range(episodes):

    state = env.reset()

    total_reward = 0
    done = False
    steps = 0

    print(f"\nEpisode {episode + 1}")

    while not done:

        # Agent chooses action
        action = agent.choose_action(state)

        # Environment executes action
        next_state, reward, done = env.step(action)

        # Update total reward
        total_reward += reward
        steps += 1

        print(
            f"State: {state}, "
            f"Action: {action}, "
            f"Next state: {next_state}, "
            f"Reward: {reward}"
        )

        # Update state
        state = next_state

    print("Total reward:", total_reward)
    print("Total steps:", steps)
